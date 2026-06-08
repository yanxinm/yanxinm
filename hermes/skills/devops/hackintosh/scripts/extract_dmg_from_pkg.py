#!/usr/bin/env python3
"""Extract SharedSupport.dmg from an Apple InstallAssistant.pkg file.

Usage:
    python3 extract_dmg_from_pkg.py <InstallAssistant.pkg> [output.dmg]

The .pkg is a XAR archive. The TOC XML lists SharedSupport.dmg with its
offset and size within the .pkg — this script parses the TOC and extracts
the DMG directly via binary seek+read.
"""

import struct
import zlib
import os
import sys
import xml.etree.ElementTree as ET


def extract_dmg(pkg_path: str, output_path: str | None = None) -> str:
    if output_path is None:
        output_path = os.path.join(
            os.path.dirname(pkg_path), "SharedSupport.dmg"
        )

    with open(pkg_path, "rb") as f:
        # Verify XAR magic
        magic = f.read(4)
        if magic != b"xar!":
            raise ValueError(f"Not a XAR archive: magic={magic!r}")

        header_size = struct.unpack(">H", f.read(2))[0]
        f.read(2)  # version
        toc_compressed = struct.unpack(">Q", f.read(8))[0]
        toc_uncompressed = struct.unpack(">Q", f.read(8))[0]
        f.read(4)  # checksum_alg

        # Read and decompress TOC XML
        f.seek(header_size)
        toc_xml = zlib.decompress(f.read(toc_compressed)).decode("utf-8")

        # Find SharedSupport.dmg in TOC
        root = ET.fromstring(toc_xml)
        offset = size = None
        for file_elem in root.iter("file"):
            name_el = file_elem.find("name")
            if name_el is not None and name_el.text == "SharedSupport.dmg":
                data_el = file_elem.find("data")
                offset = int(data_el.find("offset").text)
                size = int(data_el.find("size").text)
                break

        if offset is None:
            # Print all files for debugging
            print("ERROR: SharedSupport.dmg not found in TOC. Contents:")
            for file_elem in root.iter("file"):
                name_el = file_elem.find("name")
                data_el = file_elem.find("data")
                if name_el is not None and data_el is not None:
                    s = data_el.find("size")
                    o = data_el.find("offset")
                    print(f"  {name_el.text:30s} offset={o.text if o is not None else 'N/A':>10s} size={s.text if s is not None else 'N/A':>12s}")
            raise SystemExit(1)

        print(f"Extracting SharedSupport.dmg ({size / 1024**3:.2f} GB)...")

        f.seek(offset)
        buf_size = 64 * 1024 * 1024  # 64 MB
        total = 0
        with open(output_path, "wb") as dst:
            while total < size:
                chunk = f.read(min(buf_size, size - total))
                if not chunk:
                    break
                dst.write(chunk)
                total += len(chunk)
                pct = total / size * 100
                gb = total / 1024**3
                total_gb = size / 1024**3
                print(
                    f"\r  {pct:.1f}% ({gb:.2f}/{total_gb:.2f} GB)",
                    end="",
                    flush=True,
                )

        print(f"\nDone! {total} bytes → {output_path}")

        actual = os.path.getsize(output_path)
        assert actual == size, f"Size mismatch: expected {size}, got {actual}"
        return output_path


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <InstallAssistant.pkg> [output.dmg]")
        sys.exit(1)
    extract_dmg(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)

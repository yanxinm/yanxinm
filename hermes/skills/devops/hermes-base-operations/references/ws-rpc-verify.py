#!/usr/bin/env python3
"""
WebSocket JSON-RPC 端到端验证脚本
模拟 Hermes Desktop 协议：session.create → prompt.submit → 接收事件流

用法：
  python3 ws-rpc-verify.py
  成功输出模型回复 "OK"
  失败输出异常信息
"""
import re, urllib.request, socket, ssl, base64, os, json, struct, time

host = 'miao-thinkcentre-m710q-n080.tail589fe7.ts.net'
html = urllib.request.urlopen('https://' + host + '/', timeout=8).read().decode('utf-8','ignore')
token = re.search(r"__HERMES_SESSION_TOKEN__\s*=\s*['\"]([^'\"]+)", html).group(1)

key = base64.b64encode(os.urandom(16)).decode()
s = socket.create_connection((host, 443), timeout=8)
w = ssl.create_default_context().wrap_socket(s, server_hostname=host)
w.settimeout(60)

w.sendall((
    f"GET /api/ws?token={token} HTTP/1.1\r\n"
    f"Host: {host}\r\n"
    f"Upgrade: websocket\r\nConnection: Upgrade\r\n"
    f"Sec-WebSocket-Key: {key}\r\nSec-WebSocket-Version: 13\r\n"
    f"Origin: https://{host}\r\n\r\n"
).encode())

resp = b''
while b'\r\n\r\n' not in resp:
    resp += w.recv(4096)
status = resp.split(b'\r\n', 1)[0].decode()
assert '101' in status, f"Handshake failed: {status}"
print(f"[PASS] Handshake: {status}")

def recv_frame():
    h = w.recv(2)
    if not h:
        return None
    b1, b2 = h[0], h[1]
    ln = b2 & 0x7f
    if ln == 126:
        ln = struct.unpack('!H', w.recv(2))[0]
    elif ln == 127:
        ln = struct.unpack('!Q', w.recv(8))[0]
    mask = w.recv(4) if (b2 & 0x80) else None
    data = b''
    while len(data) < ln:
        data += w.recv(ln - len(data))
    if mask:
        data = bytes(c ^ mask[i % 4] for i, c in enumerate(data))
    return b1 & 0xf, data.decode('utf-8', 'ignore')

def send(method, params, rid):
    text = json.dumps({'jsonrpc': '2.0', 'id': rid, 'method': method, 'params': params},
                      ensure_ascii=False)
    data = text.encode()
    mask = os.urandom(4)
    ln = len(data)
    out = bytearray([0x81])
    if ln < 126:
        out.append(0x80 | ln)
    elif ln < 65536:
        out.append(0x80 | 126)
        out.extend(struct.pack('!H', ln))
    else:
        out.append(0x80 | 127)
        out.extend(struct.pack('!Q', ln))
    out.extend(mask)
    out.extend(bytes(c ^ mask[i % 4] for i, c in enumerate(data)))
    w.sendall(out)

def wait_id(rid, max_frames=80):
    for i in range(max_frames):
        fr = recv_frame()
        if fr is None:
            raise RuntimeError('Connection closed')
        op, msg = fr
        if f'"id": {rid}' in msg or f'"id":{rid}' in msg:
            return json.loads(msg)
    raise RuntimeError(f'Response id={rid} not found in {max_frames} frames')

# Step 1: Read gateway.ready
op, ready_msg = recv_frame()
assert 'gateway.ready' in ready_msg, f"Expected gateway.ready, got: {ready_msg[:100]}"
print("[PASS] gateway.ready received")

# Step 2: session.create
send('session.create', {'cols': 120, 'close_on_disconnect': False}, 1)
r1 = wait_id(1)
sid = r1['result']['session_id']
print(f"[PASS] session.create → {sid}")

# Step 3: prompt.submit
send('prompt.submit', {'session_id': sid, 'text': '只回答 OK'}, 2)
r2 = wait_id(2)
assert r2.get('result', {}).get('status') == 'streaming', f"Expected streaming, got {r2}"
print("[PASS] prompt.submit → streaming")

# Step 4: Receive completion
for i in range(80):
    fr = recv_frame()
    if fr is None:
        break
    op, msg = fr
    if 'message.complete' in msg or 'error' in msg:
        data = json.loads(msg)
        if 'error' in data:
            print(f"[FAIL] {data['error']}")
            break
        text = data.get('params', {}).get('payload', {}).get('text', '')
        print(f"[PASS] message.complete: {text[:200]}")
        break
else:
    print("[FAIL] No message.complete within 80 frames")

w.close()

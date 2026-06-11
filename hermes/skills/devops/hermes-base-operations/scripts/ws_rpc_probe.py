#!/usr/bin/env python3
"""
Hermes Dashboard WebSocket JSON-RPC 端到端探针。
模拟 Desktop 完整协议：session.create → prompt.submit → 接收事件流。

用法：
  python3 ws_rpc_probe.py

环境要求：Python 标准库
"""

import re, urllib.request, socket, ssl, base64, os, json, struct, sys

HOST = 'miao-thinkcentre-m710q-n080.tail589fe7.ts.net'
TEST_PROMPT = '只回答 OK'
WS_TIMEOUT = 60
MAX_FRAMES = 80


def _extract_token(host: str) -> str:
    html = urllib.request.urlopen(f'https://{host}/', timeout=8).read().decode('utf-8', 'ignore')
    m = re.search(r"__HERMES_SESSION_TOKEN__\s*=\s*['\"]([^'\"]+)", html)
    if not m:
        raise RuntimeError('无法从 Dashboard 页面提取 session token')
    return m.group(1)


def _ws_connect(host: str, token: str):
    key = base64.b64encode(os.urandom(16)).decode()
    s = socket.create_connection((host, 443), timeout=8)
    w = ssl.create_default_context().wrap_socket(s, server_hostname=host)
    w.settimeout(WS_TIMEOUT)
    req = (
        f"GET /api/ws?token={token} HTTP/1.1\r\n"
        f"Host: {host}\r\n"
        f"Upgrade: websocket\r\n"
        f"Connection: Upgrade\r\n"
        f"Sec-WebSocket-Key: {key}\r\n"
        f"Sec-WebSocket-Version: 13\r\n"
        f"Origin: https://{host}\r\n\r\n"
    )
    w.sendall(req.encode())
    resp = b''
    while b'\r\n\r\n' not in resp:
        resp += w.recv(4096)
    status_line = resp.split(b'\r\n', 1)[0].decode()
    if '101' not in status_line:
        raise RuntimeError(f'握手失败: {status_line}')
    return w


def _recv_frame(w):
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


def _send_text(w, text: str):
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


def _send_rpc(w, method: str, params: dict, rid: int):
    _send_text(w, json.dumps({
        'jsonrpc': '2.0', 'id': rid,
        'method': method, 'params': params,
    }, ensure_ascii=False))


def _wait_rpc_response(w, rid: int, max_frames: int = MAX_FRAMES):
    for i in range(max_frames):
        fr = _recv_frame(w)
        if fr is None:
            raise RuntimeError('连接已关闭')
        _, msg = fr
        if f'"id": {rid}' in msg or f'"id":{rid}' in msg:
            return json.loads(msg)
    raise RuntimeError(f'超时：未收到 id={rid} 的响应')


def main():
    step = 0

    def log(s):
        nonlocal step
        step += 1
        print(f'[{step}] {s}')

    log(f'提取 Dashboard session token...')
    token = _extract_token(HOST)
    log(f'Token 长度 {len(token)}')

    log(f'WebSocket 连接 {HOST}/api/ws...')
    w = _ws_connect(HOST, token)
    log('握手成功 (101)')

    fr = _recv_frame(w)
    if fr is None:
        raise RuntimeError('未收到 gateway.ready')
    log(f'收到 gateway.ready')

    log('发送 session.create...')
    _send_rpc(w, 'session.create', {'cols': 120, 'close_on_disconnect': False}, 1)
    r = _wait_rpc_response(w, 1)
    sid = r['result']['session_id']
    log(f'会话创建成功: session_id={sid}')

    log(f'发送 prompt.submit (text="{TEST_PROMPT}")...')
    _send_rpc(w, 'prompt.submit', {'session_id': sid, 'text': TEST_PROMPT}, 2)
    r = _wait_rpc_response(w, 2)
    log(f'提交返回: {r.get("result", {}).get("status", "unknown")}')

    log('等待模型回复...')
    found_complete = False
    for i in range(MAX_FRAMES):
        fr = _recv_frame(w)
        if fr is None:
            break
        _, msg = fr
        if 'message.complete' in msg:
            payload = json.loads(msg)
            text = payload.get('params', {}).get('payload', {}).get('text', '')
            print(f'[OK] message.complete: "{text}"')
            found_complete = True
            break
        elif 'delta' in msg:
            pass

    w.close()
    print()
    if found_complete:
        print('发送链路正常')
        return 0
    else:
        print('未收到 message.complete')
        return 1


if __name__ == '__main__':
    sys.exit(main())

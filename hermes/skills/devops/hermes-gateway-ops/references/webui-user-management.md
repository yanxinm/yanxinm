# Web UI 用户管理（直接 SQLite 操作）

## 何时使用

Web UI v0.6.11 的 `/api/auth/change-password` 和 `/api/auth/change-username` 端点存在 bug——即使携带有效的 JWT Bearer token 也返回 401 Unauthorized。浏览器设置页修改用户名/密码时报错但无有用提示。

当 Web UI 的 API 认证端点不可用时，直接操作 SQLite 数据库是可靠的 fallback。

## 数据库位置

```
~/.hermes-web-ui/hermes-web-ui.db
```

## 前提：Node.js built-in SQLite

使用 Node.js ≥ 22.5 的内置 `node:sqlite` 模块（无需安装第三方包）。执行脚本时不要在 `~/.hermes/memos-plugin/` 等有其他 `node_modules` 的目录下运行——那里的 `better-sqlite3` native 模块可能与当前 Node 版本不匹配。`cd /tmp` 后执行。

## 查询用户

```bash
cd /tmp && node -e "
const {DatabaseSync} = require('node:sqlite');
const db = new DatabaseSync('/home/<USER>/.hermes-web-ui/hermes-web-ui.db');
const rows = db.prepare('SELECT id, username, role, status FROM users').all();
console.log(JSON.stringify(rows, null, 2));
"
```

## 重置密码

```bash
cd /tmp && node -e "
const crypto = require('crypto');
const {DatabaseSync} = require('node:sqlite');

const password = 'NEW_PASSWORD';
const salt = crypto.randomBytes(16).toString('hex');

crypto.scrypt(password, salt, 64, (err, derivedKey) => {
  if (err) throw err;
  const hash = 'scrypt:' + salt + ':' + derivedKey.toString('hex');
  const db = new DatabaseSync('/home/<USER>/.hermes-web-ui/hermes-web-ui.db');
  const now = Date.now();
  db.prepare('UPDATE users SET password_hash = ?, updated_at = ? WHERE username = ?')
    .run(hash, now, 'admin');
  console.log('Password updated');
});
"
```

**密码哈希格式：** `scrypt:<16-byte-hex-salt>:<64-byte-hex-derived-key>`

## 修改用户名

```bash
cd /tmp && node -e "
const {DatabaseSync} = require('node:sqlite');
const db = new DatabaseSync('/home/<USER>/.hermes-web-ui/hermes-web-ui.db');
const now = Date.now();
db.prepare('UPDATE users SET username = ?, updated_at = ? WHERE id = 1').run('NEW_USERNAME', now);
const user = db.prepare('SELECT id, username, role, status FROM users WHERE id = 1').get();
console.log(JSON.stringify(user));
"
```

## 验证新密码可用

```bash
curl -s -X POST http://localhost:8648/api/auth/login \
  -H 'Content-Type: application/json' \
  -d '{"username":"admin","password":"NEW_PASSWORD"}'
# 预期: {"token": "eyJ..."}
```

## 常见陷阱

- **不要用 `better-sqlite3`：** 系统可能安装了多个 Node 版本，`better-sqlite3` 的 native 绑定只匹配编译时的 Node 版本。用 `node:sqlite` (built-in) 避免此问题。
- **不要在项目目录下执行：** `cwd` 中的 `node_modules` 可能加载不兼容的 `better-sqlite3`。`cd /tmp` 后执行。
- **Web UI 的重启不需要：** 修改数据库后 Web UI 即时生效，不需要重启服务。

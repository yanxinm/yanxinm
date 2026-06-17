See: ~/.hermes/scripts/hermes-health-check.sh (canonical copy)

This is the health check script used by the cron job `Hermes 全链路自检 (每日2次)`.

Checks:
1. Gateway process (pgrep + ps etime)
2. Web UI (8648) HTTP response
3. Dashboard (9119) HTTP response
4. TDAI Memory (8420) port listening
5. Feishu — journalctl [Lark].*connected check
6. Weixin — Gateway process liveness inference

Config path hardcoded: all paths reference ~/miao (base machine user).
For use on other machines, update paths accordingly.

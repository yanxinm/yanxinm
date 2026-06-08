# External SIGTERM Kill Pattern (exit-diag Blind Spot)

## Observed Behavior

2026-05-31 12:16 CST — Gateway received an external SIGTERM, shut down
gracefully (notified active WeChat chat), but **no entry appeared in
`gateway-exit-diag.log`**.

The diag log's last `gateway.start` entry was from 01:35 UTC (PID 1120), with no
corresponding exit record for that PID despite it running from 01:35 until
12:16. This means:

1. **exit-diag.log is unreliable for SIGTERM kills from parent process groups.**
   When the bash wrapper process (parent) is killed, the Python atexit hooks may
   not execute before the child process terminates.

2. **gateway.log is the authoritative source** — it captured the full shutdown
   sequence including the SIGTERM signal, shutdown context, notification
   delivery, and phase timing.

## Gateway Log Signature (External SIGTERM)

```
INFO gateway.run: Received SIGTERM — initiating shutdown
WARNING gateway.run: Shutdown context: signal=SIGTERM under_systemd=no parent_pid=<N> parent_name=bash
```

Key difference from planned `--replace` takeover:
- Planned: `Received SIGTERM as a planned --replace takeover — exiting cleanly`
- External: `Received SIGTERM — initiating shutdown` (no "planned" qualifier)

## Root Cause Scenarios

1. **Windows Task Scheduler re-triggers** the startup script, which runs
   `hermes gateway run --replace`. The new instance sends SIGTERM to the old
   bash wrapper, but if the wrapper doesn't propagate --replace flags properly,
   the old Gateway sees it as an external signal.

2. **WSL shutdown/restart** sends SIGTERM to all processes in the WSL instance.

3. **Manual kill** of the bash wrapper process (e.g., closing the terminal
   window that launched the wrapper).

## Diagnosis When Gateway is Down with No Exit-Diag Entry

1. Check gateway.log for `Received SIGTERM` — this confirms it was a signal
   kill, not a crash.
2. Check the shutdown context line for `parent_pid`, `parent_name`, and
   `parent_cmdline` — these identify what sent the signal.
3. Do NOT trust exit-diag.log alone to rule out crashes — always cross-check
   gateway.log timestamps.

## Mitigation

No code fix needed — this is expected behavior when the parent process group
receives a signal. The diagnostic approach is: **gateway.log is ground truth;
exit-diag.log is a supplement, not a substitute.**

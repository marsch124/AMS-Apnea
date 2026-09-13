# AMS Apnea

Dry static-apnea training for the iPhone home screen — a personal replacement for a STAmina subscription.

- **Live app:** https://marsch124.github.io/AMS-Apnea/
- **CO₂ table** — same hold (share of your PB), rest shrinks 15 s per round
- **O₂ table** — 2:00 rest, hold grows each round up to a share of your PB
- **PB attempt** — breathe-up, then an open hold; the screen turns gold past your record and the PB updates itself
- Tap anywhere during a hold to log a contraction; press and hold 1 s to stop
- Voice + beeps for every change, full-screen colours, huge clock — usable eyes closed
- History with a PB chart, backups (share file / clipboard / restore), self-update via `version.json`
- Everything stays in `localStorage` on the device

**Land only. Never train breath holds in or near water.**

## Releasing a change
1. New entry at the **top** of `VERSIONLOG` in `index.html` (its `v` is the app version).
2. Same version in `version.json`. The service-worker cache name follows the version by itself.
3. Update "How this works" in Settings if behaviour changed.
4. Push to `main` — GitHub Actions deploys Pages.

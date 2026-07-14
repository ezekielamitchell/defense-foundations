# Defense Foundations Mobile PWA

This folder contains a static mobile-first Progressive Web App for the
`defense-foundations` repo. It gives you a phone-friendly dashboard for the P0
weekly plan, phase map, evidence links, and quick capture notes.

The current projection starts with Week 0 on 2026-07-14 through 2026-07-19,
then uses Monday–Sunday execution weeks from 2026-07-20. The six-week gate is
2026-08-30 and the eight-week maximum gate is 2026-09-13. Aegis Nexus
`01_Daily/_Phase Config.md` is the sole hard-date authority; this PWA is a
read-only projection.

The active `projects/file_stats` and `projects/hello-stats` paths are stubs/WIP.
Mobile checkboxes and notes are planning aids, not curriculum evidence.

## Run locally

From the repository root:

```sh
python3 -m http.server 4173
```

Then open:

```text
http://localhost:4173/mobile/
```

To open it on your phone while you are on the same Wi-Fi network, replace
`localhost` with your Mac's local IP address:

```text
http://YOUR_MAC_IP:4173/mobile/
```

## Install on a phone

- iPhone Safari: open the URL, tap Share, then tap Add to Home Screen.
- Android Chrome: open the URL and use the Install prompt or Add to Home screen.

The app shell is cached for offline use after the first successful load. Source
document links still need network or local server access unless the browser has
already cached them.

## Notes behavior

Quick capture notes are stored in the current browser with `localStorage`. They
are intentionally scratch space, not repo evidence. Promote useful notes into
Markdown when you are back at your desk.

## Publish with GitHub Pages

If the repository is published with GitHub Pages from the repo root, the mobile
app will be available at:

```text
https://YOUR_GITHUB_USERNAME.github.io/defense-foundations/mobile/
```

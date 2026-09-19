# Defense Foundations Mobile PWA

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

The app shell is cache-first for offline use after the first successful load.
The generated projection is network-first so a changed Aegis authority is not
hidden by an older cache; its last successful response remains available as an
offline fallback. Source document links still need network or local server
access unless the browser has already cached them.

The Phases view follows the [competency dependency route](../curriculum/COMPETENCY_PATHWAY.md). Current dates and status come from the generated Aegis projection; only demonstrated evidence and an explicit gate decision advance a phase.

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


## Active parallel curriculum — September 19, 2026

Static module labels follow the core/optional dependency route. The generated projection now reflects the activated September 19 parallel curriculum reset. Course reservations do not earn learning credit.
The app-shell cache version changes so a future served load can refresh labels;
no deployment or installed-browser cache refresh is claimed by editing source.
See [Start Here](../curriculum/START_HERE.md) and [Reset Handoff](../curriculum/RESET_HANDOFF.md).

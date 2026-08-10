# Defense Foundations Mobile PWA

This folder contains a static mobile-first Progressive Web App for the
`defense-foundations` repo. It gives you a phone-friendly dashboard for the P0
weekly plan, phase map, evidence links, and quick capture notes.

The current projection starts with Day 0 at 16:00 on 2026-08-09; condensed
Week 1 is that day only. Week 2 resumes the Monday–Sunday cadence on
2026-08-10. The six-week minimum gate is
2026-08-30 and the eight-week maximum gate is 2026-09-13. Aegis Nexus
`01_Daily/_Phase Config.md` is the sole hard-date authority; this PWA is a
read-only projection.

DD #85/#78 schedules two bounded **non-gate** overlays through 2026-09-13: the
Hugging Face AI Agents Course at a maximum of two linked blocks per full week
(consuming the deterministic-sampler allocation, never a fifth lane), and a
60-minute daily research paper at 08:00–09:00. The operating envelope is
Monday–Friday 09:30–23:00, Saturday 09:30–18:15, and Sunday 09:30–18:00
America/Los_Angeles, with 15-minute cross-domain transitions and protected personal
commitments. Foundations still control the gate; overlay proof stays separate.
Hugging Face, Udemy, projects, and foundation checklists all restart at zero.

The Phase 0 artifact is the paired file-statistics CLI. The active
`projects/file_stats` (Python) and `projects/hello-stats` (Rust) paths are stubs/WIP.
Mobile checkboxes use a new reset namespace, so earlier local checks do not carry
forward. They and mobile notes remain planning aids, not curriculum evidence.
Scheduling an agent block does not mark it complete.

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

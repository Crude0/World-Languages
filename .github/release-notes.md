**Every view now has a link.** Until now nothing you built on the map could be
shared: filter to a language, zoom into Anatolia, and the only way to show
someone was to tell them to do the same thing themselves. What is on screen now
lives in the address bar —

```
#l=en&p=pct&d=on&f=l.tr&v=489,208,422
```

— interface language, colouring (family / density / head count), detail level
(country / region), the filter, the selected country or province, the table
view and the viewport. A **Link** button in the toolbar copies the current
view's address to the clipboard. The format is the same in both interfaces, so
a link made on the desktop page opens correctly in the phone version.

Two deliberate decisions:

- **The theme is not in the link.** Light or dark is the reader's own
  preference and should not be imposed by a URL. The language is part of the
  content, so it does travel — and overrides the saved preference.
- **Writing is delayed.** Calling `history.replaceState` on every frame while
  panning is both expensive and hits Safari's rate limit; the URL is written
  once, 400 ms after the movement stops.

A broken or invented link does not break the page: every field that is not
recognised is quietly ignored and the default view opens.

**The browser version is installable and works offline.** A manifest, a service
worker and icons were added to the `docs/` copies; pick "Install" in Chrome or
"Add to Home Screen" on iOS and it opens like an app with no address bar, and
keeps working with the network completely down (measured: with the server
stopped the page still opens and makes zero requests). The desktop and phone
interfaces use separate manifests — otherwise installing from the phone would
have opened the desktop page.

This concerns only the published site. The packaged builds
(`dunya-dilleri.html`, the desktop app, the APK) are untouched: they are
already offline, and a service worker registration over `file://` is
meaningless.

**Continuous integration was added.** On every push and pull request: the data
and pages are built from scratch, **the published copy is verified to match the
templates**, and both interfaces are checked with Playwright. That last step
would have caught most of the regressions found by hand in this session.

**`build_subs.py` now actually downloads its source file.** The README had long
claimed it "downloads Natural Earth's 40 MB subdivision file on its first run",
but there was no download in the code — the file had been fetched by hand, and
`make` did not work in a clean checkout. Because the download can be truncated
silently (the first attempt returned 35 MB instead of 40 and the JSON stopped
mid-file), both the length and the parse are verified, and it retries on
failure.

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 513 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | 7.3 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.4 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

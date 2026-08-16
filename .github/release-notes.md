<!-- title: The downloads were actually 0.8.0 -->
**0.9.0, 0.9.1 and 0.9.2 shipped 0.8.0 binaries.** If you downloaded the .dmg,
its About panel said 0.8.0 and none of the new interface was there. The version
number, the notes and the tag were all correct — only the files were old.

The cause: `make desktop` writes the packages into `desktop/dist/`, which is in
`.gitignore`, while the release workflow uploaded the repository's `dist/`
folder. Nothing copied between the two, so `dist/` had been frozen since the day
it was last refreshed by hand — 0.8.0.

Both halves are now closed. The build moves the packages into `dist/`
(`make publish`), and a new check (`tools/check-dist.py`) looks inside them: the
mac bundle's `Info.plist` version, the version string baked into each binary,
and whether the page embedded in the APK matches the one in the repository. The
release workflow runs it before uploading and stops if it fails. Run against the
stale packages, it caught all four.

**Full screen left empty bars above and below the map.** The map is 2.29:1 and
screens are usually 16:10, so fitting the map inside the viewport left the rest
blank. The viewBox now takes its aspect ratio from the screen: the map fills it,
and zoomed in you see more around the edges instead of bars. At world zoom,
where the box ends up taller than the map, it is centred and the ocean simply
continues past the top and bottom, so there is no visible seam.

The Android APK is rebuilt from the current page as well. The phone interface
itself is still unchanged since 0.8.0 — that work comes next.

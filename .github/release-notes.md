**The DMG is now built on a real Mac.** I could not get the background image
in place across two releases: in 0.5.1 I built the alias record by hand, which
did not work; in 0.5.2 I reshaped that record to match exactly what
`mac_alias` writes on a Mac and made the image a plain PNG, which also did not
work. In both, the window size and the icon positions did take effect — the
`.DS_Store` was being read — but the background never appeared.

The reason is now clear: the alias record Finder uses to find the background
carries the file's real CNID and the volume's real creation date. Both can only
be produced while the image is mounted, by macOS's own calls; on Linux both are
invented, and Finder cannot resolve the record. There was no point guessing at
it a third time.

So the published disk image is now built by `dmgbuild` on a **macOS runner**:
the window, the icon positions and the background are written by macOS itself.
Two further gains come with it:

- The image is **HFS+** rather than ISO9660, which makes `bless --openfolder`
  work: the window now **opens by itself** when the image is mounted. That was
  the one thing that could not be done on ISO9660.
- The Retina representation is added with `tiffutil`, so the background is both
  1x and 2x — produced by Apple's own tool rather than guessed at.

`make desktop` still works on Linux and still produces a DMG; that one is plain
(ISO9660, no window styling). The published build is the macOS one.

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 513 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | ~8 MB |
| macOS, no disk image | `Dunya-Dilleri-Atlasi-mac.zip` | 3.2 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.4 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

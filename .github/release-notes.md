**The background image never showed up on a real Mac.** When 0.5.1 was tried,
the window size and the icon positions took effect — so the `.DS_Store` was
being read — but the background stayed black. The problem was the alias record
Finder uses to find the image. I went through what `mac_alias` writes on an
actual Mac line by line and rebuilt it the same way: the POSIX path relative to
the volume and **with a leading slash** (`/.background/bg.png` — the previous
attempt had no slash), the Carbon path in the library's own joining format. A
`pBBk` bookmark is now written alongside it, since modern Finder can read the
background from there too — whichever resolves.

The second suspect is gone as well: the background is no longer a
multi-representation, JPEG-compressed TIFF but a **plain PNG**. It is a touch
softer on a Retina display, but there is nothing left in it that could fail to
decode. Sharpness is easy to bring back once the image is confirmed to appear.

**OKU-BENI.txt is out of the DMG.** It stuck out as a third icon in that
otherwise clean window (and made Finder say "3 items"). The text moved inside
the app, at `Dunya Dilleri Atlasi.app/Contents/Resources/OKU-BENI.txt`. The
install and first-launch notes are also here in the release and in the README.

**A .zip for people who do not want a disk image.** The app was already being
packaged as a `.zip`, it just was not published; it is in Releases now. Unzip
it, drag the app to Applications, done — no mounting step at all. Having the
window open by itself on mount is not something I can arrange: that flag lives
in the HFS+ volume header, this image is ISO9660, and there is no tooling to
produce HFS+ on Linux (the one candidate, `machfs`, writes only the old HFS
that Catalina no longer mounts). So for anyone the mount dance annoys, the zip
is the honest answer.

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 513 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | 8.6 MB |
| macOS, no disk image | `Dunya-Dilleri-Atlasi-mac.zip` | 3.2 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.4 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

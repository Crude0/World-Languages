**The DMG finally opens a proper install window.** Until now the disk image
opened bare: no background, no place for the icons. You had to find the .app
yourself and drag it to your Applications folder.

How a disk image looks on macOS is written in a `.DS_Store` file at its root:
the window size, the view mode, the background image and the coordinates of
every icon. Normally you have Finder write that file on a Mac; there is no Mac
here, so `desktop/dmg_window.py` produces it directly. The window is 768×512
with the sidebar and toolbar off, the app on the left and Applications on the
right — both centred in the dashed frames of the background art.

The background is stored at 1x and 2x in a single TIFF so it stays sharp on a
Retina display. JPEG compression brings it from 6.3 MB down to 1.7 MB.

The mounted volume now carries the app's icon through `.VolumeIcon.icns`, so it
is something you spot in the Finder sidebar rather than something you hunt for.

**Two bugs in the application icon.** When writing the `.icns`, `make_icon.py`
did not include the 8-byte header in each chunk's length field, so the file
could not be parsed past the second chunk — of the eight sizes in it, only the
first was readable. The icon was also still being drawn with the washed-out
palette from before 0.3.0; it now uses the app's own colours.

**What could not be done:** having the window open by itself when the image is
mounted. That flag lives in the HFS+ volume header, and this image is ISO9660 —
there is no tooling to produce HFS+ on Linux. Finder usually opens the volume
on its own when you double-click a .dmg; when it does not, it cannot be forced
from the image.

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 513 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | 9.5 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.4 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

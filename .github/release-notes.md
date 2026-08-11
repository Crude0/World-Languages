**The stutter while panning: found and measured.** This had been chased by
guesswork for several rounds — a compositor transform was tried (wrong, it left
a blank gap at the edge), canvas was considered (measured, it came out slower),
viewport culling was added (correct, but not enough on its own). This time
nothing was guessed: Chrome's own trace records were used to sum the
`RasterTask` time spent over a fixed two-second drag. Every repetition reloads
the page and returns to the same viewBox, otherwise the place the previous drag
left the map shifts the next measurement by 25%.

The answer is unambiguous: **70–80% of the time goes into stroking.** Fills, the
hatch patterns on creoles, the ornaments and the graticule cost nothing
measurable — turning all of them into flat colour changed nothing. Turning every
stroke off takes the world view from 2,535 ms down to 451 ms.

Stroke cost turned out to depend on two things: the pixels it paints (dropping
the width from 1.2 to 0.5 cuts the cost to a third) and the number of points
(20,547 points down to 7,715 saves 58%). Three fixes followed:

- **Coarser geometry when zoomed out.** In the world view one map unit is 0.74
  pixels, so most of the points along a country border are sub-pixel detail.
  Below 1.0 px/unit the simplified path is used (20,547 → 10,417 points), above
  it the full one, with hysteresis in between. The coarse version is computed in
  the browser right after startup — it **adds no bytes to the data file**.
- **Antialiasing off during a gesture.** The phone interface already did this;
  the desktop one did not. On a map in motion the difference is invisible; on
  its own it saves 20–29%.
- **Each line is stroked once.** In region mode the outer edge of a country used
  to be produced like this: *every* province path was stroked, then covered over
  by the province fills. So every interior border was drawn twice and then
  hidden — 21,628 points of stroking for a thin line visible only at the edge.
  `build_subs.py` was already counting edges; it now also emits the ones that
  occur once as a separate network (`outer`, 12,173 points), and the base layer
  is fill only. In region mode the country outline of subdivided countries is
  no longer stroked either: the new network already draws that same line.

Measured result (1440×900, 2 s drag, rasterisation time):

| view | before | after |
|---|---|---|
| world (country mode) | 2,535 ms | **1,234 ms** (−51%) |
| region mode, 3.6 px/unit | 2,252 ms | **1,539 ms** (−32%) |
| region mode, 8 px/unit | 1,404 ms | **1,212 ms** (−14%) |

**Some things were tried and dropped.** Since TopoJSON arcs are already shared,
deduplicating country borders looked attractive; counting showed the gain was
only 20% of the geometry (1,482 of the 1,841 arcs belong to a single country —
coastline, already drawn once), and measuring showed a 2% difference. Moving the
stroke off the filled path onto a separate unfilled network gained nothing
either. Neither was done.

**A side effect: the international border is now distinguishable from a province
border.** 0.3.1 claimed to have fixed this, but the job was half done — the
US–Canada border still looked exactly like a state line. The new outer-edge
network genuinely fixes it.

**A bug in the culling list.** The list that skips paths outside the viewport is
rebuilt when the geometry level changes. Because `getBBox` returns 0×0 for a
hidden element, any path that happened to be off-screen at that moment fell out
of the list and never came back (19 of 234 countries missing after returning to
the world view). Hidden states are now cleared before the list is built.

**The map can be driven from the keyboard.** `#map` is focusable; the arrow keys
pan (Shift for a large step), `+`/`−` zoom, `0` returns to the world. There was
no way to zoom without a mouse.

On the phone interface, the invisible touch targets of small countries were also
added to the culling list.

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 509 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | 7.3 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.4 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

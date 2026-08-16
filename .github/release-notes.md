<!-- title: Panning got 20× cheaper -->
### Panning: 774 ms of raster down to 39 ms

Panning in full screen, zoomed into Europe with regions on, stuttered badly. My
first measurement was wrong: a frame counter reported 60 fps in every case,
which proves nothing — `requestAnimationFrame` keeps ticking even when raster
cannot keep up. Measuring rasterisation through the tracing API, for a
one-second drag:

```
full screen, Europe, regions   raster 774 ms / 1465 tasks
windowed                       raster 389 ms /  600 tasks
all strokes off                raster 779 ms      ← no change
hatch patterns flat            raster 804 ms      ← no change
device pixel ratio 1           raster 794 ms      ← no change
```

Not the strokes — the 0.4.0 stroke work holds. The cost is tile count: changing
`viewBox` every frame invalidates the whole layer, so every tile is
re-rasterised, and doubling the area doubles the work.

The gesture now freezes `viewBox` and translates the layer with a CSS
transform. This was tried once and reverted, because the compositor can only
move pixels it has already drawn and the trailing edge went blank. The
difference: the map is now drawn **28% beyond the visible area on every side**,
and the buffer is redrawn once when that margin runs out.

```
full screen, Europe, regions   774 → 39 ms   (1465 → 56 tasks)
windowed                       389 → 20 ms
```

Correctness was checked separately: after a drag longer than the margin the
`viewBox` deviates by **0.000** map units, the set of culled paths and hit tests
at five points are identical to the unbuffered path, and every inline style is
cleaned up when the gesture ends. No blank edge mid-gesture.

### Borders are drawn at the level the data exists

France has data per région, not per département — but the map drew every
département boundary, so it looked as though you could pick Manchester by hand,
while hovering said "England". The same in Spain, Italy and the UK.

The border network now compares the *data units* on either side of an edge
rather than the administrative units in the source file: if both sides fall in
the same unit, the edge is not drawn at all. The inner border network went from
**11,883 points to 9,445**, and from 126 buckets to 99.

The UK becomes its four nations, France its 18 régions, Spain its 19 autonomous
communities, Italy its 20 regions. Türkiye's 81 provinces, Germany's 16 states
and Russia's 83 federal subjects are unchanged — the data is already at that
level there.

### The country card in full screen

It now stretches to the bottom of the panel column instead of scrolling inside
a fixed box, stopping above the scale strip when that is visible.

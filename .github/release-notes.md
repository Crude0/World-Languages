<!-- title: The bubble stops stuttering -->
**The bubble's foil was rewritten: a silver prism, real parallax, 60 fps.** The
light sweep in the previous release was both too showy and janky. In its place
is a faint silver prism texture that is there even at rest, while the glare
appears only when the pointer moves onto the bubble — very faint, with the
layers sliding at different rates as it moves.

The stutter was not caused by the effect being heavy. It was caused by animating
the wrong property, twice over:

- The bubble's "alive at rest" drift animated registered custom properties, and
  those properties appeared inside `calc()` in the `background-position`,
  `mask-position`, `box-shadow` and `filter` of five different layers. So every
  one of them repainted on every frame even when the mouse never moved. Median
  frame time 50 ms — 20 fps.
- Moving the parallax to `transform` was not enough on its own, and in fact made
  things worse. Measured: `mix-blend-mode` defeats compositor-only movement. A
  blended layer has to read the backdrop underneath it, so it cannot be
  composited independently, and every `transform` change re-rasterises the whole
  group. Shrinking the layers to card size made no difference at all (50.0 ms
  versus 50.0 ms), which proves the cost was the blending rather than the raster
  area. The "adds light" look that blending provided is now baked straight into
  the colours, since the bubble's own background is known to be dark.

There was also a third problem: what looked like parallax was not parallax. The
mask sat on the moving layer, so the pattern and the window showing it slid
together and no relative motion was left — the result is a flat image sliding
around. The window is fixed now and the pattern slides behind it. Measured
relative travel: base −37 px, prism −137 px, glare +241 px, a 378 px spread
between layers.

The stepping on hover was a separate fault: the 0.22 s `transform` transition
restarted on every `pointermove`. The transition is gone and the smoothing moved
into a `requestAnimationFrame` loop that advances a fixed fraction toward the
target each frame, so nothing restarts and sparse pointer samples get filled in.

**Nothing moves at rest.** Light drifting continuously behind text you are
trying to read is distracting, so the whole effect is now tied to the pointer
and an idle page spends no frames at all. The tilt was eased off too: it was
44°/30°, it is 26°/17° now.

Measured result: **0 long frames out of 220** while the pointer sweeps across the
bubble, **0 out of 238** at rest, with a median frame time of 16.7 ms in both.

<!-- title: The crash, and a PNG worth keeping -->
**The macOS app crashed on pressing PNG.** The bridge ran for real for the first
time in 0.12.1, and one line inside it took the process down: the call that
reports the result back to the page,
`evaluateJavaScript:completionHandler:`, was handed `$()` where a block was
expected. Passing an object where ObjC wants a block crashes at a level
JavaScript's `try/catch` cannot reach. It now passes a real empty function.

The reason that line slipped through was the reach of the check: 0.12.1's check
mode exercised only the file-writing path, not the callback. Writing passed, and
the crashing line was never reached. The check now runs both, and the release
workflow looks for a third gate (`geri bildirim: ok`) — so if it crashes, it
crashes on a real macOS runner rather than on your machine.

Two safeguards alongside it: if the callback never arrives the button no longer
waits forever (the file is written *before* the callback, so a timeout assumes
success), and the Downloads folder is created only if it is genuinely missing.

**The exported PNG came out at a tiny resolution.** The output size was derived
from the view box's *map units* (`vb.w × 2`), so zooming in shrank the box and
shrank the export with it — around 387×837 on a phone. The long edge is now
targeted in pixels (2800) and the scale derived from that, with ceilings for the
canvas limit and WebView memory. Measured: on the phone both the world view and
a 16× zoomed view come out at 1375×2800, and the desktop at 2800×1226. Because
Chromium re-rasterizes the SVG at the destination size, the result is genuinely
sharp rather than an upscaled bitmap — that was measured too.

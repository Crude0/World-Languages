<!-- title: The phone gets the same fix -->
### Same cause on the phone, same fix

The stutter on the phone came from the same place as on the desktop. Measured
(Pixel 7, Europe, region mode, one-second drag): **398 ms of raster over 613
tasks**; turning off every stroke gave 371 ms, so it is not the strokes there
either.

The gesture buffer is now on the phone too: **398 → 80–88 ms** (613 → ~275
tasks), consistent over three runs. The margin is 0.28; 0.5, 0.8 and 1.1 were
measured as well and were no better (81 / 88 / 90 ms).

Porting it surfaced a bug. The phone's drag took its scale from
`svg.getBoundingClientRect()`. Because the buffer draws the SVG larger than the
visible area, that scale shrank and the map lagged behind the finger — 116
pixels of movement for 180 pixels of drag, exactly the buffer ratio. It now
measures `#stage`, which is what the comment in that code already said it
should do. Deviation after a drag is **0.000**.

### "I speak" comes to the phone

The new red-to-green scale (worst neighbouring gap ΔE 9.5) is used on the phone
as well; the old one was a single hue. With no cursor there, the place card does
what the desktop tooltip does: the share of the population you could talk to,
how many people that is, and the three languages contributing most.

The border dissolve comes from the data, so it applies on the phone too: the UK
4, France 18, Spain 19, Türkiye 81.

### Two desktop fixes

**The card ends where its text ends.** In 0.10.0 I had it fill the column, so a
short card left the glass box running on into empty space. It is now as tall as
its content, capping and scrolling when it does not fit (Belarus: 702 px box for
700 px of content; India: 779 px box for 1050 px of content).

**The glass drops its blur during a gesture.** While panning, the glass showed a
stale image that took seconds to catch up. That was a side effect of 0.10.0: the
map is now moved by the compositor and not re-rasterised, so the source that
`backdrop-filter` samples was not refreshing either. The blur now turns off for
the duration of the gesture and settles when it ends — which is what the phone
interface already did.

<!-- title: Hovering a family leaves only it on the map -->
**Hovering a family in the legend now leaves only that family on the map.**
Clicking sets the filter for good; hovering only shows: the rest of the world
fades to muted land, the family keeps its colour, and everything returns when
the pointer leaves. A 0.22s colour transition, none at all with "reduce
motion" on. It works from the bottom bar in fullscreen too. It stays out of
the way while a filter is already active — the map is answering that question
already.

This is the thing that was promised for a few releases and never actually
shipped: the trial lived on a local branch behind `#anim=1` and never made it
to `main`. The fade works through fill and needs `!important`, because in the
density and people paint modes the colour is written into the `style`
attribute and nothing else can override it. Measured: 596 nodes fade under
Germanic, 655 under Romance, zero once the pointer leaves; median frame 16.7ms.

**The "Speakers" button sat outside its box.** In a 300px column the heading
takes 86, the three-way switch 182 and the gap between them 8 — four pixels
more than the 272 available, so the third button was clipped. The side padding
went from 13 to 11 and the button padding from 8 to 6; there are twelve pixels
of slack now. The header row can also wrap: if the type gets bigger the switch
drops to its own line instead of being cut off.

**An empty frame trailed off to the right of two buttons in the "I speak"
sheet.** The Share / Home language switch stretched to the full line inside a
vertical box — 272 pixels of frame around 146 pixels of content. It is as wide
as its content now.

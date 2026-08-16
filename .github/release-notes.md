The desktop interface has been reworked: the controls moved onto the map, there
is a full-screen mode, and the **I speak** layer got a new colour scale and a
tooltip that answers the question it was always about.

### Sixteen controls in one row

The title bar carried four layers, three colour modes, three levels of detail,
clear-filter, table, link, PNG, SVG and three zoom buttons — all side by side.
Every new map mode made it a little more crowded.

They now live on the map. The bar keeps only the title; a three-button glass bar
floats over the map — **View**, **Table**, **Share** (plus **Clear filter** when
one is active). Layer, colour and detail are grouped in the View sheet, each
group with a line saying what it does. Export lives in the Share sheet. The zoom
stack sits in the opposite corner.

### Full screen

The map was sometimes small on screen. **⛶** hands it the whole viewport — page,
sidebar and cards go away. It uses the Fullscreen API where available, so the
browser chrome goes too, and falls back to a fixed overlay where it is not.
Because the controls are already on the map, both modes share one layout. The
macOS app has it in the View menu as **Map Only (⇧⌘F)**.

The panels can sit on the left or the right edge (⇄); the choice is stored in
your browser.

Floating surfaces are frosted glass — the map shows through, so you can see what
a panel is covering. Where `backdrop-filter` is unsupported, or the system asks
for reduced transparency, they fall back to a solid panel colour: legibility
comes before the material. The rest of the page is unchanged.

### I speak: a percentage in the tooltip, a new scale

Hovering a country now tells you **what share of its population you could talk
to**, how many people that is, and the three languages contributing most.

The colour scale changed too. It used to be one hue running dark to light; the
smallest CIEDE2000 gap between neighbouring bins was **4.5**, which is why China
and Afghanistan looked alike. The new scale runs red to green with a worst
neighbouring gap of **9.5**, measured under normal vision and all three kinds of
colour blindness. A plain red-to-green ramp was tried first and was worse: under
protanopia neighbours fell to **1.1** and the two ends were only 3.1 apart. What
ships instead is a smooth curve searched in OKLCH whose lightness also rises
monotonically (ends 50.7–77.3 apart).

### The macOS About panel

It had no copyright line, and showed a generic folder icon instead of the app's
own. It now reads **© 2026 Crude**, shows the real icon, and the build number in
parentheses is gone — that was osascript's, leaking through. The release
workflow checks all three on a real macOS runner.

### Fixed along the way

- Opening the table hid the whole map area; once the controls moved there, the
  button that closes the table went with it.
- The tooltip only had its opacity zeroed when hidden, so its box stayed in the
  layout and could push the page sideways when the window was narrowed.
- A local variable in `hover()` shadowed the translation accessor.
- The number of countries with region data still read 12 in three places; it
  became 18 in 0.7.0.

The phone interface is unchanged in this release.

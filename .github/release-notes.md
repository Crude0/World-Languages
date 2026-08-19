<!-- title: The legend leaves the left edge -->
**In fullscreen the legend moves off the left column and into a bar along the
bottom.** A nine-row list was covering the most readable edge of the screen
end to end. The bar spans the width and is 47 pixels tall: a thin spectrum
along its top edge showing each family's share of countries, badges below it.
The dimming and the frosted glass stay, and clicking a badge still filters —
pressing Germanic from the bar keeps 50 countries blue and drops 178 to grey.

Fitting it on one line was arithmetic, not trial and error: nine badges with
the English names want 1483 pixels, and the "LANGUAGE FAMILIES" heading was
exactly the 155 pixels that split that line in two. The heading is gone
visually — it stays for screen readers, since the section's accessible name
comes from it — and the type and inner spacing came down a notch. The result
is one line from 1366px in English and from 1180px in Turkish; below that it
wraps to two, and the bottom-corner controls and the scale strip follow the
bar's new height.

**Entering and leaving fullscreen is no longer a jump cut.** The map box's
position before and after the mode change is measured, the difference applied
as an inverse transform, and then animated to identity. 420ms, transform only,
so every frame stays on the compositor: median frame 16.7ms. The controls fade
in and the legend bar rises from below.

The trap here was *when* the measurement happens. The button calls
`requestFullscreen()`, and the browser stretches the overlay to the screen the
moment it grants the request — so by the time the mode-switching code ran, the
"before" position was already the after position and the animation never
started. The measurement now happens before the request. Because real
fullscreen also enlarges the viewport, if the two measurements fall on
different sides of that change the translation is dropped and only the ratio
is kept — a soft zoom in place beats growing from the wrong corner.

**The release check now looks at the stylesheet's integrity too.** This round I
wrote a selector twice; one extra opening brace swallowed every rule after it
and the map came out solid black — no console error, no crash, so it could
have shipped quietly. `check-desktop.mjs` now checks the rule count and a
known outcome: is Brazil still Romance red. It was tested against a
deliberately broken copy, saw 58 rules instead of 410, and failed the build.

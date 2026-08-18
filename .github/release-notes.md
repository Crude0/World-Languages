<!-- title: Same family, different shade -->
**The same colour no longer reads as the same language.** The family colour
stays what it was, but each language within a family now takes a different
lightness step — Brazil separates from its Spanish-speaking neighbours,
Portugal from Spain, and the Balkans stop being one purple block.
**Settings → Shade**, off by default.

How many steps this needs was computed, not guessed. A country adjacency graph
was derived from Natural Earth's shared border arcs (316 land-border pairs) and
coloured within each family: **four steps are enough for all nine families**,
with zero violations — no two land-bordering countries in the same family ever
land on the same shade. The four languages spread across the most countries in
each family get fixed steps, so Spanish/French/Portuguese/Italian and
English/German/Dutch/Swedish read apart everywhere in the world.

The ladder is built in OKLCH: hue fixed, only lightness moving, with chroma
pulled in slightly on the lighter steps. The smallest gap between neighbouring
steps is ΔEok 0.089. Distinct fills on the map go from 9 to 36. The rules hang
off a single class, so switching it costs no redraw, and the choice travels in
the share link.

What the shade does not tell you: **a step does not identify a language**, it
only guarantees that neighbours differ. Spain and Romania share a shade because
they do not border each other. Of the 121 languages that are the majority
somewhere, 98 are the majority in exactly one country; giving each its own
shade would have meant an unreadable map.

**Turkish text was left behind in the English interface.** Button tooltips and
accessibility labels came only from the Turkish skeleton the page starts from;
switching language never touched them. 27 strings on the desktop and 9 on the
phone are now bound to the language. The count is down to zero — what remains
are the languages' own names (Français, Türkçe, Sängö), as it should be.

**The selection label on the map stayed Turkish too**, for two different
reasons: on the desktop the country name never went through the translating
function at all, and on the phone the marks were not redrawn when the language
changed. Both fixed.

<!-- title: Zero gets its own colour -->
**Zero now has a colour of its own.** Pick Kurdish and you can talk to 0.9% of
Sweden and to nobody at all in Norway — yet both fell into the ramp's first bin
and the map said "neither". True zero is a deep maroon now; the threshold is
0.05 because everything below it already prints as "0.0%". The scale gained a
zero swatch at its head, on the phone too.

**Kurdish was missing entirely from France, the Netherlands, Belgium and
Denmark.** The migrant-community table is hand-built, and Kurdish had only been
entered for Germany, Sweden, Austria and Switzerland — while France hosts the
largest community after Germany (150,000–240,000). All four were added. Norway
was deliberately left out: no reliable figure turned up, and a gap is better
than an invented number.

The table was swept as a whole — a matrix of 20 destination countries against
24 migrant languages — and it showed further gaps (Persian in France, Belgium
and the Netherlands; Filipino in the UK, Italy and Spain, among others). Those
are not in this release: each needs a source, and they will be handled in a
round of their own.

**The card's three figures overlapped in Turkish.** "anlaşabildiğiniz" is a
single unbreakable word that wants 99 pixels in an 85-pixel column, so it ran
over its neighbour. The labels were shortened, the column gap opened up, and
long words are now allowed to break — better hyphenated than clipped in some
other language or at a larger type size.

**The walkthrough's door moved out of the View sheet and next to the
questions:** a small question mark to the right of the second one. The
first-visit bubble now hangs off that button — anchored to the question it was
covering the very button it advertises, and both offer the same thing. The
highlight chain after the walkthrough grew to three stops: the language picker,
the fullscreen button, and — once you leave fullscreen — "you can open the
walkthrough again from here". The third one waits for the exit on purpose,
because the button it points at lives in the masthead, which fullscreen hides.

**The bubble returns once after every update.** The "seen" flag stores the
version now, and since telling someone who already picked their languages to
pick their languages is pointless, they get "the atlas has been updated" and
the walkthrough instead. The version is planted into the page at build time.

**Changing layer now looks like changing question.** Home ↔ Script ↔ Official
melts the map into its new colours and lifts the caption and the column card as
they refresh — the same half-second fill transition.

On a narrow screen the bubble was making the page scroll sideways: left-aligned,
its right edge sat at 587 pixels on a 360-pixel screen. It is right-aligned now,
with its width tied to the viewport.

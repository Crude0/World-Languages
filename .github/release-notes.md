<!-- title: Now you can actually see it -->
**The foil shipped in 0.23.0 worked, but you could not see it.** Mechanically it
was all in place — the pointer variables were being written, the layers were
sliding — it just sat below the threshold of visibility: the change between two
pointer positions averaged 9.3 units of brightness. On a bubble that is 309×81
pixels, nobody notices that. The numbers had been chosen on 336-pixel demo cards
viewed at 2× in a contact sheet, and they did not survive the real size. The
prism now goes to 42% on hover instead of 16.5%, and the stripes carry more
contrast of their own — the same measurement now reads 14.7 on average and 83.6
at most, with the pattern's peak-to-trough exceeding 100 units.

**At rest the bubble is genuinely one flat colour now.** The prism texture had
been left switched on at rest; measured, it put a 13.1-unit ripple across the
bubble that never moved — it read as dirt rather than as a surface. Every layer
is now multiplied by the pointer term, so the resting peak-to-trough is 0.0.

Turning the strength up dropped the text contrast to 3.1, so two things changed.
The troughs of the prism stripes became fully transparent — with dark-to-light
midtones, the price of amplitude was a rising mean, and transparent troughs keep
the amplitude while halving it. And a plate was placed behind the text, fading
out from left to right: the foil shines freely on the right-hand side while the
text keeps its own ground. Contrast is 8.2 in the dark theme and 9.7 in the light
one.

Performance is unchanged: 0 long frames out of 219 on hover, median frame time
16.7 ms.

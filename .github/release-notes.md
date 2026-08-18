<!-- title: The card moves beside the map -->
**The selected place's card is no longer below the map — it is beside it.** You
had to scroll down to see the card of a country you had just clicked. On a wide
screen a third column now opens and the card lives there. Below 1360px the
column dissolves and the card returns to its old place under the map, so
nothing changes on a narrow screen.

Alongside it, the desktop's typography and map plate were reworked: Newsreader's
optical size axis is switched on (letters thin out by themselves at display
sizes), the headline goes to 3.1rem with tracking pulled to −.032em, and the
masthead figures become a band, each with its own vertical rule. The map's
printed-plate frame — a 1px border with a second hairline inside it — gives way
to an 8px radius and a soft elevation; the source line moves to small caps; the
legend swatches are round.

**The legend is now within reach in fullscreen.** With the side panel gone there
was nothing left to say what the colours meant. Rather than rendering a second
copy, the key itself moves into the glass column — so clicking a family still
filters the map — and returns to the panel on exit.

**A country's name did not sit in the middle of it.** The label was placed 18
pixels below its anchor: that nudge exists to clear the pin drawn for small
countries, but it was applied even when no pin was drawn, and since text aligns
on its baseline the body of the word fell a few pixels lower still. The nudge
now applies only when there is a pin; otherwise the name is centred on the
anchor.

There was nothing wrong with the anchor itself, and that was measured: in all
177 countries the anchor falls inside its own polygon, and its distance to the
nearest edge is a median 0.625 of the equivalent radius (Poland 0.742). A pole
of inaccessibility is not a visual centre — in concave countries it moves to the
widest place the label can sit, which is exactly what it is for.

**The hover tooltip follows the layer too.** On the script layer, hovering a
country gave you the language spoken at home rather than "Latin", and the same
on the official-language layer. The tooltip now follows the same rule as the
card: the script on the script layer, the state's language on the official
layer, along with whether the home language is official at all.

Fixing it turned up one more untranslated Turkish string inside the tooltip
("· no majority"): it only shows for the 21 countries without a majority
language, which is why the earlier sweep never caught it.

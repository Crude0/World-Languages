<!-- title: The map grows into the empty column -->
**With nothing selected, the map now grows into the card column.** The column
sat there as an empty 312px strip whenever it had nothing to show. It now
starts closed and gives that space to the map: in a 1500px window the map goes
from 776 to 1110 pixels, 43% wider. Click a place and the column opens again,
handing the space back — both on the same 0.44s curve.

The column gutter was moved out of the grid and onto the column's own margin
for this: `gap` stays put even when the third track collapses to zero, which
left a 22px dead strip to the right of the map. Because the card widens along
with the column, its text spends the first moments wrapping inside a narrow
box; the column reaches 94% of its final size in 220ms, so a dimmed opening
covers exactly that phase. The box the pointer-to-map conversion relies on is
refreshed during the transition and again when it ends, otherwise clicks would
land off-target afterwards. With "reduce motion" on there is no transition, the
size just lands; below 1360px there is no column to begin with, so nothing
changed there.

**The masthead figures broke into two rows in English.** The fourth figure
("21 · no majority language") dropped to a second line, its left rule hanging
in empty space and its number tucked under the label above it. The cause was
how a flex row decides where to break: it measures each item unwrapped, so the
long label counted as one unbreakable piece and pushed the band over. Turkish
labels are short, which is why only English showed it. The band is a grid now —
the first three columns size to their content, the fourth takes what is left
and wraps its label inside its own cell. Below 560px it becomes a 2×2 block.

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

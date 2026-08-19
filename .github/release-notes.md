<!-- title: The atlas asks two questions now -->
**The atlas answers two questions, and it now says so under the headline.**
"I speak" was a two-word button in a glass bar floating over the map — someone
seeing the app for the first time could not find it at all. Two tabs sit under
the headline instead: *What does the world speak?* and *Who could you talk
to?* Switching to the second changes the headline and the standfirst too, so
the page states which question it is answering. The feature stopped being a
mode setting and became one of the two things the atlas does.

The tabs are set in the headline's serif at 22px; the language and theme
switches in the masthead are 11px sans, so the two never read as the same kind
of control. The inactive tab always carries an arrow, which slides three
pixels on hover while the underline draws itself left to right. The arrow
occupies space on both tabs, so nothing shifts when the selection changes.

**Each question shows only its own tools.** In the second one the language
index, the "most spoken languages" band and the layer/colour/shade groups in
the View sheet all step aside; what remains is your languages, the reach map
and its ramp. In the first one "I speak" appears nowhere — it left the layer
list, and the button over the map now shows only in fullscreen, where there is
no masthead. One entry point per context.

**The language picker moved off the map and into the left column.** That column
was already getting short in the second question; with the picker there, the
map is never covered. Below 1000px and in fullscreen it goes back to being a
sheet. Two identical representations were removed along the way: the column's
card and the sheet were both printing the same three figures, the same
Share/Home switch and the same note.

**Transitions.** The line under the tabs is no longer each tab's own border but
a single bar that slides between them (0.44s; its width comes from the label,
and across seven widths in two languages it lands within 0 pixels). The
headline, the standfirst and the column card rise seven pixels as they change.
The map melts into its new colours: the fill transition is switched on only for
that half second — leaving it on would slow every filter and layer change too.

**A first-visit bubble, and a short walkthrough.** The bubble appears once, only
when no languages have been picked, and points at the second question. A light
travels around its edge: the angle of a conic gradient turns once every 3.4
seconds and the gradient shows only in the border. Clicking the bubble opens a
four-step walkthrough — the page dims, only the part being explained stays lit,
and the hole and the caption slide between steps. The last step's button
switches to the second question and opens the picker. Esc leaves, arrow and
Enter advance.

**The selected country's card depended on the language list but wasn't
listening to it.** Click a country first and a language second, and the card
stayed as it was, still leading with the country's home language instead of how
many people you could talk to there. It is redrawn when the list changes now.

Smaller fixes: the "Speakers" button was clipped in the 300px column (side
padding 13 → 11, button padding 8 → 6, twelve pixels of slack, and the header
row wraps if it needs to). The Share / Home language switch in the "I speak"
sheet stretched across the full line inside a vertical box, leaving 272 pixels
of frame around 146 pixels of content.

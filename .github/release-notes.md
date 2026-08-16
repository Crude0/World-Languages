<!-- title: The country card in full screen -->
**Clicking a country in full screen appeared to do nothing.** The country card
lives below the map on the page, and full screen put it outside the viewport.
The country really was being selected — its border highlighted — but the card
was off-screen, so the click looked like it had been swallowed.

The card now opens beside the map, in the panel column: frosted glass, a single
column, scrolling inside itself when it is long. The minority-language list
moves the same way. Leaving full screen puts both back where they were on the
page, in their original order — three enter/leave cycles leave the DOM
unchanged.

A closed minority list showed up as an empty glass box: a `display` rule was
overriding the `[hidden]` attribute, the same mistake that had happened with the
scale strip.

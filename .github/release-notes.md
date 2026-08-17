<!-- title: The phone, rebuilt from scratch -->
**The phone interface was rebuilt from the ground up.** The layout dated from
the 0.2 era and every release since had piled onto it: layer, colour, detail
level, theme, export and interface language all lived stacked inside a single
floating card, opened by a `◧` button that told you nothing about what it did.
Nothing was where you would look for it.

In its place, a **bottom tab bar** — a tab bar on iOS, a navigation bar on
Android. Both follow the same rule: *a tab is a destination, not a mode.* Four
destinations, each one tap away, always in the same place:

- **Map** — the question the map answers sits in the sheet's header (Home ·
  Script · Official), the colour key in its body. That key never appeared on
  the home layer before, because the floating card had no room for it.
- **Languages** — search and the index of 270 languages. Tapping one filters
  the map and returns you to Map.
- **I speak** — its own destination now. Three large figures (how many
  languages, how many people you reach, in how many countries), the languages
  you picked, and the list to pick from. A badge on the tab shows how many you
  have selected.
- **Settings** — colour by, detail level, theme, export, interface language.

Each tab remembers its own sheet height: low on Map so you can see the map,
fully open in the language index. The top bar retracts when the sheet is fully
open. The tab bar is opaque — the sheet's body slides down behind it, and
through the glass the list rows stayed legible enough to collide with the tab
labels.

**PNG and SVG export wrote no file anywhere.** The page said "Saved" and
nothing appeared in Downloads or in the gallery. The cause: `<a download>` only
works in a browser — neither Android WebView, nor WKWebView, nor WebView2 has
a download handler, so the click was swallowed silently. All three shells now
have a save bridge (Android `JavascriptInterface` + MediaStore, macOS
`WKScriptMessageHandler`, Windows WebView2 `Bind`), files land in Downloads,
and the button text finally reports what actually happened. No new Android
permission is requested.

**Choosing the "I speak" layer in fullscreen was a dead end.** Languages could
only be picked from the index in the left panel, and fullscreen has no left
panel — you had to press Escape, pick your languages, and go back in. The
desktop now has a **"My languages"** sheet that opens over the map: reading
mode, the three figures, your chosen languages, and a language list with its
own search field. It opens by itself when you switch to the layer with nothing
picked yet. It is in the same place in both modes, because it lives inside the
map.

**The total-people-you-could-talk-to figure went stale.** It was in the
subtitle, but only rewritten when the filter changed — adding or removing a
language never refreshed it, so it still read "Pick the languages you speak"
with six languages selected.

**In Sweden, 95% next to 85% read as a contradiction.** The two numbers measure
different things: the figure at the top of the card counts first- and
second-language speakers together, while the list below it counts the language
spoken at home. Twenty countries differ, the largest being Indonesia (94% /
20% — almost everyone speaks Indonesian, one in five speaks it at home). The
card now writes a line reconciling the two wherever they diverge.

Two data fixes alongside it:

- Aliases in the distribution tables now reach `data.json` under their
  canonical name. The row "Filipince (Tagalog)" did not match the language
  record's own name, "Filipince": for a Filipino speaker, the Philippines and
  the Northern Mariana Islands counted as zero. All 234 countries now have
  their majority language present in their distribution.
- In Croatia the share who speak the language (95%) was below the share who
  speak it at home (96%) — impossible by definition. Fixed, with a build check
  that will not let it through again.

**The hover tooltip was drawn under the HUD bar.** With the cursor over a
country beneath the "View · Table · Share" bar, the tooltip text ended up
behind it; the stacking order is fixed.

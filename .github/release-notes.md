### 0.94 billion people's languages were invisible

A gap noted at the end of 0.7.0 turned out to be far larger than expected. The
distribution tables carry language names as text, and a name with no entry in the
language table is dropped along with its row: **186 languages** were being
discarded that way, and the rows added up to **0.94 billion people**. The largest
were Javanese (90 million), Wu Chinese (85), Bhojpuri (74), Yoruba (48), Lingala
(44), Oromo (44), Sundanese (42) and Sindhi (40).

There were two separate problems. Some languages had never been registered; others
were **the same language under two spellings**, written differently as the tables
grew over the years — "Vu Çincesi" beside "Wu Çincesi", "Yoruba" beside
"Yorubaca", Taiwanese Hokkien beside Min Chinese, Fulfulde and Pulaar beside Fula.
An alias table now maps those together.

Every language with more than two million speakers — 63 of them — has been
registered. Of the 0.94 billion, **0.057 billion** remains unmatched (89 small
languages, the largest at 2 million). The language count goes from **219 to 270**,
and the population counted under a named first language from 7.19 to **7.98
billion**.

### Compare two places

**Compare with …** on a country card pins a place; pick a second and the card
splits into two columns with both distributions side by side. Underneath,
**spoken in both** lists the languages they share, each at the smaller of the two
shares — a floor on how many people that language reaches in both places. Turkey
against Germany comes out as Turkish 2%, Kurdish 1.2%, Arabic 1.2%. Regions work
as well as countries: Tatarstan against Chuvashia, Québec against Ontario.

### The world in the languages you speak

A fourth layer, **I speak**. Tick the languages you know and the map colours every
country by the share of its population that speaks at least one of them, as a
first or second language. Turkish plus English reaches roughly 1.81 billion
people. The choice is stored in the browser and travels in the link
(`#k=know&kn=tr.en`), so a view can be shared.

The layer reads two ways. **Share** works as above. **Home language** instead
lights only the countries where one of your languages is the *majority language
spoken at home* — each in the colour of its own family, the rest dimmed. Turkish
plus English gives 38 countries and about 538 million people. "Where could I get
by" and "where is my language the language" are different questions, so they get
different modes.

In share mode the shares are added and capped at 100%: someone who speaks two of
your languages is counted twice, so the figure is an upper bound — and the panel
says so.

### Download the view as PNG or SVG

Two new buttons put the current view — zoom, layer, filter, selection — into a
single file. The SVG stands on its own: only the rules that concern the map are
copied out of the page's stylesheet, the colours in use are resolved into it, and
culled paths are never written. The filename is derived from what is on screen
(`dunya-dilleri-off-french.svg`). Both are in the layer menu on the phone.

### The macOS menu bar

The app's menu bar showed **"osascript"** as the application name, and there was
no About, no File and no View menu. The reason: the title of the application menu
comes from the running process's bundle name rather than from the menu item, and
the window is opened inside osascript. The bundle name is now rewritten at startup.

The menu is also complete: **About** with the version number, Hide / Hide Others /
Show All, **File** (copy link, close window), **Edit** (undo, cut, copy, paste,
select all), **View** (zoom in, zoom out, fit, toggle table, full screen) and
**Window**. The View items drive the page's own controls, so the menu and the
toolbar do the same thing. Quit uses its own selector now: with `terminate:` macOS
rewrote the title to "Quit and Keep Windows", in English, because the running
bundle carries osascript's localisations.

Since this could not be tried on a Mac while it was written, the script gained an
audit mode that builds the menu and prints it, and the release workflow **runs
that on the macOS runner** and checks that the bundle name and all five menus are
in place. If the check fails, the release does not go out.

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 669 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | ~9 MB |
| macOS, no disk image | `Dunya-Dilleri-Atlasi-mac.zip` | 3.5 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.9 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

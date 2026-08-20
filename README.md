**English** · [Türkçe](README.tr.md)

# World Language Atlas

An interactive map of the language spoken by the majority in each of 234
countries and territories, filterable by language. It works entirely offline:
one self-contained web page, a desktop app (macOS · Windows) and an Android app.
No network requests, no permissions.

<p>
  <a href="https://crude0.github.io/World-Languages/"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/img/btn-open-en-dark.svg">
    <img height="46" alt="Open in your browser" src="docs/img/btn-open-en-light.svg">
  </picture></a>
  <a href="https://crude0.github.io/World-Languages/mobile.html"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/img/btn-phone-en-dark.svg">
    <img height="46" alt="Phone version" src="docs/img/btn-phone-en-light.svg">
  </picture></a>
  <a href="#downloads"><picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/img/btn-dl-en-dark.svg">
    <img height="46" alt="Downloads" src="docs/img/btn-dl-en-light.svg">
  </picture></a>
</p>

![World map](docs/img/desktop-world.png)

Turkish and English interface; light, dark, or follow the system.

| | | | |
|---|---|---|---|
| **234** countries and territories | **270** languages, **121** a majority somewhere | **1,128** country × language rows | **507** states, provinces and cantons |
| **32** writing systems | **8.09 billion** people covered | **7.97 billion** under a named first language | **18** countries mapped at region level |

---

## What it does

<table>
<tr>
<td colspan="2"><img alt="The atlas asks two questions" src="docs/img/desktop-questions.png"></td>
</tr>
<tr>
<td colspan="2"><b>The atlas asks two questions</b>, and the whole page follows
whichever one you pick. "What does the world speak?" is the map of everyone
else; "Who could you talk to?" is the map of you. The question mark opens a
short walkthrough.</td>
</tr>
<tr>
<td width="50%"><img alt="Turkish diaspora" src="docs/img/desktop-diaspora.png"></td>
<td width="50%"><img alt="Density map" src="docs/img/desktop-density.png"></td>
</tr>
<tr>
<td><b>Pick a language, see where it lives.</b> Countries where it is the
majority turn solid, where it is a minority they are tinted. The tail reaches
down to 0.05%, so Turkish in Belgium (1.3%) and Ukrainian in Germany (1.4%)
are on the map. Turkish appears in 26 countries.</td>
<td><b>Or colour by density.</b> Share of the population, or head count.
Speaker counts are population × language share, with native and
second-language speakers kept apart.</td>
</tr>
<tr>
<td><img alt="Writing systems" src="docs/img/desktop-scripts.png"></td>
<td><img alt="Official languages" src="docs/img/desktop-official.png"></td>
</tr>
<tr>
<td><b>Script layer.</b> Turkish, Vietnamese and Indonesian are unrelated yet
all write in Latin; Serbian and Croatian are mutually intelligible and write in
Cyrillic and Latin. The script is derived from each language's own name for
itself, counted by Unicode block.</td>
<td><b>Official-language layer.</b> Half of Africa changes colour: the state's
language is not the home language. English is official in 51 countries but
spoken at home in 36. The <b>23 countries</b> whose home language is on no
official list are cross-hatched.</td>
</tr>
<tr>
<td><img alt="Region level" src="docs/img/desktop-regions.png"></td>
<td><img alt="Russia's federal subjects" src="docs/img/desktop-russia.png"></td>
</tr>
<tr>
<td><b>Zoom in and countries become regions.</b> French is 78% in Québec and
1.1% in British Columbia; Kurdish 82% in south-eastern Türkiye and 3% in the
west — differences a national average hides.</td>
<td><b>Russia's 83 federal subjects</b> are the largest of them. Tatarstan
reads Tatar, Chuvashia Chuvash, Sakha Yakut; Chechnya, Ingushetia and Dagestan
stand apart in their own Caucasian languages.</td>
</tr>
<tr>
<td><img alt="The world in the languages you speak" src="docs/img/desktop-know.png"></td>
<td><img alt="Language card" src="docs/img/desktop-card.png"></td>
</tr>
<tr>
<td><b>"Who could you talk to?"</b> Tick the languages you know and every
country is shaded by the share of its population you could hold a conversation
with. Turkish plus English is about 1.81 billion people. The choice travels in
the link.</td>
<td><b>Click a language and its card opens.</b> Family and script, native and
second-language speakers, where it is the majority, and everywhere it is spoken
as a minority.</td>
</tr>
<tr>
<td><img alt="Full-screen map" src="docs/img/desktop-fullscreen.png"></td>
<td><img alt="The walkthrough" src="docs/img/desktop-tour.png"></td>
</tr>
<tr>
<td><b>Full screen</b> hands the whole viewport to the map; the legend moves
into a bar along the bottom. Compare two places side by side, and export the
current view as <b>PNG or SVG</b>.</td>
<td><b>A short walkthrough</b> dims the page and lights one thing at a time.
It is behind the question mark next to the second question, and it comes round
once after every update.</td>
</tr>
</table>

### Phone version

The Android app is not the desktop page shrunk down; it is a separate interface
written for the phone: full-screen map, floating glass layers above it, a
three-detent bottom sheet, touch gestures and the system typeface.

<p>
  <img src="docs/img/mobile-home.png" width="220" alt="Home screen">
  <img src="docs/img/mobile-detail.png" width="220" alt="Country card">
  <img src="docs/img/mobile-know.png" width="220" alt="I speak">
  <img src="docs/img/mobile-settings.png" width="220" alt="Settings">
</p>

---

## Downloads

The current build is on the
**[Releases page](https://github.com/Crude0/World-Languages/releases/latest)**;
what changed is in [CHANGELOG.md](CHANGELOG.md).

| Platform | File | Size | Note |
|---|---|---|---|
| Android 7+ | [`Dunya-Dilleri-Atlasi.apk`](dist/Dunya-Dilleri-Atlasi.apk) | 690 KB | No internet permission |
| macOS 10.15+ | [`Dunya-Dilleri-Atlasi.dmg`](dist/Dunya-Dilleri-Atlasi.dmg) | 9.3 MB | Universal (Intel + Apple Silicon) |
| macOS, no disk image | [`Dunya-Dilleri-Atlasi-mac.zip`](dist/Dunya-Dilleri-Atlasi-mac.zip) | 3.5 MB | Unzip and drag the app across |
| Windows 10+ | [`Dunya Dilleri Atlasi.exe`](dist/Dunya%20Dilleri%20Atlasi.exe) | 5.0 MB | Single file, no installer |
| Browser | [`docs/index.html`](docs/index.html) | 1.9 MB | One file, just open it |

The browser version is **installable** — "Install" in Chrome, "Add to Home
Screen" in Safari — and then runs offline like an app. Any view you build has
its own link: press **Link** and share it.

<details>
<summary>The apps are unsigned — how to open them anyway</summary>

There is no Apple or Microsoft developer certificate behind these builds:

- **macOS**: on first launch right-click the app → **Open** → **Open** again in
  the dialog. Or: `xattr -dr com.apple.quarantine "/Applications/Dunya Dilleri Atlasi.app"`
- **Windows**: on the SmartScreen warning pick **More info** → **Run anyway**.
- **Android**: you need to allow installation from unknown sources.

The desktop apps use the operating system's own browser engine (WKWebView on
macOS, WebView2 on Windows) — they open in their own window, no browser needed.
If the engine is missing there is a fallback that opens an installed browser in
app mode, without an address bar.
</details>

---

## Data

Where the numbers come from, how they are computed and where they are weak is
written out in **[DATA.md](DATA.en.md)**. Borders are
[Natural Earth](https://www.naturalearthdata.com/) (public domain), population
is the UN Population Division's 2024 estimates, and language shares are
compiled from national censuses, Ethnologue and official language policy.

These are approximations and need care in cross-country comparison: one census
asks for "mother tongue", another for "language spoken at home". Türkiye has no
official language census, so its provincial figures are survey-based estimates.
**There is no city-level data** — most countries do not publish language
statistics per municipality, and inventing it was not an option.

<details>
<summary>Build</summary>

Requirements: Python 3.9+, Node 18+ (verification only), Go 1.21+ (desktop),
Android SDK build-tools 34 + JDK 17+ (Android).

```bash
make            # data + web page (single file, opens in a browser)
make desktop    # macOS .dmg + .app, Windows .exe
make android    # signed APK
make check      # interface checks with Playwright
```

Pipeline:

```
countries-50m.json ──► build_map.py  ──► map_paths.json  ┐
ne_10m_admin_1…    ──► build_subs.py ──► sub_paths.json  ├─► build_data.py ──► data.json
lang_mix / diaspora / population / subdiv ───────────────┘                        │
                                                    page.tmpl.html   ◄────────────┤
                                                    mobile.tmpl.html ◄────────────┘
```

On its first run `src/build_subs.py` downloads Natural Earth's 40 MB subdivision
file (not kept in the repository).

```
src/                every build script, data table and template
  build_map.py      country borders → projected SVG paths
  build_subs.py     state/province borders; topology-preserving simplification
  build_data.py     joins every layer, computes speaker counts
  build_page.py     desktop page (single file, fonts embedded)
  build_mobile.py   phone interface (system fonts)
  pwa.py            manifest, service worker and icon wiring for docs/
  anchor.py         label anchors (pole of inaccessibility)
  page.tmpl.html    desktop interface
  mobile.tmpl.html  phone interface
  layers.py         writing systems and official languages
  lang_mix.py       language distribution per country
  diaspora.py       migrant and minority communities (down to 0.05%)
  population.py     country populations
  subdiv.py         state/province distributions and populations
  i18n.py           English language names, family labels, country notes
VERSION             single source for the version in every package
desktop/            Go launcher + packaging (WKWebView / WebView2)
android/            WebView shell + APK build script
tools/              Playwright checks, README screenshots and buttons
```

`node tools/shots.mjs` regenerates every screenshot in this file, and
`python3 tools/make_buttons.py` the buttons above it.
</details>

<details>
<summary>Technical notes</summary>

- **Projection** is Natural Earth (Šavrič's polynomial), implemented by hand in
  Python; the map is embedded as plain SVG paths with no runtime dependency.
- **Topology-preserving simplification**: simplifying neighbouring provinces one
  by one picked different points along the shared border and left hairline gaps
  between them. Using TopoJSON's rule — a point starts an arc when its pair of
  neighbours changes — rings are split into arcs and each shared arc is
  simplified exactly once.
- **Label anchors** are the pole of inaccessibility of the largest ring, not a
  centroid. A vertex mean lands offshore on concave coasts: Norway's label ended
  up in the sea, Croatia's on top of Bosnia. 228 of 234 anchors are now strictly
  inside their country; the six that are not are pixel-sized (Vatican, Monaco,
  Macao…) and are drawn as pins anyway.
- **The palette is computed, not chosen.** Simulated annealing over OKLCH with a
  colour-blindness model (Machado 2009), checked so that *every pair* of the
  nine legend colours stays apart, not just neighbours. Worst pair: ΔE 9.1 in
  light mode, 9.0 in dark. Ten colours could not clear it in dark mode's narrow
  lightness band — which is why creoles carry a diagonal hatch over their
  lexifier's colour instead of a hue of their own.
- **The stutter while panning was strokes, not fills.** It was chased by guesswork
  for a long time; in the end Chrome's own trace records were used to measure
  rasterisation time. 70–80% of it goes into stroking: fills, hatch patterns and
  ornaments cost nothing measurable. Three things followed — country outlines are
  drawn from a coarser geometry when zoomed out (computed in the browser at
  startup, so it adds no bytes to the file), antialiasing is switched off while
  a gesture is in progress, and in region mode the same line is no longer stroked
  several times over. Rasterisation halved in the world view.
- **The 180th meridian**: Russia's and Fiji's rings are cut at the edge and split
  into separate pieces, otherwise a horizontal band is drawn across the map.
- **The ISO 9660 trap on macOS**: files with Turkish characters inside the DMG
  could not be opened (the cd9660 driver does not normalise Unicode). File names
  are ASCII on disk, with the visible name supplied by a localized
  `InfoPlist.strings`.
- **DPI on Windows**: an application that does not declare itself DPI-aware is
  drawn at 1080p and stretched on a 2K/4K display, which looks blurry.
</details>

---

The code is [MIT](LICENSE). Map borders come from Natural Earth and are public
domain. Language and population data are compiled from public sources; the list
is in [DATA.en.md](DATA.en.md).

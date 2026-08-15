**Two new map layers.** Until now the map answered one question: which language
is spoken at home here? The **Layer** control in the toolbar now asks the same
countries two more.

### Script

Which alphabet is the language written in? It says something the family map does
not: Turkish, Vietnamese and Indonesian are unrelated yet all write in Latin,
while Serbian and Croatian are close enough to be mutually intelligible and are
written in Cyrillic and Latin respectively. Nine legend entries — Latin (175
countries), Arabic (25), Cyrillic (10), East Asia (7), Southeast Asian Brahmic
(5), other alphabets (5), South Asian Brahmic (4), Ge'ez (2), other (1).

The script data is not typed in by hand. The letters of each language's own name
for itself are counted by Unicode block, which covers all 155 languages on its
own and leaves no table to maintain; only six exceptions are written out. The
**13 languages written in two scripts** are marked separately — Serbian,
Punjabi, Kazakh, Kurdish, Uzbek, Mongolian and others — with the second script
and the reason for it on the country card.

### Official language

Is the language of the state the language of the home? Across half of Africa it
is not. Switching the layer transforms the continent: west and central Africa
turn the red of French, the south and east the blue of English. English is
official in **51** countries but the home language of only 36; French is
official in 18 and spoken at home in 13.

The **23 countries whose home language is not on the official list at all** are
cross-hatched on the map: Nigeria (Pidgin at home, English in law), Senegal
(Wolof / French), Sierra Leone (Krio / English), South Sudan (Juba Arabic /
English), Mauritius, Jamaica, the Solomon Islands and others. New Zealand runs
the other way: English was never declared official, and the languages official
in law are Māori (1987) and New Zealand Sign Language (2006).

The table covers all 234 countries and is ordered by **legal precedence**, not
by everyday use — Ireland's constitution names Irish the first official language
while daily life runs in English, and both are listed in that order. The 16
countries that have declared no official language in law are marked as such, and
48 countries carry a note explaining what the layer is showing.

### 142 languages became 155

Thirteen languages that appear only as official languages were added to the
table: Pashto, Afrikaans, Belarusian, Irish, Māori, Tamazight, Fiji Hindi,
Chamorro, Xhosa, Ndebele, Romansh, Hiri Motu and Latin. Most of them were
already rows in `lang_mix.py` but had no entry in the language table, so they
were being dropped silently — their speaker counts are now computed as well.
Pashto alone accounts for roughly 90 million people.

### Elsewhere

The layer is part of the link (`#k=scr`, `#k=off`), so a shared view opens on
the layer it was shared from. The writing system and official-language rows show
on the country card in every layer, and tapping an official-language badge
filters to the countries where that language is official. On the phone the layer
menu carries the colour key with it.

The home layer renders **pixel for pixel** identical to 0.5.3; the new layers
reuse the existing palette, so no second colour search was needed.

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 513 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | ~8 MB |
| macOS, no disk image | `Dunya-Dilleri-Atlasi-mac.zip` | 3.2 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.4 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

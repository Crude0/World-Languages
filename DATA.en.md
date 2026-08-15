**English** · [Türkçe](DATA.md)

# Data: sources, method and limits

This document says where every number on the map comes from, how it is computed
and where it is weak. All of the figures are **approximate**; read them as orders
of magnitude, not to the decimal.

## Layers

| Layer | File | Coverage | What it says |
|---|---|---|---|
| Majority language | `C` in `build_data.py` | 234/234 | The language the largest part of the population uses in daily life |
| Home languages | `lang_mix.py` (`MIX`) | 234/234 | Distribution of native-language shares |
| Migrant/minority tail | `diaspora.py` | 56 countries, 440 rows | Communities below 1%, down to 0.05% |
| Second language | `lang_mix.py` (`L2`) | 189/234 | Languages spoken well enough to hold a conversation without being native |
| Population | `population.py` | 234/234 | UN 2024 estimate, thousands |
| State / province | `subdiv.py` | 313 regions, 12 countries | Language distribution and population per region |
| Writing system | `layers.py` (`SCRIPT_FIX`, `SCRIPT2`) | 155/155 languages | Which alphabet the language is written in; the second one where two are in use |
| Official language | `layers.py` (`OFFICIAL`, `DE_FACTO`) | 234/234 | The state's official languages in law; the de facto one where none is declared |

## Sources

**Borders** — [Natural Earth](https://www.naturalearthdata.com/): 1:50m for
countries, 1:10m for subdivisions. Public domain. The borders do not express any
claim of sovereignty; Kosovo, Northern Cyprus and Somaliland are shown separately
because their language distributions differ from their surroundings.

**Population** — UN Population Division, *World Population Prospects 2024*.
National statistical offices for dependent territories.

**Language shares** — compiled and rounded from the language questions of
national censuses (Canada, US ACS, the Swiss structural survey, India 2011,
Australia, New Zealand, Ukraine 2001, Bolivia 2012 and others), Ethnologue and
official language policy.

**Second language** — Eurobarometer 386 (2012) in Europe, on the "able to hold a
conversation" criterion. National censuses and estimates elsewhere.

**The writing system is not typed in by hand**: the letters of each language's
own name for itself (its endonym) are counted by Unicode block, and the most
frequent block is taken as the script. That covers all 155 languages on its own
and leaves no table to maintain. Only six exceptions are written out
(`SCRIPT_FIX`): the Japanese endonym looks like pure kanji but the script is
kanji + hiragana + katakana; Konkani's official script in Goa is Devanagari;
Chinese and Cantonese arrive from the "CJK" block; and the Unicode block names
for Meetei and Inuktitut do not translate directly into script names.

**Languages written in two scripts** (`SCRIPT2`) are a separate table of 13.
Serbian's official script is Cyrillic but Latin is used everywhere too; Punjabi
is written in Gurmukhi in India and Shahmukhi in Pakistan; Kazakh is moving to
Latin between 2023 and 2031. The map colours by the primary script, and the
second one appears on the country card.

**Official languages** are compiled from constitutions and language acts, and
ordered by **legal precedence**, not by everyday use. Ireland's constitution
names Irish the first official language while daily life runs in English — both
are listed, in the constitution's order. The 16 countries that have declared no
official language in law are held in the `DE_FACTO` table with the language the
state actually uses, and are marked "no official language in law" on the card.
(The United States is not among them: an executive order made English official
in 2025.)

## Calculations

**Speaker count** = population of the country (or region) × the share of that
language, summed over all countries. So "Spanish 503 million" means the sum, over
every country, of its population times the Spanish native-language share.

**A language's total** keeps native and second-language speakers apart. For
English, native ≈ 418 million and second language ≈ 1.36 billion; the "Total"
ranking adds the two (≈ 1.8 billion).

**Percentages can exceed 100%.** In multilingual countries many people speak more
than one language at home, and sources like the Swiss structural survey allow
multiple answers.

## Known limits

**The criteria differ from country to country.** One census asks "what is your
mother tongue", another "which language do you speak at home". These are not the
same thing and the figures shift accordingly. Keep it in mind when comparing
across countries.

**Ancestry ≠ language.** Diaspora figures count the people who *speak the
language at home*, not everyone of that descent. Belgium has a population of
Turkish descent of about 220,000 but roughly 150,000 speak Turkish at home; the
difference is language loss in the second and third generation.

**Türkiye's provincial figures are estimates.** There is no official language
census in Türkiye; the provincial shares for Kurdish, Zaza and Arabic are
approximations derived from survey-based studies (of the KONDA kind).

**Diaspora coverage is uneven.** The migrant-community tail has been filled in
for the 56 main destination countries; not every small community in every country
is listed. If one you know is missing it can be added to `diaspora.py`.

**No city-level data.** Language statistics per municipality are not published in
most countries. Sweden, for example, publishes *country of birth* per
municipality, not language spoken — a different measure, and presenting it as
language data would be misleading. The finest level of detail therefore stops at
province / state / canton.

**War and migration age quickly.** Ukrainian migration after 2022 is reflected in
the figures for Poland, Czechia, Germany and the Baltic states; those numbers are
more volatile than the rest.

**The line between "language" and "dialect" is contested.** Arabic is collapsed
into one row even though Moroccan and Iraqi speech are not mutually intelligible.
Chinese is split into Mandarin and Cantonese but Wu and Min sit on their own
rows. Serbo-Croatian is counted as one language in some countries and separately
in others. These are classification choices, not data errors.

**Language families are grouped for colour.** The map has eight family colours
plus "other", because more than that cannot be told apart reliably (see the
palette note in the README). "East and South Asian languages" is therefore a
*geographic* grouping — Sino-Tibetan, Japonic, Koreanic, Dravidian, Austroasiatic
and Tai-Kadai are separate families and the label does not claim otherwise. The
exact family of every language is shown in its own row and tooltip.

## Contributing

If you think a number is wrong, open an issue with the source. The data files are
plain Python dictionaries and are easy to edit:

- `lang_mix.py` — native and second-language distribution per country
- `diaspora.py` — small communities
- `population.py` — populations
- `subdiv.py` — state/province distributions
- `L` and `C` in `build_data.py` — the language list and the majority language
  per country

After a change, `make` is enough; `build_data.py` stops with an error if it finds
an undefined country or language.

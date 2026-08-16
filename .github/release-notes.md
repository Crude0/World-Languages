**Regional data goes from 12 countries to 18, and from 313 regions to 507.** The
largest blank patches on the map are filled in.

### Russia · 83 federal subjects

More than 30 languages are official at republic level across the federation, and
until now the map drew the whole country in a single colour. Tatarstan now reads
Tatar, Chuvashia Chuvash, Sakha Yakut and Tuva Tuvan in the Turkic colour, while
Chechnya, Ingushetia, Dagestan and Kabardino-Balkaria stand apart in their own
Caucasian languages. The source is the 2021 census. Thirty-two languages arrive
with it: Tatar, Bashkir, Chuvash, Yakut, Tuvan, Chechen, Avar, Lezgian, Ossetian,
Mari, Udmurt, Buryat, Kalmyk, Chukchi and the rest.

### China · 31 provinces

"Chinese" is not one language: Mandarin, Cantonese, Wu, Min, Hakka, Xiang and Gan
are not mutually intelligible, and the map separates them for the first time.
Shanghai and Zhejiang read Wu, Fujian and Hainan Min, Jiangxi Gan, Hunan Xiang,
Guangdong Cantonese — alongside Uyghur in Xinjiang, Tibetan in Tibet, Mongolian
in Inner Mongolia and Zhuang in Guangxi.

### Nigeria, South Africa, France, Germany

**Nigeria's 37 states** show what a national average cannot: the country has no
majority language, and the real pattern is Hausa in the north, Yoruba in the
south-west, Igbo in the south-east and a Nigerian Pidgin belt across the Niger
Delta. **South Africa's 9 provinces** come from Census 2022, where none of the 12
official languages is a national majority. **France** adds Corsican, Breton and
Occitan plus the overseas creoles, and **Germany's 16 Länder** come from the 2022
census — the first to ask which language a household actually speaks.

Brazil is deliberately left out: Portuguese is around 98% in all 27 states, so
its geometry would buy a single flat colour. Crimea, Sevastopol and the Paracel
Islands are left out too — Natural Earth attaches them to Russia and China, and
this repository takes no position on borders, so switching to region level never
changes which country a place is counted as part of.

**The language count goes from 155 to 219**, 64 of them new, and family labels
from 44 to 54: Northeast Caucasian, Northwest Caucasian, Tungusic,
Chukotko-Kamchatkan, Hmong-Mien, Nilo-Saharan and four new branches of
Niger-Congo.

### The stutter did not come back — the map got faster

The geometry grew by 83% (21,628 → 39,683 points). Added without measuring, that
would have doubled the cost of region mode; the first measurement showed 1956 →
3772 ms when zoomed into Russia. Measuring layer by layer turned up two causes.

**`stroke-linejoin: round`** on the border networks accounted for **29%** of the
cost on its own — round join geometry generated at each of fifteen thousand
vertices, for a difference invisible on a 1.2-pixel line. Removed. (The same run
also tested dropping `vector-effect: non-scaling-stroke`, flagged as a suspect
back in 0.4.0: it made a 6 ms difference, so that lead is closed.)

**Culling was not working on the border networks.** Each country's network was a
single path, so Russia's 153-chain outer perimeter was stroked in full even when
a tenth of it was on screen. The chains are now spread across a coarse grid (40
SVG units per cell, 260 buckets in total) and off-screen buckets are dropped —
which helps Canada's 5957-point perimeter as much as the new countries.

Together, despite 83% more geometry:

| case | 0.6.1 | 0.7.0 |
|---|---|---|
| world · country mode | 878 ms | 647 ms |
| world · region mode forced | 1951 ms | **1506 ms** |
| zoomed into Russia · region forced | 1845 ms | **1503 ms** |
| zoomed into Russia · default mode | 1608 ms | **1241 ms** |
| around Moscow · default mode | 1455 ms | **967 ms** |
| China · default mode | 1153 ms | 1082 ms |

So the map draws Russia's 83 subjects and China's 31 provinces and is still
faster than 0.6.1, which drew neither. The page grew from 1442 KB to 1931 KB
(585 → 735 KB compressed).

### Downloads

| Platform | File | Size |
|---|---|---|
| Android 7+ | `Dunya-Dilleri-Atlasi.apk` | 665 KB |
| macOS 10.15+ | `Dunya-Dilleri-Atlasi.dmg` | ~9 MB |
| macOS, no disk image | `Dunya-Dilleri-Atlasi-mac.zip` | 3.5 MB |
| Windows 10+ | `Dunya Dilleri Atlasi.exe` | 4.9 MB |

The apps are unsigned: on macOS right-click → **Open**, on Windows pick
**More info** → **Run anyway**, on Android allow unknown sources.

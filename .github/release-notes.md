<!-- title: The question had the wrong model behind it -->
**"Who could you talk to?" was being answered by checking whether the name of
the language matched exactly.** Pick Turkish and Azerbaijan showed 0%. Nothing
was missing from Azerbaijan's data — 92% of the population speaks Azerbaijani
and it is recorded — the model simply treated the two languages as complete
strangers. The same fault ran through a dozen other pairs. There is now a
mutual-intelligibility network: 42 languages, 90 directed links. For a Turkish
speaker Azerbaijan is 69%, Turkmenistan 44.6%, Kyrgyzstan 23%, Kazakhstan 19.9%,
Uzbekistan 21.2%. Hindi → Pakistan 62%, Czech → Slovakia 100%, Danish → Norway
81% and Sweden 51%.

The factors are directed, because intelligibility is not symmetric: a Portuguese
speaker understands Spanish (60%) better than a Spanish speaker understands
Portuguese (45%). The card marks the chip "≈75%" and explains it on hover —
without that, there is no way to tell where the 69% came from.

**Data auditing is now a permanent tool:** `tools/audit-data.py`. Instead of
chasing one example at a time it sweeps the whole dataset in nine classes. What
the first run found: 377 million people were assigned to no language at all, 45
countries with more than 20 million people had five or fewer languages on
record, and Egypt had exactly one.

**33 languages were registered and four countries were rewritten from their
sources.** Indonesia from the BPS 2010 census table of everyday home language
(Malay, Madurese, Minangkabau, Banjar, Balinese, Buginese, Betawi, Acehnese,
Sasak, Batak and Makassarese join Javanese, Indonesian and Sundanese): 70% →
87.7%. The Philippines from the PSA 2020 census (Bikol, Waray, Kapampangan,
Pangasinan, Maguindanao, Maranao, Tausug): 64% → 90.6% — the census counts
Bisaya/Binisaya and Cebuano separately, and they were merged as one cluster.
Ethiopia from the 2007 census (Sidamo, Wolaytta, Gurage, Afar, Hadiyya, Gamo):
75% → 89.2%. Iran gained Gilaki, Mazanderani, Balochi, Qashqai and Arabic.
China's variety groups were separated out (Jin, Xiang, Gan, Hakka) and the main
minority languages added (Zhuang, Uyghur, Miao, Yi, Tibetan, Mongolian, Korean).

Unassigned population fell from **377 million to 194 million**.

**Turkish in Germany is 2.5%, not 2%.** The 2023 Mikrozensus reports that 2.5%
of the population predominantly speaks Turkish at home. A distinction worth
stating, since it is easy to conflate: the Turkish-origin population of Germany
is about 2.9 million, but the map counts the language spoken at home, not
ancestry — most of the third generation speaks German at home. The audit now has
a section of its own for that class.

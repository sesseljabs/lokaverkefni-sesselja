# lokaverkefni-sesselja, planið

Hugsusnin var að gera conway's game of life með einhverskonar node grid (ég veit ekki alveg hvað það myndi kallast.)

Þá var semsagt plan að gera nodes sem benda á node fyrir ofan, neðan, hægra megin og vinstra megin. Þá geymir nodeið hvort hún sé lifandi eða dauð, og notar pointerana til að skoða nodein í kringum hana.

[wikipedia grein um game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

[sýnidæmi á netinu](https://playgameoflife.com/)

# Verkefnið

Þetta verkefni gekk bara vel, ég gerði það þannig að það sé hægt að setja txt file inn í forritið sem svo breytir því í Grid. 
Það er líka hægt að gera þetta með lista. Maður býr til Grid object, tekur fram hæð og breidd (þarf að vera sama og í txt skránni), setur inn í gridið með skránni og keyrir gridrun() á Gridið.

# Aðgerðir:
- copylist(listi): setur inn í grid út frá lista
- listfromfile(skráarnafn): setur inn í grid út frá txt skrá
- frame(): gerir eina aðgerð sem reiknar út hvaða node lifa og deyja
- printgrid(): prentar allt gridið
- gridrun(): keyrir allt forritið, keyrir að eilífu nema int sé sett inn sem segir hversu margar kynslóðir á að gera

Nú er ég ekki viss um flækjutíma, en hlutir eins og frame() er kannski O(n*m), ef n er hæð og m er breidd. Ég hef samt eiginlega enga hugmynd.
Þetta er mikið af nested lykkjum.

# Mikilvægt

Skráin sem er notuð er main.py, en hinar innihalda klasa

Til að keyra forritið þarf að keyra skrána beint, ekki eins og inní pycharm vegna þess að forritið notar os til að hreinsa skjáinn, ef það virkar ekki þá veit ég ekki hvað er hægt að gera.

grid.txt er það sem forritið er að nota núna, það inniheldur byrjun til að gera Gosper's glider gun [(Guns á wikipediu)](https://en.wikipedia.org/wiki/Gun_(cellular_automaton)) sem á að keyra að eilífu


## [myndband af virkni á youtube](https://youtu.be/sXCa4cFo-HI)
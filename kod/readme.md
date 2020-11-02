# Struktur av system
Hemsida (interaktion med användarna) -> Python-server (tar emot användar-data, tolkar data och servrar) <-> SuperCollider (genererar musik)

# Musik
Varje instans av mätdata existerar som ett *objekt* i musiken, objekten har vissa attribut (såsom register, spatiell kodning, etc). Koda gärna binauralt (kanske via *Ambisonics*).

### Harmonicitet (spektralitet)
Varje *objekt* har följande attribut i förhållande till spektralitet:

* Register
* Tonart (bruksskala)
* Stämning (*renstämd/liksvävig*)

### Temporalitet
Varje *objekt* har följande attribut i förhållande till temporalitet:

* Tempo (?)

### Spatialitet
Varje *objekt* har följande attribut i förhållande till spatialitet:

* Position
* Bredd


# TODO
1. Kod för musik (skelettkod till en början)
    1. SuperCollider
    1. Python
1. Text till seminarium 
	1. Skelett för layout av examenstext (**deadline 8/11**)
	1. Litteraturstudie
		1. Låna: *Det omätbaras renässans* av Jonna Bornemark

## Diverse
- [ ] Ska hemsida vara på svenska eller engelska? 
- [ ] Merge med "idé"-textfil 
- [ ] Sätta upp GitHub (pages kanske t.o.m?) 

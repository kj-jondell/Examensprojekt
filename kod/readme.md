(*Dokument uppdaterat:* \today)

# Struktur av system
![Flowchart program](https://user-images.githubusercontent.com/30523857/98031117-550b9880-1e12-11eb-9abd-c8afc5563eac.png)

**Hemsida** (interaktion med användarna) -> **Python**-server (tar emot användar-data, tolkar data och servrar) <-> **SuperCollider** (genererar musik) -> **Webbradio** (dvs. *DarkIce* -> *IceCast*, som strömmar ut musiken) -> **Hemsida** (som spelar upp musiken)

Kommunikation mellan Python-server och SuperCollider-patch sker *antingen* i realtid via OSC **eller** asynkront via CSV-filer. 

# Blodsockervärden
Blodsocker mäts i mmol/L och varierar hos en icke-diabetiker mellan 4 och 6 mmol/L. Hos en diabetiker kan detta värde variera från under 1 till över 30 mmol/L, och Freestyle Libre-sensorn har ett spann på att mäta från lägst 2,2 till 27,7 mmol/L (annars visar den "*LO*" (sic) respektive "*HI*" (sic)). Freestyle Libre-sensorn mäter kontinuerligt var 15:e minut.

Att s.k. *mappa* denna data till musikaliska parametrar är förstås godtyckligt -- värdena i sig har ingen musikalisk mening -- och bör så vara: det är helt enkelt min konstnärliga gärning som bestämmer hur de förhåller sig till varandra. Även en bearbetad signal går att använda för att styra musiken: interpolation (mellan de diskreta mätpunkterna), variation (FFT, derivator, etc.), stokastiska egenskaper (auto-korrelation etc), statistiska egenskaper (median, medel, etc.). "*Tid i målområdet*" och liknande värden kan också vara intressanta att använda, och har medicinsk betydelse.

Det som är viktigt i denna *mappning* är dock att den gestaltade datan -- dvs. musiken -- **inte** får avslöja något om den underliggande eller bakomliggande (mät)datan. Dels är det en integritetsfråga, som diskuteras vidare nedan, dels är det en förutsättning för detta projekt: det existerar inga "*bra*" eller "*dåliga*" värden. Delningen av värdena är det viktiga. Genom delningen sker en kollektiv kreation: *lägereldssången*. 

## Integritet, delning osv.


# Musik (SuperCollider-kod)
Varje instans av mätdata existerar som ett *objekt* i musiken, objekten har vissa attribut (såsom register, spatiell kodning, etc). Koda gärna binauralt (kanske via *Ambisonics*). Klassen har en Osc-tolkarfunktion **eller** CSV-filläsare.

Använd *Diabetessynth* som klangkälla? Kanske även andra Synthar.

### Effektkedja
Använda effekter för bl.a. spatialitet (delay/reverb), förstärkning, mixining och manipulation.

### Klangkällor
Följande beskriver vilka ljudkällor (syntesmetoder) som kan tänkas användas:

* *Diabetessynth* (dvs. granulärsynth/wavetable-synth)
* FM-synth/AM-synth
* Annan granulär/sampler/wavetable-synth

### Harmonicitet (spektralitet)
Varje *objekt* har följande attribut i förhållande till spektralitet:

* Register
* Tonart (bruksskala)
* Stämning (*renstämd/liksvävig*)
* Klangfärg (bestäms av mätdata?)

### Temporalitet
Varje *objekt* har följande attribut i förhållande till temporalitet:

* Tempo 

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
- [ ] Hantera *lo*, *hi*, och mg/dL (ist. för mmol/L).
- [ ] Ska hemsida vara på svenska eller engelska? 
- [ ] Merge med "idé"-textfil
- [ ] Sätta upp GitHub (pages kanske t.o.m?) 
- [ ] Tänk på vilket register som ska motsvaras av vilken typ av ljudkälla...
- [ ] openFrameworks... visualisering av mätdata?

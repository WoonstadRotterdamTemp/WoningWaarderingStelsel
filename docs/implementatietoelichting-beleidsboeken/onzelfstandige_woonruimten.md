# Hoofdstuk 2 - Algemene toelichting

## 2.6 Evenredige verdeling, afronding punten en eindsaldering

**Evenredige verdeling**

In geval van een onzelfstandige woonruimte zijn er vaak ruimtes of voorzieningen waarvan (ook) andere bewoners gebruik maken. Deze ruimtes of voorzieningen worden betrokken in de berekening van het aantal punten voor de onzelfstandige woonruimte in kwestie. De manier waarop is als volgt.  

Punten die moeten worden gedeeld door het aantal onzelfstandige woonruimten worden evenredig over het aantal woonruimten binnen de gehele woning verdeeld, ongeacht de grootte van de afzonderlijke onzelfstandige woonruimten. Als slechts een deel van de onzelfstandige woonruimten op een adres toegang heeft tot bepaalde gemeenschappelijke vertrekken, ruimtes en voorzieningen, worden de punten alleen verdeeld onder die specifieke woonruimten die, volgens de huurovereenkomst, daadwerkelijk toegangs- en gebruiksrecht hebben tot die gedeelde vertrekken, ruimtes of voorzieningen.

> Wij hebben `gedeeld_met_aantal_onzelfstandige_woonruimten` toegevoegd als property van ruimten om te kunnen specificeren moet hoeveel een ruimte gedeeld wordt met andere personen op hetzelfde adres. Indien deze property leeg is of kleiner is dan 2, tellen we de ruimte mee als zijnde niet gedeeld.

**Afronding per rubriek**

De waardering in punten wordt per rubriek na saldering afgerond op 0,25 punt waarbij een achtste (1/8) punt naar boven wordt afgerond. Dat wil zeggen dat 0,125 wordt afgerond naar 0,25. Een kwartpunt is de kleinst werkbare waardering binnen het woningwaarderingsstelsel voor een afzonderlijke rubriek.

**Eindsaldering**

Het puntentotaal per woning wordt na eindsaldering (met inbegrip van de bij zorgwoningen geldende toeslag) afgerond op hele punten. Bij 0,5 punten of meer wordt afgerond naar boven op hele punten, bij minder dan 0,5 punten wordt afgerond naar beneden op hele punten.

```text
NB: Alle punten worden bij elkaar opgeteld inclusief de punten voor de gemeenschappelijke ruimten en voorzieningen waarna wordt afgerond. De toeslag van 35 % bij zorgwoningen wordt toegepast op het puntentotaal van de onderdelen 1 t/m 11 en pas daarna wordt afgerond.
```

**Meer dan 250 punten**

In geval van een woonruimte met méér dan 250 punten wordt de maximale huurprijs als volgt berekend: elk punt boven de 250 wordt vermenigvuldigd met het verschil tussen de bedragen, genoemd in de huurprijstabel (zie bijlage 4) bij 249 en 250 punten. Het verkregen bedrag wordt vervolgens opgeteld bij de maximale huurprijs die volgens de huurprijstabel behoort bij 250 punten.

Voorbeeld

```text
Voorbeeld:  Een zelfstandige woning wordt beoordeeld met 255 punten. Bij een puntenaantal van 250 hoort een maximale huurprijs van € 1.521,50 (prijspeil 1 juli 2024). Het puntenaantal voor de woning ligt echter vijf punten hoger. Dit verschil van vijf punten dient te worden vermenigvuldigd met het verschil tussen de bedragen die correspondeerden met 249 en 250 punten. Dat verschil bedraagt (€ 1.521,50 - € 1516,53 =) € 4,97. De verhoging op de maximale huurprijs is in dit geval € 24,85 (€ 4,97 x 5). De maximale huurprijs bedraagt dus € 1.546,35 (€ 1.521,50 + € 24,85).
```

## 2.7 Prijsopslag monumenten

De punten die worden gehaald op basis van het woningwaarderingsstelsel resulteren in een maximale huurprijs. Op deze maximale huurprijs kan daarnaast sprake zijn van een prijsopslag voor monumenten op grond van artikel 8a van het Besluit huurprijzen woonruimte.

### 2.7.1 Rijksmonument

**Huurovereenkomst afgesloten op of na 1 juli 2024**

Indien een woonruimte bestaat uit of deel uitmaakt van een rijksmonument, als bedoeld in artikel 1.1 Erfgoedwet, dan wordt de maximale huurprijs vermeerderd met 35%. Hiermee worden rijksmonumenten bedoeld die zijn geregistreerd in het monumentenregister van de Rijksdienst voor het Cultureel Erfgoed.

Deze prijsopslag geldt alleen voor huurovereenkomsten die zijn afgesloten op of na het tijdstip van inwerkingtreding van de Wet betaalbare huur, dus vanaf 1 juli 2024. Als de huurovereenkomst is afgesloten vóór 1 juli 2024 dan geldt onderstaande waardering.

De Huurcommissie hanteert passief beleid. De verhuurder moet aantonen dat een woning bestaat of deel uitmaakt van een rijksmonument.

**Huurovereenkomst afgesloten vóór 1 juli 2024**

Indien een woonruimte een rijksmonument is of daar deel van uitmaakt, als bedoeld in artikel 1.1 Erfgoedwet, dan worden 10 punten extra toegekend. Hiermee worden rijksmonumenten, en dus niet gemeentelijke monumenten, bedoeld die zijn geregistreerd in het monumentenregister van de Rijksdienst voor het Cultureel Erfgoed. Alleen deze monumenten krijgen een toeslag van 10 punten.

Het Rijksmonumentenregister kan door eenieder worden geraadpleegd. Het register bevat gegevens over de inschrijving en ter identificatie van de Rijksmonumenten: http://monumentenregister.cultureelerfgoed.nl/.

> De datum van afsluiten van de huurovereenkomst dient gespecificeerd te worden voor Rijksmonumenten. Het VERA model heeft hier echter geen specifiek attribuut voor. Deze datum dient gespecificeerd te worden onder `extra-attributen` met als naam `datumAfsluitenHuurovereenkomst` op het `EenhedenEenheidbericht` model:
>
> ```json
> {
>   "extra-attributen": [
>     {
>       "naam": "datumAfsluitenHuurovereenkomst",
>       "waarde": "YYYY-MM-DD"
>     }
>   ]
> }
> ```

### 2.7.2 Gemeentelijk of provinciaal monument

Indien een woonruimte een gemeentelijk of provinciaal monument is of daarvan deel uitmaakt, dan wordt de maximale huurprijs vermeerderd met 15%. Het gemeentelijk monument moet zijn aangewezen door het college van burgemeester en wethouders. Een provinciaal monument moet zijn aangewezen door de gedeputeerde staten.

De Huurcommissie hanteert passief beleid. De partijen moeten aantonen dat een woning bestaat of deel uitmaakt van een gemeentelijk of provinciaal monument.

### 2.7.3 Beschermd stad- of dorpsgezicht

De maximale huurprijs wordt met 5% vermeerderd als:

a. de woonruimte behoort tot een rijksbeschermd stads- of dorpsgezicht als bedoeld in artikel 2.34. vierde lid, van de Omgevingswet;
b. de woonruimte behoort tot een woning die is gebouwd voor 1965; en
c. de woonruimte niet bestaat uit of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet of van een door het college van burgemeester en wethouders aangewezen gemeentelijk monument of een door gedeputeerde staten aangewezen provinciaal monument.
De Huurcommissie hanteert voor beschermde stads- en dorpsgezichten een passief beleid. Dit betekent dat het aan de verhuurder is om aan te tonen dat de woonruimte aan de voorwaarden voor deze prijsopslag voldoet.

_Cumulatie van opslagen_

De samenloop van verschillende opslagen is in het woningwaarderingstelsel voor onzelfstandige woonruimte niet mogelijk. De monumentenopslag (zowel de Rijksmonumenten als provinciale en gemeentelijke monumenten) en de opslag voor een beschermd stad- of dorpsgezicht kunnen niet tegelijkertijd voor dezelfde woonruimte worden toegekend (zie art. 8 lid 5 onder c Besluit huurprijzen woonruimte).

# Hoofdstuk 3 - De rubrieken van het woningwaarderingsstelsel onzelfstandige woonruimte

## Rubriek 1 - Oppervlakte van vertrekken

### 1.1 Puntentoekenning

- Privévertrekken worden gewaardeerd met 1 punt per vierkante meter.
- Gemeenschappelijke vertrekken worden ook gewaardeerd met 1 punt per vierkante meter. Dit puntenaantal wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot die gemeenschappelijke vertrekken.

> Wij hebben `gedeeldMetAantalOnzelfstandigeWoonruimten` toegevoegd als property van ruimten om te kunnen specificeren of een ruimte gedeeld wordt met andere personen op hetzelfde adres.

### 1.2 Wat zijn vertrekken?
> De gespecificeerde ruimtesoort is leidend bij de waardering van een ruimte. Een ruimte dient `Ruimtesoort` `vertrek` te hebben om in aanmerking te komen voor een waardering in de rubriek 'Oppervlakte van vertrekken'.
>
> Een ruimte dient alleen als vertrek gespecificeerd te worden wanneer deze voldoet aan alle onderstaande eisen. De doorgehaalde eisen worden niet door het systeem gecontroleerd.
>
> Wanneer een ruimte met `Ruimtesoort` `vertrek` niet voldoet aan de minimale oppervlakte, wordt er gekeken of de ruimte gewaardeeerd kan worden onder de rubriek 'Oppervlakte van overige ruimten'.

Een ruimte wordt als vertrek gewaardeerd als deze voldoet aan de volgende eisen:

- ~~de vloer moet begaanbaar zijn;~~
- ~~de muren/wanden dienen uit “vast” materiaal te bestaan;~~
- ~~de ruimte dient over tenminste 80% van de lengte (de langste zijde) ten minste 1,50 m breed te zijn;~~
- de ruimte dient een oppervlakte te hebben van minimaal 4 m2;
- ~~de ruimte dient over ten minste 50% van de oppervlakte of over een oppervlakte van 11 m2 een vrije hoogte te hebben van ten minste 2,10 m (gemeten vanaf de vloer tot het zichtbare plafond (onder het zichtbare plafond aanwezige balken blijven buiten de meting);~~
- ~~de ruimte dient te zijn voorzien van minimaal 0,5 m2 aan de buitenlucht grenzend transparant oppervlak (bijvoorbeeld een raam of deur met vensters);~~
- ~~de ruimte dient te beschikken over direct met de buitenlucht verbonden ventilatie;~~
- ~~er moet ten minste één stopcontact en één lichtpunt aanwezig zijn.~~

Voorbeelden van vertrekken zijn onder andere de woonkamer, een hobbykamer, studeerkamer, slaapkamer en eetkamer, maar dus alleen als aan de hierboven gestelde eisen wordt voldaan.

In afwijking van bovenstaande eisen is een ruimte die uitsluitend als keuken, badkamer of doucheruimte dient altijd een vertrek.

Van de minimumoppervlakte zoals hiervoor genoemd kan niet worden afgeweken. Heeft de ruimte bijvoorbeeld een oppervlakte van 3,5 of 3,85 m2, dan wordt niet aan de gestelde eis van minimaal 4 m2 voldaan. De oppervlakte mag niet naar boven worden afgerond waardoor invulling aan de eis zou zijn gegeven.

**Zolderruimte**

Voor zolderruimten gelden, naast bovenstaande eisen, nog twee eisen om als vertrek gewaardeerd te worden. De zolderruimte moet namelijk bereikbaar zijn via een vaste trap ~~en het dak moet beschoten zijn.~~

### ~~1.3 Meetinstructies~~

~~De wetgever heeft in de toelichting op het woningwaarderingsstelsel een aantal meetinstructies meegegeven:~~

> De woningwaarderingpackage gaat ervanuit dat ruimten worden ingestuurd die zijn gemeten volgens de meetinstructies van de huurcommissie.

### 1.4 Puntenberekening en saldering

De oppervlakten voor privé- en gemeenschappelijke vertrekken worden afzonderlijk berekend. Als sprake is van meerdere vertrekken die tot dezelfde categorie behoren (privé of gemeenschappelijk), dan wordt voor de berekening eerst de oppervlakte voor die categorie vertrek afgerond en per categorie punten toegekend alvorens die bij elkaar worden opgeteld.

De Huurcommissie bepaalt eerst de oppervlakte per vertrek afgerond op twee decimalen. Daarna wordt de oppervlakte van alle vertrekken per categorie (privé of gemeenschappelijk) gesaldeerd en vind afronding plaats op hele vierkante meter. Bij 0,5m² of meer wordt afgerond naar boven, bij minder dan 0,5m² naar beneden. Als laatste wordt een waardering in punten toegekend.

Voorbeeld Puntenberekening en saldering

```text
Privévertrekken

Privékamer: lengte 3,76m x breedte 4,12m = 15,4912 m², afgerond : 15,49 m²

Gemeenschappelijke vertrekken voor drie kamers

Gedeelde keuken: lengte 2,95m x breedte 3,81m = 11,2395 m², afgerond : 11,24 m²

Totaal: 15 m2 privévetrekken en 11 m2 gemeenschappelijk vertrekken

Dit vertaalt zich naar 15 (15*1) + 3.75* (11 * 1 gedeeld door 3 kamers) = 18.75 punt

*11 punten gedeeld door 3 (kamers) = 3,67. Er wordt afgerond op 0,25 punt, waarbij een achtste punt naar boven wordt afgerond, waardoor de uitkomst 3,75 punt is.
```

## Rubriek 2 - Oppervlakte van overige ruimten

### 2.1 Puntentoekenning

Privé overige ruimten worden gewaardeerd met 0,75 punt per vierkante meter.
Gemeenschappelijke overige ruimten worden gewaardeerd met 0,75 punt per vierkante meter. Dit puntenaantal wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft tot de gemeenschappelijke overige ruimte(n).

### 2.2 Wat zijn overige ruimten?
> De gespecificeerde ruimtesoort is leidend bij de waardering van een ruimte. Een ruimte met `Ruimtesoort` `overige ruimte` komt in aanmerking voor waardering in de rubriek 'Oppervlakte van overige ruimten' als de oppervlakte minimaal 2 m² is. Een ruimte met `Ruimtesoort` `vertrek` komt in aanmerking voor waardering in de rubriek 'Oppervlakte van overige ruimten' als de oppervlakte minder dan 4 m² en minimaal 2 m² is.
>
> Een ruimte dient alleen als overige ruimte gespecificeerd te worden wanneer deze voldoet aan alle onderstaande eisen. De doorgehaalde eisen worden niet door het systeem gecontroleerd.

Een ruimte wordt als overige ruimte gewaardeerd als deze voldoet aan de volgende eisen:

- ~~de vloer moet begaanbaar zijn;~~
- de ruimte dient een oppervlakte te hebben van minimaal 2 m2; en
- voldoet niet aan de eisen voor een vertrek (zie paragraaf 1.2) of een verkeersruimte zijnde;
- ~~een ruimte die dient voor het bereiken van een andere ruimte;~~
- ~~geen ruimte om duurzaam in te verblijven.~~

Voorbeelden van overige ruimten zijn bijkeukens, bergingen, wasruimten, schuren, garages, zolders en kelders, op voorwaarde dat aan bovenstaande eisen wordt voldaan.
Parkeerruimte die exclusief tot één adres behoort (privé-garage), wordt gewaardeerd als overige ruimte. Gemeenschappelijke garages met daarin parkeerplek(ken) worden gewaardeerd onder rubriek 10  (gemeenschappelijke parkeerruimten).

Van de minimumoppervlakte zoals hiervoor genoemd kan niet worden afgeweken. Heeft de ruimte bijvoorbeeld een oppervlakte van 1,95 m², dan wordt niet aan de gestelde eis van minimaal 2 m² voldaan. De oppervlakte mag niet naar boven worden afgerond waardoor invulling aan de eis zou zijn gegeven.

#### Verkeersruimten

Verkeersruimten zoals hallen, gangen, en overlopen worden sowieso niet afzonderlijk gewaardeerd, dus krijgen geen punten op basis van dit onderdeel van het woningwaarderingsstelsel.

#### Zolderruimte

Indien een zolderruimte niet als vertrek kan worden gewaardeerd (zie paragraaf 1.2), dan kan deze mogelijk wel in aanmerking komen voor een waardering als overige ruimte. Dan moet de zolderruimte naast bovenstaande eisen aan nog twee eisen voldoen. De zolderruimte moet namelijk bereikbaar zijn via een tot de woning behorende trap ~~en het dak moet beschoten zijn.~~ Voldoet de zolderruimte niet aan de eisen van paragraaf 1.2 en niet aan de voornoemde eisen, dan wordt de zolderruimte niet gewaardeerd.

#### Toiletruimte

Een toiletruimte kan als overige ruimte worden gewaardeerd als aan de eisen van overige ruimte wordt voldaan.

### ~~2.3 Meetinstructies~~

~~De wetgever heeft in de toelichting op het woningwaarderingsstelsel een aantal meetinstructies meegegeven:~~

> De woningwaarderingpackage gaat ervanuit dat ruimten worden ingestuurd die zijn gemeten volgens de meetinstructies van de huurcommissie.

### 2.4 Saldering en puntenberekening

De oppervlakten voor privé en voor gemeenschappelijke overige ruimten worden afzonderlijk berekend. De punten voor privé overige ruimte(n) worden uitsluitend in de berekening betrokken voor de woonruimte in kwestie.

De punten voor gemeenschappelijke overige ruimte(n) moeten worden verdeeld over het aantal onzelfstandige woonruimtes.

Als sprake is van meerdere overige ruimten die tot dezelfde categorie behoren (privé of gemeenschappelijk) dan wordt voor de berekening eerst de oppervlakte per categorie overige ruimte berekend en afgerond.

Voor privé overige ruimte betekent dit dat de oppervlakte van de overige ruimtes bij mekaar worden opgeteld en op basis daarvan punten worden toegekend.

Voor gemeenschappelijke overige ruimtes betekent dit ook dat de oppervlakte van deze overige ruimtes bij elkaar worden opgeteld en op basis daarvan punten worden toegekend. Om de juiste punten aan de woonruimte in kwestie te kunnen toerekenen moeten de punten eerst nog worden verdeeld door het aantal onzelfstandige woonruimtes die gebruikmaken van de gemeenschappelijke overige ruimte.

De oppervlakte per overige ruimte wordt afgerond op 2 decimalen. De afronding van de oppervlakte van alle overige ruimte samen vindt plaats op hele vierkante meters na saldering van de oppervlakte van de afzonderlijke overige ruimten; bij 0,5 m2 of meer wordt naar boven afgerond, bij minder dan 0,5 m2 naar beneden. Waardering in punten vindt na saldering en afronding plaats.

```text
Voorbeeld:

Privé overige ruimten

Er is sprake van één privé overige ruimte van 4 m2. Er worden 3 punten toegekend (4 x 0,75).

Gemeenschappelijke overige ruimten voor drie kamers

Garage: lengte 3,16m x breedte 6,12m = 19,3392 m², afgerond : 19,34 m²
Bijkeuken: lengte 2,11m x breedte 2,87m = 6,0557 m², afgerond : 6,06 m²
Totaal : 25,40 m² Afronding op hele m² : 25 m².

Dit vertaalt zich dan naar 25 * 0,75 punt (per m2) = 18.75 punten. Dit puntenaantal wordt gedeeld door 3 (kamers) en de uitkomst is 6,25 punt.

In totaal is voor de woonruimte in dit voorbeeld een puntenaantal van 3 plus 6,25 punten, dus 9.25 punten voor overige ruimte.
```

## Rubriek 3 - Verkoeling en verwarming

### 3.1 Puntentoekenning

**Vertrekken**

- Verwarmde privévertrekken worden gewaardeerd met 2 punten.
- Verwarmde gemeenschappelijke vertrekken worden gewaardeerd met 2 punten. Dit puntenaantal wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

**Overige ruimten**

- Verwarmde privé overige ruimten en verkeersruimten worden gewaardeerd met 1 punt met een maximum van 4 punten voor alle overige ruimtes en verkeersruimten (samen).
- Verwarmde gemeenschappelijke overige ruimten en verkeersruimten worden gewaardeerd met 1 punt per ruimte met een maximum van 4 punten voor alle overige ruimten en verkeersruimten (samen). Dit puntenaantal wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.

**Extra voorziening**

- Voorzieningen met zowel een verwarmingsfunctie als verkoelingsfunctie worden per privé vertrek gewaardeerd met 1 punt tot een maximum van 2 punten (bij meerdere vertrekken met een verkoelingsfunctie).
- Voorzieningen met zowel een verwarmingsfunctie als verkoelingsfunctie worden per gemeenschappelijk vertrek gewaardeerd met 1 punt tot een maximum van 2 punten. Dit puntenaantal wordt gedeeld door het aantal onzelfstandige woonruimten dat toegang en gebruiksrecht heeft.
- ~~Woningen die zonder koeling voldoende koel kunnen blijven, worden per vertrek gewaardeerd met 1 extra punt tot een maximum van twee punten. Of sprake is van zo’n woning, dient te worden bepaald met de NTA 8800 en blijkt uit een actueel NTA-energielabel waarin de koelfunctie is meegenomen en het risico voor oververhitting als ‘laag’ is afgegeven.~~

### 3.2 Onroerende zaak en onroerende aanhorigheden

~~Punten voor verwarming en verkoeling worden alleen toegekend als de verwarming of de voorziening met zowel een verwarmingsfunctie als verkoelingsfunctie tot de onroerende zaak en zijn onroerende aanhorigheid behoort.~~

~~Dit is bij een radiator het geval als hij is bevestigd aan de muur of in de grond. Een mobiele elektrische radiator of mobiele airco behoort niet tot de onroerende zaak. Hetzelfde geldt voor gevelkachels en gashaarden. Een verdikte buis, pijp of moederhaard wordt wél gerekend tot de onroerende zaak, indien deze als zodanig bedoeld of herkenbaar is.~~

> De properties `verkoeld` en `verwarmd` mogen alleen gebruikt worden voor ruimten die verkoeld dan wel verwarmd worden door onroerende zaken die tot de onroerende aanhorigheid behoren.

**Koelsystemen**

~~Centrale koelsystemen, zoals omkeerbare warmtepompen, passieve koeling door een bodemlus of een WKO-systeem moeten voorzien zijn van vloerkoeling, lage temperatuur radiatoren of radiatorconvectoren. Voor andere onroerend aanhorige koelsystemen, zoals een vaste airco, geldt dat deze een productgebonden energielabel moet hebben van minimaal A+ (bepaald volgens de Europese Ecodesign-richtlijn), en een minimaal vermogen moet kunnen leveren van 100 W/m2 bij een werkingstemperatuur tot 35 graden Celsius.~~

> Indien een ruimte wordt doorgegeven als `verkoeld` moet het koelsysteem dat ervoor zorgt dat de ruimte verkoeld wordt aan deze voorwaarden voldoen.

### 3.3 Aangrenzende ruimten met open doorgang

~~Vertrekken of overige ruimten die met elkaar in verbinding staan, worden in een bepaald geval als één verwarmd vertrek of overige ruimte gewaardeerd. Dit is het geval als zich tussen die twee verwarmde vertrekken of overige ruimten een opening bevindt, die breder is dan 50% van de muur, waarin deze opening zich bevindt. Het moet hierbij gaan om een niet afsluitbare opening, die over een breedte van minimaal 0,85 m een minimumhoogte heeft van 2 m. De muur wordt gemeten in het vertrek of overige ruimte, waarin de tussenwand het smalst is. De figuur in paragraaf 2.4 van het vorige hoofdstuk geeft dit visueel weer.~~

### 3.4 Open keukens

~~Voor deze rubriek wordt een verwarmde open keuken als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten. Onder een open keuken wordt hier verstaan een keuken die in open verbinding staat met een ander vertrek, terwijl zich tussen de keuken en het andere vertrek een opening bevindt, die breder is dan 50% van de tussenmuur.~~ Zowel de open keuken als het vertrek of overige ruimte waarmee de open verbinding bestaat, wordt voor deze rubriek individueel gewaardeerd met punten indien deze verwarmd zijn.

> Deze package gaat er vanuit dat een aanrecht in een woon- of slaapvertrek een open keuken is.

## Rubriek 4 - Energieprestatie

De energieprestatie van een woning kan sinds 1 januari 2021 op drie manieren zijn vastgesteld:

1. **Een oud energielabel**: registratie heeft plaatsgevonden vóór 1 januari 2015. In 2021 en later liepen en lopen veel sinds 1 juli 2011 verstrekte energielabels af, want de geldigheidsduur is tien jaar.
2. **De energie-index**: registratie op of na 1 januari 2015 tot 1 januari 2021. In 2025 en later lopen veel sinds 1 januari 2015 verstrekte energie-indexen af, want de geldigheidsduur is tien jaar.
3. **Het energielabel op basis van de NTA 8800**: registratie op of na 1 januari 2021.

In EP-online is te vinden wat de energieprestatie van een woning is. Voor de waardering van de energieprestatie van de onzelfstandige woonruimte(n) wordt de energieprestatie toegepast van de gehele woning (het adres) waar de onzelfstandige woonruimte onderdeel van uitmaakt.

### 4.1 Puntentoekenning

Bij een energielabel bepaalt de labelklasse (A++++ t/m G) het aantal punten dat de verhuurder mag doorrekenen in de maximale huur. Bij een energie-index is de indeling in letters vervangen door een cijfer. De energie-index wordt meegenomen indien in EP-online staat aangegeven dat de energie-index geldig is voor het woningwaarderingsstelsel.

Zie hieronder de puntentoekenning van de energieprestatie bij een geldig energie-index (oud of nieuw) energielabel.

#### Puntentoekenning energielabel

| **Energielabel** | **Energie-index (EI)**  | **Punten per m² die volgens rubriek 1 zijn toe te rekenen aan de huurder** |
|------------------|-------------------------|--------------------------------------------------------------------------|
| A++++            | n.v.t.                  | 1 punt                                                                   |
| A+++             | n.v.t.                  | 0,95 punt                                                                |
| A++              | EI < 0,6                | 0,85 punt                                                                |
| A+               | 0,6 < EI ≤ 0,8          | 0,75 punt                                                                |
| A                | 0,8 < EI ≤ 1,2          | 0,65 punt                                                                |
| B                | 1,2 < EI ≤ 1,4          | 0,50 punt                                                                |
| C                | 1,4 < EI ≤ 1,8          | 0,35 punt                                                                |
| D                | 1,8 < EI ≤ 2,1          | 0,20 punt                                                                |
| E                | 2,1 < EI ≤ 2,4          | -0,05 punt                                                               |
| F                | 2,4 < EI ≤ 2,7          | -0,10 punt                                                               |
| G                | EI > 2,7                | -0,15 punt                                                               |

Zoals aangegeven in de tabel hierboven, worden voor de waardering van energieprestatie de punten per m² die volgens rubriek 1 (oppervlakte van vertrekken) zijn toe te rekenen aan de onzelfstandige woonruimte gebruikt om de punten voor energieprestatie te berekenen.

#### Voorbeeld Puntentoekenning

Huurder A huurt één onzelfstandige woonruimte. Het totale privévertrek beslaat 10 m². Daarnaast is het totale oppervlakte van de aanwezige gemeenschappelijke vertrek op het adres 40 m². Huurder A deelt dit met drie andere huurders van onzelfstandige woonruimten op dit adres.

Het aantal m² dat volgens rubriek 1 aan de huurder is toe te rekenen is 10 m² + 10 m² (40 m² / 4) = 20 m². Het energielabel van de woning is A. Dit maakt het aantal punten in deze rubriek:  
20 m² x 0,65 punt = **13 punten**.

### 4.2 Bouwjaar bepalend bij ontbreken geldig energielabel of energie-index

Indien op de peildatum van de woningwaardering een geldig energielabel of energie-index ontbreekt of als de geldigheidsduur van het energielabel is verstreken, dan bepaalt het bouwjaar van de woning het aantal punten.

De puntentelling bij toepassing bouwjaar is als volgt:

#### Puntentelling bij toepassing bouwjaar

| **Bouwjaar**      | **Punten per m² die volgens rubriek 1 zijn toe te rekenen aan de huurder** |
|-------------------|---------------------------------------------------------------------------|
| 2002 en later     | 0,65 punt                                                                 |
| 2000 t/m 2001     | 0,50 punt                                                                 |
| 1992 t/m 1999     | 0,35 punt                                                                 |
| 1984 t/m 1991     | 0,20 punt                                                                 |
| 1979 t/m 1983     | -0,05 punt                                                                |
| 1977 t/m 1978     | -0,10 punt                                                                |
| 1976 of ouder     | -0,15 punt                                                                |

### 4.3 Monumenten

Voor Rijks-, provinciale en gemeentelijke monumenten gelden, in afwijking van andere woningen, geen minpunten voor de energielabels E, F, en G. De puntentoekenning bedraagt dan, in afwijking van bovenstaande tabellen, **0 punten**.

### 4.4 Afwijkingsbevoegdheid hogere energielabelklasse dan A++++

> Het is mogelijk om met een energielabel A++++ de punten voor de Energieprestatie te berekenen.

De hierboven vermelde tabellen met de puntentoekenning voor de labelklasse gaan tot A++++. De Huurcommissie heeft de bevoegdheid om af te wijken van de hierboven aangegeven puntenwaardering indien de gemaakte kosten om deze energieprestatie te bereiken, aanmerkelijk afwijken van hetgeen als gangbaar wordt beschouwd, of indien de energieprestatie aanmerkelijk beter is dan hetgeen als gangbaar bij een energielabelklasse A++++ wordt beschouwd.

### ~~4.5 Gerede twijfel energielabel~~

> In woningwaardering package wordt er vanuit gegaan dat een energieprestatie juist is.

~~Als een huurder twijfelt aan de juistheid van het toepasselijke energielabel, dan heeft de Huurcommissie de bevoegdheid om een 'eigen oordeel' uit te spreken bij gerede twijfel van het energielabel. Een Huurcommissie Eigen Oordeel (HEO) kan worden uitgesproken indien de huurder aantoont dat er sprake is van gerede twijfel over de juistheid van het energielabel/energie-index en dat het gewijzigde energielabel/energie-index van invloed zal zijn op de maximaal redelijke huurprijs.~~

~~Bij ‘gerede twijfel’ wordt beoordeeld of de huurder voldoende heeft aangetoond dat een verkeerd woningkenmerk is gebruikt bij het vaststellen van het energielabel, waardoor de juistheid van de labelklasse voor de woning in het geding is. Voorbeelden van foutieve kenmerken zijn:~~

~~- Verkeerd soort glas, bijvoorbeeld enkel in plaats van dubbel glas.~~
~~- Verkeerd type woning, zoals een hoekwoning in plaats van een tussenwoning.~~
~~- Slecht geïsoleerde muren terwijl het energielabel aangeeft dat het huis goed geïsoleerd is.~~

~~De huurder dient gerede twijfel aan te tonen door middel van het energielabelafschrift en moet onderbouwen waarom een onjuist woningkenmerk is gebruikt. Het energielabelafschrift is te downloaden via Mijnoverheid.~~

~~Indien de Huurcommissie tot een eigen oordeel wil komen, dan laat de Huurcommissie onderzoeken wat de energieprestatie van de woning is. Het eigen oordeel is uitsluitend in de voorliggende zaak van kracht, wordt niet geregistreerd in het register van de Rijksdienst voor Ondernemend Nederland, en komt te vervallen na ontbinding van de huurovereenkomst.~~

### 4.6 Energieprestatievergoeding

Voor woningen die zelf (gedeeltelijk) in hun energieverbruik voorzien, bijvoorbeeld door zonnepanelen, kan bij het verhuren een energieprestatievergoeding (EPV) worden afgesproken. De woning moet dan voldoen aan de eisen voor een EPV. Als dit het geval is, dan is het aantal punten op basis van het puntenstelsel voor de energieprestatie lager.

Om te voorkomen dat in gevallen waarin een energieprestatievergoeding is overeengekomen, de opwekking van energie voor de huurder tevens wordt verdisconteerd in de huurprijs door middel van puntentoekenning vanwege het energielabel/-index, wordt voor deze woningen een correctiefactor toegepast op het aantal punten voor de energieprestatie. In deze gevallen wordt de energieprestatie gewaardeerd met **0,50 punt per m²**.

## Rubriek 5 - Keuken

### 5.1 Eisen keuken

Punten worden alleen aan het onderdeel ‘keuken’ toegekend als de keuken voldoet aan het volgende basisniveau:

- ~~aan- en afvoer van water en ten minste één vast aansluitpunt voor koken op gas of elektriciteit;~~
- een aanrechtblad met een aan een gesloten lengte van minimaal 1 m ~~(lengte incl. spoelbak, incl. kookplaat);~~
- ~~twee inbouwkasten met een breedte van minimaal 50 cm;~~
- ~~waterdichte afwerking boven het aanrechtblad en in de kookhoek vanaf de vloer tot een hoogte van minimaal 1,50 m.~~

> Zorg ervoor dat alleen aanrechten met een spoelbak worden meegegeven en dat deze spoelbak niet ook nog als aparte `wastafel` wordt meegegeven.

Als de keuken niet voldoet aan het basisniveau, worden geen punten toegekend. Een spoelbak in een keuken die voldoet aan het basisniveau, krijgt alleen de waardering voor de rubriek keuken en niet ook nog als ‘wastafel’.

Een waterdichte afwerking wordt in beginsel verondersteld aanwezig te zijn, maar kan pas worden meegenomen als deze aan te merken valt als onroerende aanhorigheid. Dat betekent dat een keuken met bijvoorbeeld een tegelwand of aangebrachte, waterdichte verf wel voldoet aan de eis van een waterdichte afwerking, maar als er slecht een plastic zeil voor een wand is gehangen niet.

### 5.2 Puntentoekenning lengte aanrecht

De waardering van de keukeninstallatie wordt bepaald op basis van de lengte van het aanrecht. ~~Hierbij worden alleen punten toegekend als het aanrechtblad waterdicht is.~~

- Bij een aanrechtlengte minder dan 1 meter worden 0 punten toegekend.
- Bij een aanrechtlengte tussen de 1 en 2 meter worden 4 punten toegekend.
- Bij een aanrechtlengte tussen de 2 en 3 meter worden 7 punten toegekend.
- Bij een aanrechtlengte van meer dan 3 meter worden 10 punten toegekend, worden 13 punten toegekend als er minimaal 8 onzelfstandige woonruimten toegang en gebruiksrecht hebben tot de keuken.

De toegekende punten worden gedeeld door het aantal onzelfstandige woningen dat toegang en gebruiksrecht heeft.

Een aanrecht met spoelbak, waarvan de lengte minder bedraagt dan 1 m, voldoet dus niet aan de eis van 1 m en wordt daarom niet als aanrecht gewaardeerd, maar als wastafel. ~~Een aanrecht zonder onderkasten wordt ook gewaardeerd als wastafel.~~

~~### 5.3 Meetinstructies lengte aanrechtblad~~

> De woningwaarderingpackage gaat ervanuit dat lengten van aanrechten worden ingestuurd die zijn gemeten volgens de meetinstructies van de huurcommissie.

~~De aanrechtlengte wordt over het midden van het bovenblad gemeten, inclusief ingebouwde spoelbakken en kookplaten.~~

~~De lengte van een niet direct aan het aanrecht aansluitend werkblad of van een blad dat is samengesteld uit een ander materiaal wordt bij de lengte meegeteld.~~

~~Indien een aanrechtblad langer is dan de aanwezige onderkasten met de bedoeling dat er onder het langere gedeelte van het aanrechtblad een losstaande koelkast, vaatwasser, wasmachine e.d., kan worden geplaatst, dan wordt dit gedeelte van het aanrechtblad mee gemeten mits er onder het blad aansluitmogelijkheden aanwezig zijn voor genoemde apparatuur.~~

~~Van een (standaard)aanrechtblad dat gedeeltelijk is ingemetseld of waar de wandbetegeling op het blad is aangebracht, wordt uitsluitend het bruikbare c.q. zichtbare gedeelte gemeten.~~

~~Indien er sprake is van een hoekaanrecht wordt de lengte van het aanrecht bepaald door (zie figuur):~~

~~De lange zijde van het langere aanrechtdeel te meten (zie horizontale blauwe lijn).~~
~~Vervolgens die lengte te salderen met de lange zijde van het kortere aanrechtdeel (zie verticale blauwe lijn).~~
~~De lengte van een kookeiland wordt bepaald door de lengte van de lange zijde.~~

### 5.4 Puntentoekenning extra voorzieningen

Het woningwaarderingsstelsel geeft voor het onderdeel keuken extra punten voor voorzieningen in de keuken. Hiervoor geldt een maximum tot het aantal punten dat voor de aanrechtlengte is bepaald. Een keuken met een aanrechtlengte tussen de 1 en 2 m kan bijvoorbeeld tot maximaal 4 extra punten krijgen voor voorzieningen en een keuken met een aanrechtlengte van 2 of meer meter kan tot maximaal 7 punten extra krijgen voor voorzieningen. 

Zie hieronder de limitatieve lijst met voorzieningen waarvoor extra punten worden toegekend.

Voorzieningen

| Voorziening | Punten |
| --- | --- |
| Inbouw afzuiginstallatie* | 0,75 |
| Inbouw kookplaat inductie | 1,75 |
| Inbouw kookplaat keramisch | 1 |
| Inbouw kookplaat gas | 0,5 |
| Inbouw koelkast | 1 |
| Inbouw vrieskast | 0,75 |
| Inbouw oven elektrisch | 1 |
| Inbouw oven gas | 0,5 |
| Inbouw magnetron | 1 |
| Inbouw vaatwasmachine | 1,5 |
| Extra kastruimte boven het minimum (per 60 cm breedte, met een minimum van 60 cm hoogte) | 0,75 |
| Éénhandsmengkraan | 0,25 |
| Thermostatische mengkraan | 0,5 |
| Kokend waterfunctie (al dan niet apart of in aanvulling op de kraan) | + 0,5 |

* _Bij een afzuiginstallatie gaat het om een luchtafvoer met afzuiging naar buiten de woning of op basis van recirculatie met actieve koolstof- en vetfilters. Een afzuiginstallatie kan zowel een afzuig- of recirculatiekap boven de kookinstallatie zijn, als een in het aanrecht geïntegreerd afzuigsysteem._
  
** _Om aan het basisniveau voor de kwalificatie als keuken te voldoen, moeten twee inbouwkasten met een breedte van minimaal 50 cm (per stuk) aanwezig zijn. De totale minimumbreedte bedraagt dus 1 meter. Per 60 cm breedte extra kastruimte kan vervolgens, als ook aan de andere eisen wordt voldaan, 0,75 punt extra worden toegekend._

Wanneer een object twee voorzieningen heeft, bijvoorbeeld een ingebouwde combi magnetron/oven of een gecombineerde koel- en vrieskast, worden beide voorzieningen in dit object gewaardeerd conform bovenstaande lijst. ~~Voor de meting van keukenkasten wordt uitgegaan van de buitenmaat.~~

De toegekende punten worden gedeeld door het aantal onzelfstandige woningen dat toegang en gebruiksrecht heeft.

Voorbeeld

```text
Voorbeeld: op een adres zijn vier onzelfstandige woonruimten. Er is één keuken, met een aanrechtlengte tussen 2 m en 3 m. Hiervoor worden 7 punten toegekend. Daarnaast worden 3 punten toegekend voor voorzieningen (bijv. een inbouwkoelkast, inbouw keramische kookplaat en inbouw magnetron). Omdat de keuken wordt gedeeld door vier onzelfstandige woonruimten, geldt 10/4 = 2,5 punt per onzelfstandige woonruimte.
```

## Rubriek 6 - Sanitair

### 6.1 Puntentoekenning sanitaire basisvoorzieningen

Het woningwaarderingsstelsel geeft punten aan sanitaire basisvoorzieningen:

| Voorziening | Punten |
| --- | --- |
| Toilet in een aparte ruimte | 3 |
| Toilet in een badkamer | 2 |
| Hangend toilet in aparte ruimte | 3,75 |
| Hangend toilet in badkamer | 2,75 |
| Wastafel* | 1 |
| Meerpersoonswastafel | 1,5** |
| Douche | 3 |
| Bad | 5 |
| Bad en douche | 6 |

\* Tot een maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer. Op een adres met minimaal acht of meer onzelfstandige woonruimten geldt dit maximum niet voor maximaal één ruimte. Dat betekent dat er voor adressen met acht of meer onzelfstandige woonruimten maximaal één ruimte mag zijn, naast de badkamer, met meer dan één wastafel die voor waardering in aanmerking komt.

\*\* _Tot een maximum van 1,5 punt per vertrek of overige ruimte m.u.v. de badkamer. Op een adres met minimaal 8 of meer onzelfstandige woonruimten geldt het bovengenoemde maximum niet voor maximaal één ruimte._

De toegekende punten worden gedeeld door het aantal onzelfstandige woningen dat toegang en gebruiksrecht heeft.

**Toilet**

Punten worden toegekend aan een toilet met waterspoeling als het toilet is geplaatst in een daartoe bestemde ruimte ~~en als het toilet binnen het woongebouw is gelegen~~. ~~Wanneer sprake is van een toilet dat buiten de woning maar binnen het woongebouw is gelegen, dan geldt dat het toilet in de waardering wordt meegenomen als het gebruik van het toilet door derden is uit te sluiten~~. Toiletten buiten toiletruimten en badkamers komen niet in aanmerking voor waardering.

**Wastafel**

~~Als wastafels worden alle bakken geteld voor wassen en spoelen die op de waterleiding én op het huisriool zijn aangesloten. Een dergelijke bak wordt niet als wastafel gewaardeerd indien boven de bak een douche is aangebracht. Een bad of spoelbakken in een keukenaanrecht, bidet of lavet wordt niet als wastafel, douche of bad gewaardeerd. Wastafels worden gewaardeerd tot een maximum van 1 punt per vertrek of overige ruimte, m.u.v. de badkamer.~~

> Zorg dat wastafels alleen worden meegenomen die voldoen aan de vereisten van een wastafel.

~~Van een meerpersoonswastafel is sprake bij een wastafel met een minimale breedte van 70 cm, voorzien van twee kranen.~~ Deze wastafels worden tot maximaal 1,5 punt per vertrek of overige ruimte, m.u.v. de badkamer, gewaardeerd. De kranen worden afzonderlijk gewaardeerd.

Zoals genoemd in paragraaf 5.2  waardeert de Huurcommissie een fonteintje en een aanrecht dat niet voor punten in aanmerking komt, waarvan de aanrechtlengte korter is dan één meter, als wastafel. In alle andere gevallen wordt een spoelbak in de keuken dus niet als wastafel gewaardeerd.

> Indien een aanrecht met een lengte van minder dan één meter wordt meegegeven wordt deze als wastafel gewaardeerd. Geef hier niet ook nog een wastafel mee voor de spoelbak.

**Bad en douche**

~~Als douche wordt meegeteld iedere door de verhuurder aangebrachte installatie voor het nemen van een stortbad. Hieronder valt eveneens een zogenaamde douchecabine, die voldoet aan bovengenoemde voorwaarden, als de douchcabine in een vertrek (anders dan bad- of doucheruimte) of overige ruimte is geplaatst. De oppervlakte van dat vertrek of van die overige ruimte wordt in dat geval niet verminderd met de door de douchecabine ingenomen oppervlakte.~~

Aan baden worden 5 punten toegekend, ~~ongeacht de lengte van het bad, als een volwassen persoon er in een normale zithouding in kan plaatsnemen. Indien een bad is voorzien van een (hand)douche, dan wordt het douchegarnituur niet afzonderlijk geteld.~~

Indien in de badruimte behalve het bad tevens een afzonderlijke douche is aangebracht, geldt een waardering van 6 punten.

~~Als het aansluitpunt voor warm en koud water bedoeld is voor gecombineerd gebruik van zowel een wastafel als de naastgelegen douche of bad (bijvoorbeeld door middel van een zogenaamde zwenkarm), dan wordt uitsluitend de douche of het bad gewaardeerd. Dus niet én 1 punt voor wastafel én 5 punten voor douche of respectievelijk bad.~~

### 6.2 Puntentoekenning extra voorzieningen

Het woningwaarderingsstelsel geeft voor het onderdeel sanitair extra punten voor voorzieningen in de bad- of doucheruimte. Hiervoor geldt een maximum tot het aantal punten dat reeds voor douche, bad en/of bad/douche is verkregen. Anders gezegd: maximaal een verdubbeling van de toegekende punten voor douche, bad en/of bad/douche.

**Eisen bad-of doucheruimte**

Punten voor extra voorzieningen worden enkel toegekend indien deze zich bevinden in een bad- of doucheruimte. Bad- of doucheruimten moeten voldoen aan de volgende eisen:

- ~~Een waterdichte vloerafwerking*.~~
- ~~De ruimte heeft over ten minste 50% van de oppervlakte een vrije hoogte van 2,00 m. (gemeten vanaf de vloer tot het zichtbare plafond).~~
- ~~Waterdichte afwerking tot 1,50 m hoogte voor badruimte en 1,80 m voor doucheruimte;~~
- Een wastafel ~~inclusief (tweehands-)mengkraan en een spiegel.~~
- Een douche of bad ~~met aansluitpunten voor warm en koud water (niet zijnde een warmwater apparaat) en voorzien van een warm- en koudwaterkraan of een mengkraan.~~

\* Een bad in een vertrek met een niet-waterdichte vloer wordt door de Huurcommissie wel gewaardeerd, omdat het bad zelf als een waterdichte afwerking wordt gezien.

**Lijst voorzieningen**

Zie hieronder de limitatieve lijst met voorzieningen waarvoor extra punten worden toegekend.

Voorzieningen in de bad- of doucheruimte

| Voorziening | Punten |
| --- | --- |
| Bubbelfunctie van het bad | 1,5 |
| Gemonteerde volledige afscheiding van de douche* | 1,25 |
| Handdoekenradiator | 0,75 |
| Ingebouwd kastje met in- of opgebouwde wastafel | 1 |
| Kastruimte (minimale breedte van 40cm, en minimale hoogte van 40cm) | 0,75 |
| Stopcontact (maximaal twee per wastafel) | 0,25 |
| Éénhandsmengkraan | 0,25 |
| Thermostatische mengkraan | 0,5 |

\* In het geval van een gemonteerde volledige afscheiding van de douche vindt de waardering van 1,25 punten plaats wanneer doucheruimte beschikt over  een onroerend aanhorige afscheiding met  een waterdichte afwerking aan alle zijden van de douche. Ter illustratie: glazen deuren vallen hier wel onder, maar een douchegordijn (dat snel weggenomen kan worden) niet.

> Voor een ingebouwde kast met wastafel moet de wastafel als aparte voorziening worden meegegeven.

~~Indien het aansluitpunt voor warm en koud water bedoeld is voor gecombineerd gebruik van zowel een wastafel als de naastgelegen douche of bad (bijvoorbeeld door middel van een zogenaamde zwenkarm), dan wordt uitsluitend de douche of het bad gewaardeerd. Dus niet én 1 punt voor wastafel én 3 of 5 punten voor douche of, respectievelijk bad.~~

De toegekende punten worden gedeeld door het aantal onzelfstandige woningen dat toegang en gebruiksrecht heeft.

Voorbeeld

```text
Voorbeeld: op een adres zijn vier onzelfstandige woonruimten. Er is één badkamer met een douche (3 punten), met gemonteerde afscheiding (1,25 punt) en handdoekradiator (0,75 punt). Daarnaast beschikt elke huurder over een eigen toilet (3 punten) in de onzelfstandige woonruimte. De badkamer levert in totaal 5 punten op (3 + 1,25 + 0,75). De badkamer wordt gedeeld door vier onzelfstandige woonruimten, dus 5/4 = 1,25 punt per onzelfstandige woonruimte. De vier onzelfstandige woonruimten hebben elk hun eigen toilet, dus dit puntenaantal hoeft niet nader gedeeld te worden. In dit voorbeeld geldt daarom dat elke huurder 1,25 + 3 = 4,25 punten krijgt voor de rubriek sanitair.
```

## ~~Rubriek 7 - Woonvoorzieningen voor gehandicapten~~

### ~~7.1 Puntentoekenning~~

~~Het woningwaarderingsstelsel kent punten toe voor woonvoorzieningen voor gehandicapten. Per € 332,00 van de door de verhuurder aan ingrepen in of aan de woonruimte ten behoeve van een gehandicapte bestede kosten kan, voor zover deze kosten in een redelijke verhouding staan tot de geboden kwaliteit en het niet gesubsidieerde kosten betreft, één punt worden toegekend.~~

~~De toegekende punten worden gedeeld door het aantal gehandicapten dat toegang en gebruiksrecht heeft tot de voorzieningen.~~

### ~~7.2 Woonvoorzieningen~~

~~Om de bestede kosten in of aan de woonruimte ten behoeve van een gehandicapte in de puntentelling te betrekken, is het nodig dat het gaat om:~~

1. ~~maatwerkvoorzieningen: op de behoeften, persoonskenmerken en mogelijkheden van een persoon afgestemd geheel van diensten, hulpmiddelen, woningaanpassingen en andere maatregelen ten behoeve van zelfredzaamheid, participatie of beschermd wonen en opvang, of;~~
2. ~~woningaanpassingen: een bouwkundige of woontechnische ingreep in of aan een woonruimte, als bedoeld in artikel 1.1.1, eerste lid, van de Wet maatschappelijke ondersteuning 2015, of;~~
3. ~~gesubsidieerde voorzieningen of ingrepen op grond van een andere wettelijke regeling.~~

~~Extra punten worden voor deze woonvoorzieningen, woningaanpassingen of ingrepen toegekend indien aan de volgende cumulatieve voorwaarden is voldaan:~~

- ~~de ingreep moet hebben plaatsgevonden op of ná 01-04-1994;~~
- ~~de ingreep moet voor een deel zijn gesubsidieerd;~~
- ~~de ingreep dient voor “de gehandicapte”* te zijn aangebracht.~~

~~*Onder gehandicapte wordt verstaan een persoon die ten gevolge van ziekte of gebrek aantoonbare beperkingen ondervindt.~~

~~Buiten de waardering blijven voorzieningen ten behoeve van een gehandicapte, waarvoor subsidie is verstrekt waarmee de volledige kosten worden gedekt. Extra vloeroppervlakte (als bedoeld in de subsidieregelingen) wordt aangemerkt als gesubsidieerde voorziening.~~

~~Het komt voor dat een voorziening slechts ten dele werd beschouwd als een specifieke aanpassing voor een gehandicapte en daarom slechts ten dele is gesubsidieerd. In zo’n geval worden alleen die onderdelen van de voorziening gewaardeerd, die ook in een vergelijkbare woning als standaardvoorziening voorkomen.~~

~~Indien de huurovereenkomst met de gehandicapte is beëindigd dan vervalt de toepassing van deze rubriek, tenzij de nieuwe huurder tevens gehandicapt is.~~

### ~~7.3 Vergoeding kosten~~

~~Per € 332,00 netto-investering door de verhuurder (dus het bedrag dat overblijft na aftrek van subsidie en eigen bijdrage van de huurder) wordt één punt toegekend. Voorwaarde is wel dat de kosten in een redelijke verhouding staan tot de geboden kwaliteit. De wetgever gaat ervan uit dat met deze puntenwaardering de verhuurder een redelijke rendementswaarborg heeft voor het door hem geïnvesteerde vermogen (te weten de kosten van de ingrepen, verminderd met de eigen bijdrage van de huurder en de financiële tegemoetkoming van gemeente of (bij dure woonvoorzieningen) enige instantie die ingevolge een wettelijke regeling die tegemoetkoming verleent.~~

## Rubriek 8 - Buitenruimten

### 8.1 Puntentoekenning

- Voor privé-buitenruimten worden in ieder geval 2 punten toegekend en vervolgens per vierkante meter 0,35 punt.  
*Voorbeeld: 10 vierkante meter privé-buitenruimte levert 5,5 punt op (2 + 10 x 0,35).*  

- Voor gemeenschappelijk buitenruimten op hetzelfde adres worden 0,75 per vierkante meter toegekend, gedeeld door het aantal onzelfstandige woningen dat toegang en gebruiksrecht heeft.
- Voor gemeenschappelijk buitenruimten gedeeld met meerdere adressen, worden 0,75 per vierkante meter toegekend. Dit puntenaantal wordt gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft en vervolgens gedeeld door het aantal onzelfstandige woonruimten op dat adres.
- Een aftrek van 5 punten wordt toegepast als de woning in het geheel geen privé-buitenruimte, gemeenschappelijk buitenruimte of loggia heeft.
- Maximaal 15 punten worden toegekend voor buitenruimten.

### 8.2 Definitie privé-buitenruimte

Privé-buitenruimte zijn tot de woning behorende buitenruimten, waarvan de huurder van de desbetreffende woning volgens de huurovereenkomst het exclusieve gebruiksrecht en toegang heeft. Dit kunnen onder meer voor-, zij- of achtertuinen, balkons, platjes of terrassen zijn, maar ook een oprit exclusief behorende tot de woning. Wanneer zich binnen de privé-buitenruimte een parkeerplek bevindt, geldt de parkeerplek en de weg daar naartoe als privé-buitenruimte. Gemeenschappelijke parkeerruimte wordt volgens rubriek 10 gewaardeerd.

> Ondanks dat het op basis van het woordgebruik van deze rubriek lijkt alsof parkeerplekken met meerdere onzelfstandige woonruimten op het hetzelfde adres gewaardeerd horen te worden in rubriek 10, staat in rubriek 10 expliciet vermeld dat parkeerplekken alleen worden gewaardeerd als ze gedeeld zijn met minimaal 2 adressen. Omdat anders parkeerplekken gedeeld met hetzelfde adres nergens gewaardeerd zouden worden, waarderen wij die hier in rubriek 8.

Met exclusief gebruiksrecht van privé-buitenruimte wordt bedoeld dat uitsluitend de huurder het recht heeft om te bepalen welk gebruik hij maakt van de privé-buitenruimten die tot de woning behoren.

Voor de privé-buitenruimte geldt geen minimumafmeting. 

### 8.3 Definitie gemeenschappelijke buitenruimte

Gemeenschappelijke buitenruimten hebben een minimumafmeting van 2 m x 1,5 m, 1,5 m (hoogte, breedte, diepte) en zijn tot het woongebouw behorende buitenruimten waar de bewoners in het woongebouw volgens de huurovereenkomst exclusieve toegang en gebruiksrecht toe hebben. Gemeenschappelijke buitenruimten kunnen zich bevinden op hetzelfde adres of worden gedeeld met meerdere adressen binnen hetzelfde woongebouw.

De huurder(s) moet(en) daarnaast toegang hebben tot de gemeenschappelijke buitenruimte zonder gebruikmaking van vertrekken, overige ruimten of verkeersruimten die uitsluitend ter beschikking staan aan de verhuurder of aan (een) andere huurder(s). Gedeelde buitenruimte die als parkeerplek bedoeld is, wordt gewaardeerd volgens rubriek 10.

> Er wordt vanuitgegaan dat gemeenschappelijke buitenruimten die worden meegegeven als zodanig aan de hierboven beschreven eisen voldoen.

### 8.4 Fietsenberging

Een fietsenberging wordt gewaardeerd als gemeenschappelijke buitenruimte. Onder een fietsenberging wordt verstaan een afsluitbare, overdekte bergplaats, niet zijnde een portiek, trap, gang, hal en dergelijke. Een fietsenberging in deze rubriek kan niet als overige ruimte uit rubriek 2 worden gewaardeerd, omdat deze niet onroerend is.

> `Stalling extern` en `Stalling intern` worden gewaardeerd als gemeenschappelijke buitenruimte.

### 8.4 Balkons, dakterrassen en loggia’s

Balkons, dakterrassen en loggia’s moeten aan de volgende eisen voldoen om voor punten in aanmerking te komen. Ze zijn:

- voorzien van een beloopbare afwerking, zoals vlonders, tegels e.d.;
- rondom voorzien van een afscheiding die tevens dient als valbeveiliging; en
- via een deur* of schuifpui toegankelijk zijn.

> Er wordt vanuitgegaan dat balkons, dakterrassen en loggia’s alleen worden meegegeven als ze aan de hierboven beschreven eisen voldoen.

\* Indien het balkon of dakterras is voorzien van beweegbare ramen en/of deuren in de gevel, die bestemd zijn om als buitenruimte te worden gebruikt, dan worden deze met punten gewaardeerd.

Franse balkons worden niet als buitenruimten beschouwd. Een Frans balkon is een opening in de gevel met naar binnen draaiende deuren, voorzien van een balustrade direct tegen het kozijn of de gevel. Zeembalkons worden, zolang zij voldoen aan de hiervoor aangegeven eisen van een balkon, wel gewaardeerd als buitenruimte.

> Indien een zeembalkon voldoet aan de eisen voor een balkon moet deze als `balkon` worden meegegeven.

### 8.5 Meetinstructies

Van de buitenruimten wordt de gehele onbebouwde oppervlakte gemeten, gemeten loodrecht op de voor-, achter of zijgevel. Bij balkons wordt gemeten vanaf de binnenzijde van het balkonhek. Bij (gedeeltelijk) inpandige balkons wordt bovendien gemeten ten opzichte van het terugliggende deel van de gevel. De oppervlakte, die wordt ingenomen door een balkonkast of kolenhok e.d., wordt bij de oppervlakte van de desbetreffende buitenruimte meegerekend.

### 8.6 Puntenberekening en saldering

De oppervlakten voor privé en gemeenschappelijke buitenruimten worden afzonderlijk berekend. Als sprake is van meerdere buitenruimten die tot dezelfde categorie behoren (privé, gemeenschappelijk op hetzelfde adres of gemeenschappelijk met meerdere adressen) dan wordt voor de berekening eerst de oppervlakte voor die categorie buitenruimte berekend en daarna wordt de oppervlakte van de categorie buitenruimte bij elkaar opgeteld.

De punten voor privé en gemeenschappelijke buitenruimten worden vervolgens gesaldeerd. In totaal kan maximaal 15 punten worden toegekend.

Puntenberekening en saldering
```text
Voorbeeld: in een woongebouw bevinden zich vijf adressen. Op één van deze adressen bevinden zich vier onzelfstandige woonruimten. Huurder A huurt één van deze onzelfstandige woonruimten, bestaande uit een kamer met een klein balkon (lengte 2m en breedte 0,5m). Daarnaast is er een balkon (lengte 3m en breedte 1,5m), dat huurder A deelt met de drie andere huurders van onzelfstandige woonruimten op dit adres. Tot slot beschikt het woongebouw over een gemeenschappelijk dakterras (lengte 8m en breedte 6,5m).
```

*Privé-buitenruimte*  
De woning van A beschikt over een privé-buitenruimte van 2m x 0,5m = 1m2. Dit resulteert in 2 punten + 0,35 punt x 1m2 = 2,35 punten.

*Gemeenschappelijke ruimte op hetzelfde adres*  
Op het adres van huurder A is een balkon van 3m x 1,5m = 4,5m2. Dit resulteert in 0,75 punt x 4,5m2 = 3,375 punt. Het balkon wordt gedeeld door vier onzelfstandige woonruimten op hetzelfde adres, dus 3,375 punt/4 = 0,84375 punt..

*Gemeenschappelijke ruimte gedeeld met meerdere adressen*  
Tot slot is er een dakterras van 8m x 6,5m = 52m2. Dit resulteert in 0,75 punt x 52m2 = 39 punten. Het dakterras wordt gedeeld door 5 adressen, dus 39 punten/5 = 7,8 punt. Op het adres van huurder A zijn vier onzelfstandige woonruimten, dus 7,8 punt/4 = 1,95 punt.

*Totaal*  
Voor huurder A resulteert dit in 2,35 punt + 0,84375 punt + 1,95 punt = 5,14375 punten, afgerond 5,25 punten.

## Rubriek 9 - Gemeenschappelijke binnenruimten gedeeld met meerdere adressen

### 9.1 Puntentoekenning

- Een gemeenschappelijk vertrek wordt gewaardeerd met 1 punt per vierkante meter.  
- Een gemeenschappelijke overige ruimte wordt gewaardeerd met 0,75 punt per vierkante meter.  
- Voorzieningen (verkoeling en verwarming, keuken, sanitair, gehandicaptenvoorziening) die zich bevinden in gemeenschappelijke vertrekken en overige ruimten worden gewaardeerd conform het woningwaarderingsstelsel.  

De punten worden gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft en vervolgens gedeeld door het aantal onzelfstandige woonruimten op dat adres.

> De rubriek gehandicaptenvoorziening is niet geimplementeerd in de woningwaardering package en zal dus ook niet berekend worden onder "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen"

~~**Warme maaltijden**  
Indien het verstrekken van warme maaltijden onderdeel vormt van de huurovereenkomst dan worden ook de aanwezige gemeenschappelijke (spoel)keuken en bijbehorende opslagruimte in de waardering meegenomen. Het gaat hier om de puntenwaardering van de oppervlakte van die ruimten.~~

**Gemeenschappelijke ruimten en voorzieningen in een zorgwoning**  
De ervaring leert dat bij het waarderen van de gemeenschappelijke ruimten en voorzieningen in een zorgwoning of woon/zorgcomplex de waardering per woning veelal uitkomt op een totaal van ongeveer 3 punten. Om arbeidsintensief meetwerk te voorkomen waardeert de Huurcommissie in dat geval voor de gemeenschappelijke ruimten en voorzieningen een waardering van 3 punten per woning.

### 9.2 Definitie gemeenschappelijke vertrekken en overige ruimten

Gemeenschappelijke vertrekken en overige ruimten zijn tot het woongebouw behorende binnenruimten waar de bewoners van tenminste twee adressen in het woongebouw volgens de huurovereenkomst exclusieve toegang en gebruiksrecht toe hebben. De huurder(s) moet(en) daarnaast toegang hebben tot de gemeenschappelijke binnenruimte zonder gebruikmaking van vertrekken, overige ruimten of verkeersruimten die uitsluitend ter beschikking staan aan de verhuurder of aan (een) andere huurder(s).

~~Uitgesloten zijn vertrekken en overige ruimten waarvoor ook door derden een vergoeding/huurprijs wordt betaald alsmede vertrekken en ruimten die door de eigenaar/verhuurder in gebruik zijn (bijv. kantoor- ruimte, opslagruimte, e.d.).~~

**Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:**

- ~~zij binnen het woongebouw liggen of tot de onroerende aanhorigheden behoren;~~
- ~~de vergoeding daarvoor in de huurprijs van de woning is begrepen;~~
- de oppervlakte, na deling door het aantal adressen, per woning minstens 2m2 bedraagt.

De toekenning van punten bij een gemeenschappelijke berging is als volgt: totale oppervlakte, afronden in m2, delen door het aantal adressen en waarderen als “overige ruimte”. Dat betekent dat kasten uitkomend in een verkeersruimte niet worden meegeteld.

Met vertrekken en overige ruimten wordt onder deze rubriek voor het overige aangesloten bij de definities en meetinstructies zoals toegelicht in paragraaf 1.3 en 2.3 van dit hoofdstuk.

> Wanneer het attribuut `gedeeld_met_aantal_eenheden` van een ruimte groter of gelijk aan 2 is, dan komt de ruimte in aanmerking voor een waardering onder "Gemeenschappelijke binnenruimten gedeeld met meerdere adressen", mits deze voldoet aan de criteria voor vertrekken of overige ruimten.

### 9.3 Rekenmethode en voorbeeldberekening

**Rekenmethode**

1. Bepaal of het een vertrek of een overige ruimte is en reken de oppervlaktepunten:  
  a. Gemeenschappelijke vertrekken worden met 1 punt per m2 gewaardeerd.  
  b. Gemeenschappelijke overige ruimten worden met 0,75 punt per m2 gewaardeerd.  
2. Bepaal de punten voor verkoeling en verwarming conform rubriek 3.  
3. Bepaal eventueel van toepassing zijnde extra punten conform rubriek 5, 6 en/of 7.  
4. Saldeer de punten uit de hierboven genoemde stappen.  
5. Deel dit aantal punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke binnenruimten.  
6. Deel het aantal punten door het aantal onzelfstandige woonruimten op dat adres.  


**Voorbeeld** 

```text
Voorbeeld: (A) een gemeenschappelijke binnenruimte met keuken van 20 vierkante meter, en daarnaast (B) een gedeeld toilet van 2 vierkante meter. Tot beiden hebben 4 adressen toegang. Op één van deze adressen zijn vier onzelfstandige woonruimten.

1. Vertrek A voldoet aan de eisen van een vertrek en wordt gewaardeerd met 20 x 1 punt (oppervlakte) conform rubriek 1. Ruimte B voldoet aan de eisen van een overige ruimte en wordt gewaardeerd met 1,5 (2 x 0,75) punt conform rubriek 2.  
2. Vertrek A is verwarmd middels een radiator en krijgt daarvoor 2 punten conform rubriek 3. Het toilet is onverwarmd en ontvangt daarvoor geen punten.  
3. In vertrek A wordt voldaan aan de minimumeisen van een keuken conform rubriek 5. Voor deze rubriek wordt 10 punten toegekend (7 voor het aanrecht, en 3 voor de voorzieningen). De toiletruimte B krijgt 4,75 punt (3,75 voor het hangend toilet en 1 voor de wastafel).  

4. Saldering levert op: 20 + 1,5 + 2 + 10 + 4,75 = 38,25  
5. Delen door het aantal adressen levert op: 38,25 punten/4 = 9.5625 per adres.  
6.Vervolgens wordt gedeeld door het aantal onzelfstandige woonruimten op het adres, dus 9,5625/4 = 2,390625 punten per onzelfstandige woonruimte.  

Afronden geschiedt op een kwart punt per onzelfstandige woonruimte, in dit geval dus op 2,50.
```

## Rubriek 10 - Gemeenschappelijke parkeerruimten 

### 10.1 Puntentoekenning

Voor verschillende typen gemeenschappelijke parkeerplekken, afhankelijk van afdekking van de buitenlucht, worden punten toegekend:

- **Type I**: parkeerplek in afgesloten parkeergarage behorende tot het complex krijgt **9 punten**.
- **Type II**: parkeerplek buiten behorende tot het complex of de woning met dak krijgt **6 punten**. Hieronder wordt ook begrepen een carport.
- **Type III**: parkeerplek buiten behorende tot het complex of de woning zonder dak krijgt **4 punten**.

> Onderstaande `Ruimtedetailsoorten` corresponderen met bovenstaande parkeerplek types:
> - Type I: `Ruimtedetailsoort.parkeervak_auto_binnen` met code `VAI`
> - Type II: `Ruimtedetailsoort.carport` met code `CAR`
> - Type III: `Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt` met code `VAU`

2 extra punten worden toegekend als de parkeerplek beschikt over een laadpaal voor elektrische rijden, exclusief voor gebruik door bewoners.

De punten worden gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft en vervolgens gedeeld door het aantal onzelfstandige woonruimten op dat adres.

Een gemeenschappelijke parkeerruimte is een ruimte die toegankelijk is voor bewoners van tenminste twee adressen die daar exclusief gebruiksrecht op hebben waarin zich tenminste één parkeerplek bevindt. De parkeerplek mag niet openbaar te gebruiken zijn, maar moet bij een complex of adres horen en in de huurovereenkomst moet exclusief gebruiksrecht zijn toegekend.

### 10.2 Definitie gemeenschappelijke parkeerruimte

Een gemeenschappelijke parkeerruimte is een ruimte die toegankelijk is voor bewoners van ten minste twee adressen die daar exclusief gebruiksrecht op hebben, waarin zich ten minste één parkeerplek bevindt (zoals een gemeenschappelijke parkeergarage onder een wooncomplex of een gemeenschappelijke parkeerplaats buiten met één of meer parkeerplekken). De parkeerplek mag niet openbaar te gebruiken zijn, maar moet bij een complex of adres horen en in de huurovereenkomst moet exclusief gebruiksrecht zijn toegekend.

Een parkeerruimte waartoe bewoners van één adres op grond van de huurovereenkomst exclusieve toegang hebben, wordt gewaardeerd volgens rubriek 2 (bijvoorbeeld een garagebox behorende tot de woning) of rubriek 8 (bijvoorbeeld een oprit exclusief behorende tot de woning).

> Volgens rubriek 10 in het beleidsboek zelfstandige woonruimten, geldt voor een parkeeruimte dat deze minimaal 12m2 moet zijn. deze eis wordt hier niet expliciet genoemd, maar er is vanuit gegaan dat deze eis ook geldt voor rubriek 10 in onzelfstandige woonruimten.

### 10.3 Onroerende aanhorigheid
> De woningwaardering package gaat uit van onderstaande eisen, wanneer een parkeeruimte wordt meegegeven in het input model.

Punten voor een parkeervoorziening worden alleen toegekend als deze als onroerende aanhorigheid gekwalificeerd wordt. Hiervan is sprake als de parkeervoorziening naar haar aard onlosmakelijk verbonden is met de woonruimte (bijvoorbeeld wanneer de parkeerplek direct in verbinding staat met de woonruimte of tot het adres of complex behoort, zoals bij een gemeenschappelijke oprit of gemeenschappelijke garage) of omdat de parkeervoorziening volgens verkeersopvatting onderdeel of krachtens de huurovereenkomst deel uitmaakt van de gehuurde woning.

Dit geldt als in de huurovereenkomst is afgesproken dat de parkeervoorziening tot de onroerende zaak behoort en de woonruimte en parkeerplaats verhuurd moeten zijn zonder dat ze van elkaar contractueel te scheiden zijn. Als de parkeerplek geen onroerende aanhorigheid betreft, heeft de verhuurder de mogelijkheid dit als los goed te verhuren volgens artikel 7:201 BW.

### 10.4 Rekenmethode en voorbeeldberekening

**Rekenmethode**

1. Bepaal tot welk type de parkeerplek(ken) horen.
2. Indien er sprake is van een laadpaal voor exclusief gebruik door de bewoners, geldt twee punten extra per parkeerplek met laadpaal.
3. Bij meerdere parkeerplekken worden de punten bij elkaar opgeteld.
4. Daarna wordt dit puntentotaal gedeeld door het aantal adressen dat gebruik kan maken van de parkeerplek(ken). Indien sprake is van een privéparkeerplek voor één adres, wordt gedeeld door 1.
5. Tot slot wordt dit puntentotaal gedeeld door het aantal onzelfstandige woonruimten op het adres.

**Voorbeeldberekening**
```text
In een woongebouw bevinden zich tien adressen. Op één van deze adressen zijn vier onzelfstandige woonruimten. Huurder A huurt één van deze onzelfstandige woonruimten. Bij het woongebouw horen vijf Type-III parkeerplaatsen.

1. De vijf parkeerplekken behoren tot Type III.
2. Geen laadpaal is aanwezig.
3. De vijf parkeerplaatsen leveren 5 × 4 = 20 punten op.
4. De parkeerplaatsen worden gedeeld door tien adressen, dus 20 / 10 = 2 punten per adres.
5. Op het adres van A zijn vier onzelfstandige woonruimten, dus voor A resulteert dit in 2 / 4 = 0,50 punt in de rubriek parkeerruimte.
```

> Omdat de woningwaardering package op eenheidniveau de punten voor het woningwaarderingstelsel berekent, is het niet mogelijk om `Ruimtedetailsoort.parkeergarage` en `Ruimtedetailsoort.parkeerterrein` te waarderen. Deze twee ruimtedetailsoorten maken bovenstaande berekening, waarbij de verschillende types geteld worden, met het huidige VERA-model niet mogelijk. Om punten te krijgen voor deze rubriek moeten de type parkeervakken los worden ingeschoten. Daartoe is het attribuut `Eenhedenruimte.aantal` als uitbreiding op het VERA-model toegevoegd. Hierdoor is het mogelijk om aan te geven tot hoeveel van bovenstaande parkertypes de eenheid toegang heeft zonder dat elk parkeervak van een parkeergarage of parkeerterrein meegegeven dient te worden. Daarnaast zijn ook `Eenhedenruimte.gedeeld_met_aantal_eenheden` en `Eenhedenruimte.gedeeld_met_aantal_onzelfstandige_woonruimten` als uitbreiding toegevoegd. Deze attributen dienen ook op elk type parkeerplek meegegeven te worden wanneer het een onzelfstandige woonruimte betreft. Om bovenstaand rekenvoorbeeld door de woningwaardering package te laten berekenen, kunnen de gemeenschappelijke parkeerplekken als volgt (in JSON-formaat) meegegeven worden.


```json
{
  "id": "A",
  "ruimten": [
    {
      "id": "1",
      "aantal": 5,
      "gedeeld_met_aantal_eenheden": 10,
      "gedeeld_met_aantal_onzelfstandige_woonruimten": 4,
      "soort": {
        "code": "PAR",
        "naam": "Parkeergelegenheid"
      },
      "detailSoort": {
        "code": "VAU",
        "naam": "Parkeervak auto (buiten, niet overdekt)"
      },
      "naam": "Parkeervak buiten",
      "oppervlakte": 12,
      "breedte": 3,
      "lengte": 4
    }
  ]
}
```

## Rubriek 11 Punten voor de WOZ-waarde

Punten worden toegekend op basis van de WOZ-waarde van het adres waar de onzelfstandige woonruimte onderdeel van is. WOZ staat voor Wet waardering onroerende zaken. De WOZ-waarde geeft de geschatte marktwaarde van de woning weer zoals volgt uit de Wet waardering onroerende zaken. Deze waarde wordt in principe ieder kalenderjaar door de gemeente vastgesteld, die in de WOZ-beschikking van de desbetreffende woning wordt weergegeven.

De waardepeildatum van de WOZ-waarde ligt op 1 januari van twee kalenderjaren voorafgaand. Ter illustratie: de WOZ-waarde in de WOZ-beschikking van 2024 heeft een waardepeildatum van 1 januari 2022.

> Hier staat een fout in het beleidsboek. Dit moet zijn: Ter illustratie: de WOZ-waarde in de WOZ-beschikking van **2023** heeft een waardepeildatum van 1 januari 2022.

### 11.1 Puntentoekenning

De puntentoekenning is als volgt.

- 14 punten wanneer de WOZ-waarde per m2 gebruiksoppervlakte **meer dan 10%** hoger is dan de gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van de woningen in het COROP-gebied waarbinnen de woning is gelegen.
- 12 punten wanneer de WOZ-waarde per m2 gebruiksoppervlakte **maximaal 10% hoger of lager** is dan de gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van de woningen in het COROP-gebied waarbinnen de woning is gelegen.
- 10 punten wanneer de WOZ-waarde per m2 gebruiksoppervlakte **meer dan 10% lager is** dan de gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van de woningen in het COROP-gebied waarbinnen de woning is gelegen.

Punten worden bepaald aan de hand van de gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van woningen in het COROP-gebied, zoals in bijlage 3 is weergegeven. Deze gemiddelden worden elk jaar, met ingang van 1 januari, aangepast met de gemiddelde wijziging van de eigenwoningwaarden van elk COROP-gebied. In de Uitvoeringsregeling huurprijzen woonruimte zijn de COROP-gebieden weergegeven alsmede de daarbij behorende gemiddelde WOZ-waarde per m2 gebruiksoppervlakte van woningen. In deze regeling zijn twee verschillende kolommen weergegeven: één voor de gemiddelden waar nog geen nieuwe WOZ-beschikking voor is afgegeven en één voor de gemiddelden waar wel een nieuwe WOZ-beschikking is afgegeven. De kolommen geven op basis van de peildatum van de WOZ-beschikking weer met welk bedrag moet worden gerekend.'

> Het COROP-gebied wordt bepaald op basis van de woonplaatscode van de woonplaats waarin de eenheid zich bevindt. Hiervoor dient de BAG-woonplaatscode in het attribuut `code` van de woonplaats op het adres van de eenheid gespecificeerd te zijn. Indien dit attribuut niet gespecificeerd is, wordt op basis van postcode, huisnummer, huisletter en huisnummertoevoeging bepaald in welke woonplaats een eenheid zich bevindt. Hierbij is het van belang dat deze waarden overeenkomen met de BAG-registratie.

Onder gebruiksoppervlakte in deze rubriek wordt verstaan: de oppervlakte van een verblijfsobject in gehele vierkante meters als bedoeld onder “kenmerken”, te vinden per woning op de officiële site van het WOZ-waardeloket. Het gaat hierbij op de gebruiksoppervlakte van de gehele woning (het adres) waarvan de onzelfstandige woonruimten onderdeel uitmaken.

> Deze waarde dient gespecificeerd te worden in het attribuut `adresseerbaar_object_basisregistratie.bag_gebruikers_oppervlakte` op de eenheid.

_Rekenvoorbeeld:_

_De WOZ-waarde van een woning met peildatum 1 januari 2022 is vastgesteld op € 250.000. De woning, waarvan de onzelfstandige woonruimte deel uitmaakt, is gelegen in Amsterdam en heeft een gebruiksoppervlakte van 40 m2._

_De gemeente Amsterdam ligt in het COROP-gebied Groot-Amsterdam dat € 5.596 als gemiddelde WOZ-waarde per vierkante meter heeft. De WOZ-waarde per m2 gebruiksoppervlakte van de woning betreft € 6.250 (250.000 gedeeld door 40). Dit bedrag is 11,69% hoger dan de gemiddelde WOZ-waarde per vierkante meter van het COROP-gebied Groot-Amsterdam. Gelet hierop worden 14 punten aan de onzelfstandige woonruimte toegekend aangezien de WOZ-waarde per m2 gebruiksoppervlakte meer dan 10% hoger is dan de gemiddelde WOZ-waarde per m2 in gebruiksoppervlakte het COROP-gebied Groot-Amsterdam._

### ~~11.2 Ontbreken WOZ-waarde en minimumwaarde~~

~~Als geen WOZ-waarde bekend is, kan als alternatief 85% van de taxatiewaarde van de woning worden gebruikt volgend uit een door een Register-Taxateur opgesteld (hybride)taxatierapport. De verhuurder draagt de verantwoordelijkheid voor het opstellen van dit rapport. De taxatiewaarde geldt totdat een WOZ-waarde is vastgesteld en vervalt voor toepassing van deze rubriek. Als de verhuurder geen taxatierapport heeft aangeleverd dan geldt de minimum WOZ-waarde.~~

> Als er geen WOZ-waarde beschikbaar is, maar wel een taxatiewaarde, dient 85% van deze taxatiewaarde als invoer voor de WOZ-waarde gebruikt te worden.

**Minimumwaarde**

De minimum WOZ-waarde wordt ook gebruikt voor specifieke woningen van specifieke verhuurders, zoals ‘containerwoningen’ die zijn bestemd voor studentenhuisvesting. In die gevallen wordt een minimum WOZ-waarde gehanteerd indien de WOZ-waarde lager is dan deze minimumwaarde. Deze waarde met peildatum 1 januari 2023 bedraagt € 73.607. Zie de tabel hieronder voor de minimumwaarde van de afgelopen jaren.

Tabel 1
| Peildatum | Minimumwaarde |
| ------------------ | -------- |
| Per 1 januari 2021 | € 61.198 |
| Per 1 januari 2022 | € 71.602 |
| Per 1 januari 2023 | € 73.607 |
| Per 1 januari 2024 | € 77.582 |

**~~Tijdelijke woning~~**

~~In geval van een tijdelijke woning hanteert de register-taxateur de objectafbakeningsvoorschriften en waarderingsvoorschriften van hoofdstuk III van de Wet WOZ met uitzondering van de voorschriften op grond van artikel 17, vierde lid, en artikel 18, eerste en tweede lid, van de Wet WOZ. In plaats van de voorschriften van artikel 18, eerste en tweede lid, gaat de register-taxateur uit van de staat van de woning na oplevering.~~

~~Onder tijdelijke woning wordt voor deze rubriek een woning verstaan die voor een bepaalde tijd op een tijdelijke locatie (met toegelaten functie wonen of tijdelijke afwijking Omgevingsplan) mogen worden gebouwd. Dit zijn woningen die voldoen aan de eisen die gelden voor nieuwbouw óf die getoetst zijn aan tijdelijke woningen zoals gedefinieerd in het Besluit bouwwerken leefomgeving (termijn van ten hoogste 15 jaar).~~

### ~~11.3 Gebouwd eigendom in aanbouw~~

~~Indien de WOZ-waarde betrekking heeft op een ‘gebouwd eigendom in aanbouw’, als bedoeld in artikel 17 lid 4 Wet WOZ, dan wordt voor de puntentoekenning uitgegaan van de waarde van de woning als ware de bouw voltooid. De WOZ-beschikking zal het voortgangspercentage vermelden. De Huurcommissie heeft dan tot taak de WOZ-waarde gerelateerd aan de voortgang van de aanbouw om te rekenen naar de waarde “als ware de bouw voltooid”, dus naar 100%.~~

~~Onder een ‘gebouwd eigendom in aanbouw’ wordt verstaan een onroerende zaak of gedeelte daarvan waarvoor een omgevingsvergunning is verleend en die door bouw nog niet geschikt is voor gebruik overeenkomstig haar beoogde bestemming. Het gaat hier om de situatie waarbij nieuwbouw/verbouw is begonnen na 1 januari van een lopend jaar en die niet is afgerond voor 1 januari van het daaropvolgende jaar.~~

~~Hiervan is bijvoorbeeld sprake als, in het kader van de WOZ-beschikking 2023 dat als peildatum 1 januari 2022 heeft, de werkzaamheden aan het gehuurde zijn aangevangen na 1 januari 2022 en zijn voltooid ná 1 januari 2023. De WOZ-beschikking 2024, dat als peildatum 1 januari 2023 heeft, zal in dat geval niet de waarde weergeven “als ware de bouw voltooid”. In dat geval kan de woning worden aangemerkt als ‘een gebouwd eigendom in aanbouw’ als bedoeld in artikel 17 lid 4 Wet WOZ en moet de Huurcommissie de waarde omrekenen naar 100%.~~

> De omrekening naar 100% voortgangspercentage dient als WOZ-waarde opgegeven te worden.

## Rubriek 12 - Bijzondere voorzieningen: zorgwoning

### 12.1 Zorgwoning

Als sprake is van een zorgwoning, dan wordt het puntentotaal van de rubrieken 1 tot en met 11 van het woningwaarderingsstelsel met 35% verhoogd. Dit resulteert in een hogere maximale huurprijs.

> De onderstaande doorgehaalde voorwaarden worden niet gecontroleerd door de woningwaardering package. Wanneer een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als zorgwoning gewaardeerd.

**~~Voorwaarden zorgwoning~~**

~~Er is sprake van een zorgwoning als aan de volgende vijf voorwaarden is voldaan.~~

1. **~~De zorgwoning betreft een onzelfstandige woonruimte~~**  
   Hoe het begrip onzelfstandige woonruimte door de Huurcommissie wordt ingevuld is te vinden in paragraaf 2.3.1 van dit beleidsboek.
2. **~~De onzelfstandige woonruimte is gelegen in een woongebouw~~**
3. **~~De woning en het woongebouw waarin de woning is gelegen zijn bestemd voor mensen met een fysieke beperking~~**  

~~Dat de woning en het woongebouw bestemd zijn voor mensen met een fysieke beperking moet in ieder geval blijken uit a) drempelloze toegankelijkheid en b) doorgankelijkheid.~~

~~Deze drempelloze toegankelijkheid en doorgankelijkheid houden tenminste in dat alle gangen, waar de bewoners doorheen moeten om de eigen woning en andere relevante (gemeenschappelijke) ruimten in het woongebouw te bereiken, een minimale breedte hebben van 1,2 m. Bovendien moet er sprake zijn van een lift of hellingbaan indien de eigen woning en andere relevante ruimten drempels hebben van 2 cm of hoger.~~

4. **~~De huurovereenkomst\* van de woning voorziet op de aanwezigheid van technische voorzieningen in het gebouw die het mogelijk maken dat een individuele persoonsalarmering verbinding kan maken met de noodalarmcentrale in zowel de woning als het complex waarvan de woning deel uitmaakt.~~**  
   
~~Het woongebouw moet zodanig zijn uitgerust dat een afgegeven persoonsalarm door individuele persoonsalarmering overal verbinding kan maken met de noodalarmcentrale in zowel de woning als het complex waarvan de woning deel uitmaakt. Het moet dus bijvoorbeeld ook mogelijk zijn, dat de uitrusting in het gebouw in staat moet zijn om een persoonsalarm op te vangen indien dat uit de lift van het complex wordt verzonden, of uit de tot het complex behorende buitenruimte.~~

~~Voorbeelden van technische voorzieningen zijn een noodoproepinstallatie of een persoonlijk alarmsysteem dat op de persoon wordt gedragen met een halskoord.~~

5. **~~De huurovereenkomst\* van de woning moet zien op het gebruik van gemeenschappelijke ruimten voor maaltijden of recreatie~~**  

~~Het gebruik van gemeenschappelijke ruimten voor maaltijden of recreatie moet deel uit maken van een huurovereenkomst om een woning als zorgwoning te kunnen kwalificeren in de zin van het Besluit huurprijzen woonruimte. Deze ruimten dienen tot het woongebouw te behoren of als onroerende aanhorigheid van het complex te kunnen worden aangemerkt. Het exclusieve gebruik van deze ruimten door de huurders van het woongebouw is geen vereiste. Wel dienen de ruimten primair ter beschikking te staan van de huurders van het woongebouw.~~

~~Als de gemeenschappelijke ruimten voor maaltijden of recreatie niet binnen hetzelfde maar geheel of gedeeltelijk in een naastgelegen (woon)gebouw zijn gelegen, dienen deze voorzieningen binnendoor (gesloten loopbrug, corridor, etc.) bereikbaar te zijn om als zorgwoning in de zin van het Besluit huurprijzen woonruimte te kwalificeren.~~

~~\* Indien sprake is van een gemengde woon-zorgovereenkomst dan is het woningwaarderingsstelsel, waaronder de toeslag die geldt bij een zorgwoning, alleen van toepassing indien het huurelement in de gemengde overeenkomst overheerst.~~

### 12.2 Aanbelfunctie met video- en audioverbinding

Een aanbelfunctie met video- en audioverbinding waarbij de voordeur automatisch kan worden geopend vanuit de woning wordt gewaardeerd met 0,25 punt.

Hieronder wordt een systeem verstaan dat tweewegcommunicatie mogelijk maakt met beeld en geluid tussen degene die aanbelt en een aanwezige in de woonruimte. Daarbij dient er tevens sprake te zijn van de mogelijkheid tot het openen van de (gemeenschappelijke) voordeur vanuit de woonruimte (op afstand) die toegang geeft tot het complex waarvan de woning onderdeel uitmaakt.

### 12.3 Laadpalen

Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik door de bewoners, wordt gewaardeerd met 2 punten. Dit geldt alleen als de laadpaal bestemd is voor het elektrisch opladen van een gemotoriseerd voertuig, niet zijnde een bromfiets, fiets met trapondersteuning of gehandicaptenvoertuig.

In geval een gemeenschappelijke parkeerruimte beschikt over een laadpaal, wordt voor de berekeningswijze aangesloten bij Rubriek 10.

## Rubriek 13 - Aftrekpunten

Het waarderingsstelsel voor onzelfstandige woonruimten kent een rubriek voor aftrekpunten. Een aftrek van 4 punten wordt toegepast in ieder van de volgende situaties:

- Wanneer de totale oppervlakte van vertrekken onder rubriek 1 minder is dan 8 m2.
- ~~Als de verhuurder van de onzelfstandige woonruimte zijn hoofdverblijf heeft in de woning waarvan de onzelfstandige woonruimte onderdeel uitmaakt en de onzelfstandige woonruimte of het sanitair waartoe de huurder toegang en gebruiksrecht heeft, uitsluitend via een woon- of slaapvertrek van de verhuurder te bereiken is.~~
- ~~Bij een ruitoppervlakte in het (hoofd)woonvertrek van minder dan 0,75 m2.~~
- ~~Wanneer het laagste raamkozijn van het (hoofd)woonvertrek meer dan 1,60 m boven de vloer is.~~

~~Bij de bepaling van de ruitoppervlakte van het (hoofd) woonvertrek is de oppervlakte van het zichtbare glas bepalend. Dit betekent dat het glas dat zich in de sponning bevindt niet bijdraagt aan het bepalen van de ruitoppervlakte.~~

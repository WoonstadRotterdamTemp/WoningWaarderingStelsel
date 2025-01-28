# Hoofdstuk 2 - Algemene toelichting

## 2.7 Afronding punten, eindsaldering

_Afronding per rubriek_

De waardering in punten wordt per rubriek na saldering afgerond op 0,25 punt waarbij een achtste (1/8) punt naar boven wordt afgerond. Dat wil zeggen dat 0,125 wordt afgerond naar 0,25. Een kwartpunt is de kleinst werkbare waardering binnen het woningwaarderingsstelsel voor een afzonderlijke rubriek. Voor een voorbeeld zie paragraaf 9.3.

_Eindsaldering_

Het puntentotaal per woning wordt na eindsaldering (met inbegrip van de bij zorgwoningen geldende toeslag) afgerond op hele punten. Bij 0,5 punten of meer wordt afgerond naar boven op hele punten, bij minder dan 0,5 punten wordt afgerond naar beneden op hele punten. In de eindsaldering zitten ook de punten voor eventuele gemeenschappelijke ruimten en voorzieningen.

**N.B. Alle punten worden bij elkaar opgeteld inclusief de punten voor de gemeenschappelijke ruimten en voorzieningen, waarna wordt afgerond. De toeslag van 35% bij zorgwoningen wordt toegepast op het puntentotaal van de onderdelen 1 t/m 11 en pas daarna afgerond.**

_Meer dan 250 punten_

In geval van een woonruimte met méér dan 250 punten wordt de maximale huurprijs als volgt berekend: elk punt boven de 250 wordt vermenigvuldigd met het verschil tussen de bedragen, genoemd in de huurprijstabel (zie [bijlage 5](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken_html/waarderingsstelsel-zelfstandige-woonruimte/bijlage-5)) bij 249 en 250 punten. Het verkregen bedrag wordt vervolgens opgeteld bij de maximale huurprijs die volgens de huurprijstabel behoort bij 250 punten.

**Voorbeeld:**

Een zelfstandige woning wordt beoordeeld met 255 punten. Bij een puntenaantal van 250 hoort een maximale huurprijs van € 1.572,20 (prijspeil 1 juli 2024). Het puntenaantal voor de woning ligt echter vijf punten hoger. Dit verschil van vijf punten dient te worden vermenigvuldigd met het verschil tussen de bedragen die correspondeerden met 249 en 250 punten. Dat verschil bedraagt (€ 1.572,20 - € 1.565,73 =) € 6,47. De verhoging op de maximale huurprijs is in dit geval € 32,35 (€ 6,47 x 5). De maximale huurprijs bedraagt dus € 1.604,55 (€ 1.572,20 + € 32,35).

## 2.8 Prijsopslag monumenten en nieuwbouw

De punten die worden berekend op basis van het woningwaarderingsstelsel resulteren in een maximale huurprijs. Het waarderingsstelsel kent de mogelijkheid van een opslag bovenop deze maximale huurprijs voor monumenten en voor nieuwbouw. Als meerdere opslagen van toepassing zijn, worden deze percentages bij elkaar opgeteld alvorens daarmee de huurprijs wordt vermeerderd.

Deze opslagen blijven buiten beschouwing voor het antwoord op de vraag tot welke sector (sociale sector, middensector of vrijehuursector) de woonruimte behoort.

### 2.8.1 Rijksmonument

_Huurovereenkomst afgesloten op of na 1 juli 2024_

Indien een woonruimte bestaat uit of deel uitmaakt van een rijksmonument, als bedoeld in artikel 1.1 Erfgoedwet, dan wordt de maximale huurprijs vermeerderd met 35%. Hiermee worden rijksmonumenten bedoeld die zijn geregistreerd in het monumentenregister van de Rijksdienst voor het Cultureel Erfgoed.

Deze prijsopslag geldt alleen voor huurovereenkomsten die zijn afgesloten op of na het tijdstip van inwerkingtreding van de Wet betaalbare huur: vanaf 1 juli 2024. Als de huurovereenkomst is afgesloten vóór 1 juli 2024 dan geldt onderstaande waardering.

De Huurcommissie hanteert passief beleid. De verhuurder moet aantonen dat een woning bestaat of deel uitmaakt van een rijksmonument.

_Huurovereenkomst afgesloten vóór 1 juli 2024_

Indien een woonruimte een rijksmonument is of daar deel van uitmaakt, als bedoeld in artikel 1.1 Erfgoedwet, dan worden 50 punten extra toegekend. Hiermee worden rijksmonumenten, en dus niet gemeentelijke of provinciale monumenten, bedoeld die zijn geregistreerd in het monumentenregister van de Rijksdienst voor het Cultureel Erfgoed. Alleen deze monumenten krijgen een toeslag van 50 punten.

Het Rijksmonumentenregister kan door eenieder worden geraadpleegd. Het register bevat gegevens over de inschrijving en ter identificatie van de rijksmonumenten: [http://monumentenregister.cultureelerfgoed.nl](http://monumentenregister.cultureelerfgoed.nl/).

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

### 2.8.2 Gemeentelijk of provinciaal monument

Indien een woonruimte een gemeentelijk of provinciaal monument is of daarvan deel uitmaakt, dan wordt de maximale huurprijs vermeerderd met 15%. Het gemeentelijk monument moet zijn aangewezen door het college van burgemeester en wethouders. Een provinciaal monument moet zijn aangewezen door de gedeputeerde staten.

De Huurcommissie hanteert passief beleid. De partijen moeten aantonen dat een woning bestaat of deel uitmaakt van een gemeentelijk of provinciaal monument.

### 2.8.3 Beschermd stads- of dorpsgezicht

De maximale huurprijs wordt met 5% vermeerderd als:

*   a. de woonruimte behoort tot een rijksbeschermd stads- of dorpsgezicht als bedoeld in artikel 2.34. vierde lid, van de Omgevingswet;
*   b. de woonruimte behoort tot een woning die is gebouwd voor 1965; en
*   c. de woonruimte niet bestaat uit of deel uitmaakt van een rijksmonument als bedoeld in artikel 1.1 van de Erfgoedwet of van een door het college van burgemeester en wethouders aangewezen gemeentelijk monument of een door gedeputeerde staten aangewezen provinciaal monument.

De Huurcommissie hanteert voor beschermde stads- en dorpsgezichten een passief beleid. Dit betekent dat het aan de verhuurder is om aan te tonen dat de woonruimte aan de voorwaarden voor deze prijsopslag voldoet.

### 2.8.4 Nieuwbouwopslag

De maximale huurprijs die hoort bij de kwaliteit van een huurwoning uit de middensector (zie paragraaf 2.2), wordt met 10% vermeerderd als:

*   de woning voor het eerst in gebruik wordt genomen na 1 juli 2024, en
*   de start van de nieuwbouw, transformatie of bijbouw van de woning plaatsvindt vóór 1 januari 2028.

> In tegenstelling tot de VERA-definitie van `inExploitatiedatum` gebruiken wij voor ons inputmodel `inExploitatiedatum` als de datum van de _eerste_ ingebruikname. Zie: https://github.com/woonstadrotterdam/woningwaardering/issues/105

Hieronder wordt nadere uitleg gegeven over de begrippen nieuwbouw, transformatie en bijbouw:

1.  Nieuwbouw houdt in dat een volledig nieuw pand met nieuwe woonruimten neergezet wordt. In dit geval kan de start van de bouw van het gebouw, zoals ook in de Basisadministratie Adressen en Gebouwen (BAG) is terug te vinden, gebruikt worden.
2.  Transformatie betekent dat een nieuwe woonruimte ontstaat door een functiewijziging van een bestaand verblijfsobject. Een voorbeeld is een transformatie van een winkelruimte of kantoorruimte naar een woonruimte.
3.  Bijbouw betekent dat al sprake is van bebouwing waarbij geheel nieuwe woningen worden bijgebouwd. Bijvoorbeeld middels optoppen (dus bovenop de bestaande woning) of door nieuwe woningen tegen de bestaande bebouwing aan te bouwen.

De nieuwbouwopslag eindigt na 20 jaar, gerekend vanaf het moment van ingebruikname van de woonruimte.

De nieuwbouwopslag geldt ook na bewonerswissel.

In geval van opsplitsen van woningen (woningvormen) wordt geen opslag gerekend. In dat geval wordt namelijk geen woonruimte (m2) toegevoegd.

De nieuwbouwopslag geldt alleen voor woningen die op basis van de punten van het woningwaarderingsstelsel in de middensector horen. Geldt bijvoorbeeld voor een woning met 147 kwaliteitspunten een maximum huurprijs van € 905,50, dan kan de verhuurder een huurprijs vragen tot maximaal € 996,05. Door de nieuwbouwopslag kan een middeldure huurwoning echter nooit in de vrije sector terecht komen. De kwalificatie van de woning als een woning behorend tot het middensector verandert daardoor dus niet. Een woning van 186 punten of minder met een nieuwbouwopslag blijft dus een gereguleerde huurwoning uit het middensector. De opslag geldt voor het bedrag en niet voor de hoeveelheid punten.

_Cumulatie van opslagen_

De samenloop van verschillende opslagen is in beperkte mate mogelijk. Zo kunnen de monumentenopslag (zowel de Rijksmonumenten als provinciale en gemeentelijke monumenten) en de opslag voor een beschermd stads- of dorpsgezicht niet tegelijkertijd voor dezelfde woonruimte worden toegekend (zie art. 8 lid 5 onder c Besluit huurprijzen woonruimte).

Wel mogelijk is het cumulatief toekennen van de monumentenopslag of de opslag voor beschermd stad- of dorpsgezicht met de nieuwbouwopslag. Vereist is dan wel dat aan alle vereisten van de beide opslagen – dus ieder voor zich -  is voldaan. Naar verwachting komt deze situatie in de praktijk dan ook niet vaak voor.

**Bewijsstukken**

De verhuurder moet aantonen dat de woning voldoet aan de voorwaarden van de nieuwbouwopslag. De verhuurder dient hierbij, indien mogelijk, gebruik te maken van de gegevens die geregistreerd staan in de registratie in de BAG. Zo wordt bij nieuwbouw in de BAG ‘bouw gestart’ en de praktische ingebruikname per pand geregistreerd. Deze datum kan gebruikt worden om bij de nieuwbouwwoning aan te tonen dat de start van de bouw van de woonruimte voor 1 januari 2028 lag. Indien de BAG ontoereikend is, moet de verhuurder andere bewijsstukken aanleveren waaruit blijkt dat de woning voldoet aan bovenstaande voorwaarden. In een geval van een transformatie wordt de gemeente hierover geïnformeerd en kan de verhuurder bijvoorbeeld de benodigde informatie over de transformatie bij de gemeente opvragen.

# Hoofdstuk 3 - De rubrieken van het woningwaarderingsstelsel zelfstandige woning

Het woningwaarderingsstelsel zelfstandige woning kent punten toe aan een aantal hierna te bespreken aspecten, die we hierna verder ‘rubrieken’ noemen. De totaaltelling van die punten leidt tot een waardering van de woning, de maximale huurprijs. Over deze maximale huurprijs kan, indien aan de daarvoor geldende voorwaarden is voldaan, een opslag worden berekend om tot de huurprijs te komen. Deze rubrieken komen in dit hoofdstuk aan de orde.

**Inleiding**
De onderdelen die in de puntentelling betrokken moeten worden, zijn divers van aard. Voor de in aanmerking te nemen zogenoemde vertrekken en overige ruimten begint de puntentelling met de oppervlakte van deze twee onderdelen. Op welke wijze de oppervlakte moet worden berekend komt in dit hoofdstuk aan de orde.

Vervolgens komen de voorzieningen aan bod, zoals verkoeling en verwarming, een keuken en/of sanitaire voorzieningen die zijn gesitueerd in vertrekken of overige ruimten.

Twee andere rubrieken zijn de WOZ-waarde van de woonruimte en de energieprestatie. Deze worden betrokken bij de puntentelling, maar staan dus los van vertrekken of overige ruimten.

De overige rubrieken van het woningwaarderingsstelsel zijn woonvoorzieningen voor gehandicapten, buitenruimte, gemeenschappelijke ruimten en voorzieningen, parkeerruimte en bijzondere voorzieningen.

## Rubriek 1 Oppervlakte van vertrekken

### 1.1 Puntentoekenning

Vertrekken worden gewaardeerd met 1 punt per vierkante meter.

### 1.2 Wat zijn vertrekken?

> De gespecificeerde ruimtesoort is leidend bij de waardering van een ruimte. Een ruimte dient `Ruimtesoort` `vertrek` te hebben om in aanmerking te komen voor een waardering in de rubriek 'Oppervlakte van vertrekken'.
>
> Een ruimte dient alleen als vertrek gespecificeerd te worden wanneer deze voldoet aan alle onderstaande eisen. De doorgehaalde eisen worden niet door het systeem gecontroleerd.
>
> Wanneer een ruimte met `Ruimtesoort` `vertrek` niet voldoet aan de minimale oppervlakte, wordt er gekeken of de ruimte gewaardeerd kan worden onder de rubriek 'Oppervlakte van overige ruimten'.

Een ruimte wordt als vertrek gewaardeerd als deze voldoet aan de volgende eisen:

* ~~de vloer moet begaanbaar zijn;~~
* ~~de muren/wanden dienen uit 'vast' materiaal te bestaan;~~
* ~~de ruimte dient over tenminste 80% van de lengte (de langste zijde) ten minste 1,50 m breed te zijn;~~
* de ruimte dient een oppervlakte te hebben van minimaal 4 m2;
* ~~de ruimte dient over ten minste 50% van de oppervlakte of over een oppervlakte van 11 m2 een vrije hoogte te hebben van ten minste 2,10 m (gemeten vanaf de vloer tot het zichtbare plafond (onder het zichtbare plafond aanwezige balken blijven buiten de meting);~~
* ~~de ruimte dient te zijn voorzien van minimaal 0,5 m2 aan de buitenlucht grenzend transparant oppervlak (bijvoorbeeld een raam of deur met vensters);~~
* ~~de ruimte dient te beschikken over direct met de buitenlucht verbonden ventilatie;~~
* ~~er moet ten minste één stopcontact en één lichtpunt aanwezig zijn.~~

Voorbeelden van vertrekken zijn onder andere de woonkamer, een hobbykamer, studeerkamer, slaapkamer en eetkamer, op voorwaarde dat aan de hierboven gestelde eisen wordt voldaan.

In afwijking van bovengenoemde eisen is een ruimte die uitsluitend als keuken, badkamer of doucheruimte bestemd is altijd een vertrek.

Van de minimumoppervlakte zoals hiervoor genoemd kan niet worden afgeweken. Heeft de ruimte bijvoorbeeld een oppervlakte van 3,5 of 3,85 m2, dan wordt niet aan de gestelde eis van minimaal 4 m2 voldaan. De oppervlakte mag niet naar boven worden afgerond waardoor invulling aan de eis zou zijn gegeven.

_Zolderruimte_
Voor zolderruimten gelden, naast bovengenoemde eisen, nog twee eisen om als vertrek gewaardeerd te worden. De zolderruimte moet namelijk bereikbaar zijn via een vaste trap ~~en het dak moet beschoten zijn~~.

### 1.3 Meetinstructies

> De woningwaardering package gaat er vanuit dat de gebruiker zich houdt aan onderstaande meetinstructies voor vertrekken. Met uitzondering van _Kasten_ kunnen de meetinstructies niet getoets of berekend worden op basis van het VERA model.

In de toelichting op het woningwaarderingsstelsel is een aantal meetinstructies meegegeven:

#### 1\. Binnenmaatse meting

~~Meting van de oppervlakte van vertrekken vindt plaats van muur tot muur, op een hoogte van 1,50 m boven de vloer, inclusief de oppervlakte van alle tot de woning behorende losse en vaste kasten. Deze meethoogte geldt ook als de oppervlakte afwijkt van die op vloerniveau.~~

De Huurcommissie hanteert hierbij de volgende uitgangspunten.

~~_Pui, erker en entresol_~~
~~Als er sprake is van een pui wordt de binnenzijde van die pui (het kozijn) genomen. Een erker wordt meegerekend indien deze inwendig een vrije hoogte heeft van ten minste 1,50 m. Indien er sprake is van een zgn. entresol (tussenverdieping) dan dient de oppervlakte onder en/of boven deze entresol te worden meegerekend, indien de vrije hoogte ten minste 1,50 m bedraagt. Voor het meten van vertrekken die met elkaar in open verbinding staan, zie hierboven paragraaf 2.5.~~

_Kasten_
De Huurcommissie leest de zinsnede uit de toelichting 'alle tot de woning behorende losse en vaste kasten' als: 'alle tot de vertrekken behorende kasten'. **De plaats van de deur van de kast** bepaalt bij welk vertrek de kast behoort. Dus een kast die in een vertrek uitkomt wordt, ongeacht de afmeting, bij dat vertrek geteld. Dat geldt ook voor het waarderen van een kastenwand tussen twee vertrekken.

* van vaste kasten wordt de netto oppervlakte bepaald en bij de oppervlakte van het betreffende vertrek opgeteld;
* een kast, waarvan de deur uitkomt op een verkeersruimte, wordt niet gewaardeerd;
* ~~losse kasten zijn niet van belang bij het meten. De oppervlakte van het vertrek wordt bepaald, incl. de oppervlakte die wordt ingenomen door een losse kast.~~

#### ~~2\. Hellend of verlaagd plafond~~

~~Als oppervlakte van een vertrek met een (ten dele) hellend of verlaagd plafond geldt dat alleen het gedeelte van de ruimte waarboven het plafond ten minste 1,50 m hoog is, wordt meegeteld bij de berekening van de oppervlakte.~~

~~De Huurcommissie eist in geval van een (ten dele) hellend plafond dat de 1,50 m hoogte loopt tot het dakbeschot of tot het zichtbare dakvlak of plafond. Met gordingen en balken wordt bij de meting geen rekening gehouden.~~

#### ~~3\. Vloeroppervlakte onder aanrecht, keukentoestel, wasbak en installaties~~

~~De vloeroppervlakte onder aanrechten, toestellen in de keuken, badkuip, lavet of douchebak, moederhaard, cv-ketel, boilerinstallatie en radiatoren wordt meegeteld.~~

~~Indien zich in een vertrek, of in een kast in een vertrek, een gas- en/of elektrameter bevindt, dan wordt de oppervlakte gewaardeerd onder aftrek van 30 x 60 cm (minimale afmeting meterkast bestaande bouw).~~

#### ~~4\. Oppervlakte kanalen of leidingen~~

~~De oppervlakte die wordt ingenomen door verticale koven, schoorsteenkanalen, ventilatiekanalen of stand- of grondleidingen (tenzij horizontale leidingen, zie hierna) wordt niet meegeteld.~~

~~De oppervlakte die wordt ingenomen door standleidingen (verticale leidingen) wordt niet meegeteld. De oppervlakte die wordt ingenomen door grondleidingen (horizontale leidingen), wordt wel meegeteld.~~

~~Bij een schoorsteenmantel en/of rookkanaal (die naar boven of beneden breed kan uitlopen) is de oppervlakte op 1,50m-hoogte bepalend.~~

#### ~~5\. Oppervlakte onder een open of gesloten vaste trap~~

~~Van de oppervlakte onder een open dan wel gesloten vaste trap telt mee dat gedeelte waar de ruimte tussen vloer en onderkant trap ten minste 1,50m hoog is.~~

### 1.4 Afronding oppervlakte op hele m2

De Huurcommissie bepaalt eerst de oppervlakte per vertrek afgerond op twee decimalen. Daarna wordt de oppervlakte van alle vertrekken gesaldeerd en vindt afronding plaats op hele vierkante meters. Bij 0,5m² of meer wordt afgerond naar boven, bij minder dan 0,5m² naar beneden. Als laatste wordt vervolgens een waardering in punten toegekend.

_Voorbeeld:_

_kamer : lengte 3,76m x breedte 4,12m = 15,4912 m², afgerond : 15,49 m²_  
_keuken: lengte 2,95m x breedte 3,81m = 11,2395 m², afgerond : 11,24 m²_  
_Totaal : 26,73 m² Afronding op hele m² : 27 m²._

_Dit vertaalt zich dan naar 27 \* 1 punt (per m2) = 27 punten_

## Rubriek 2 Oppervlakte van overige ruimten

### 2.1 Puntentoekenning

Overige ruimten worden gewaardeerd met 0,75 punt per vierkante meter.

### 2.2 Wat zijn overige ruimten?

> De gespecificeerde ruimtesoort is leidend bij de waardering van een ruimte. Een ruimte met `Ruimtesoort` `overige ruimte` komt in aanmerking voor waardering in de rubriek 'Oppervlakte van overige ruimten' als de oppervlakte minimaal 2 m² is. Een ruimte met `Ruimtesoort` `vertrek` komt in aanmerking voor waardering in de rubriek 'Oppervlakte van overige ruimten' als de oppervlakte minder dan 4 m² en minimaal 2 m² is.
>
> Een ruimte dient alleen als overige ruimte gespecificeerd te worden wanneer deze voldoet aan alle onderstaande eisen. De doorgehaalde eisen worden niet door het systeem gecontroleerd.

Een ruimte wordt als overige ruimte gewaardeerd als deze voldoet aan de volgende eisen:

* ~~de vloer moet begaanbaar zijn;~~
* de ruimte dient een oppervlakte te hebben van minimaal 2 m2;
* de ruimte voldoet niet aan de eisen voor een vertrek (zie paragraaf 1.2) of een verkeersruimte zijnde;
  * een ruimte die dient voor het bereiken van een andere ruimte;
  * ~~geen ruimte om duurzaam in te verblijven.~~

Voorbeelden van overige ruimten zijn bijkeukens, bergingen, wasruimten, schuren, garages, zolders en kelders, op voorwaarde dat aan bovenstaande eisen wordt voldaan. Parkeerruimte die exclusief tot één adres behoort (privé-garage), kan worden gewaardeerd als overige ruimte. Gemeenschappelijke garages met daarin parkeerplek(ken) worden gewaardeerd onder rubriek 10 (gemeenschappelijke parkeerruimten).

Van de minimumoppervlakte zoals hiervoor genoemd kan niet worden afgeweken. Heeft de ruimte bijvoorbeeld een oppervlakte van 1,95 m2, dan wordt niet aan de gestelde eis van minimaal 2 m2 voldaan. De oppervlakte mag niet naar boven worden afgerond waardoor invulling aan de eis zou zijn gegeven.

_Verkeersruimten_

Verkeersruimten zoals hallen, gangen, en overlopen worden sowieso niet afzonderlijk gewaardeerd, dus krijgen geen punten op basis van dit onderdeel van het woningwaarderingsstelsel.

_Zolderruimte_

Indien een zolderruimte niet als vertrek wordt gewaardeerd (zie paragraaf 1.2), dan kan deze mogelijk wel in aanmerking komen voor een waardering als overige ruimte. Dan moet de zolderruimte naast bovenstaande eisen aan nog twee eisen voldoen. De zolderruimte moet namelijk bereikbaar zijn via een tot de woning behorende trap en het dak moet beschoten zijn. Voldoet de zolderruimte niet aan de eisen van paragraaf 1.2 en niet aan de voornoemde eisen, dan wordt de zolderruimte niet gewaardeerd.

> Zolderruimte groter dan 2m2 met het `Bouwkundigelement` `vlizotrap` wordt gewaardeerd onder `Oppervlakte van overige ruimten`, mits deze wordt ingeschoten met `ruimtesoort` `overige ruimte`.
> Zolderruimte groter dan 2m2 maar kleiner dan 4m2 met het `Bouwkundigelement` `trap` wordt gewaardeerd onder `Oppervlakte van overige ruimten`, mits deze wordt ingeschoten met `ruimtesoort` `overige ruimte`.
> Zolderruimte groter dan 4m2 met het `Bouwkundigelement` `trap` wordt gewaardeerd onder `Oppervlakte van vertrekken`, mits deze wordt ingeschoten met `ruimtesoort` `vertrek`.

_Toiletruimte_

Een toiletruimte kan als overige ruimte worden gewaardeerd als aan de eisen van overige ruimte wordt voldaan.

### 2.3 Meetinstructies

> De woningwaardering package gaat er vanuit dat de gebruiker zich houdt aan onderstaande meetinstructies voor oveirge ruimten. Met uizondering van _kasten_ kunnen de meetinstructies niet getoets of berekend worden op basis van het VERA model.

De wetgever heeft een aantal meetinstructies meegegeven:

#### 1\. Binnenmaatse meting

~~Meting van de oppervlakte van overige ruimten vindt plaats van muur tot muur, op een hoogte van 1,50 m boven de vloer, inclusief de oppervlakte van alle tot de woning behorende losse en vaste kasten.~~

~~De Huurcommissie berekent de hoogte van 1,50 m door te meten tot het dakbeschot, het zichtbare dakvlak of plafond (gordingen en balken blijven buiten de meting).~~

_~~Pui, erker en entresol~~_

~~Als er sprake is van een pui wordt de binnenzijde van die pui (het kozijn) genomen. Een erker wordt meegerekend indien deze inwendig een vrije hoogte heeft van ten minste 1,50 m. Indien er sprake is van een zgn. entresol (tussenverdieping) dan dient de oppervlakte onder en/of boven deze entresol te worden meegerekend, indien de vrije hoogte ten minste 1,50m bedraagt.~~

_Kasten_

De oppervlakte van alle tot de woning behorende losse en vaste kasten wordt meegerekend.

* Van vaste kasten die uitkomen in een wel gewaardeerde overige ruimte wordt de netto oppervlakte bepaald en bij de oppervlakte opgeteld
* Een kast, waarvan de deur uitkomt op een verkeersruimte, wordt niet gewaardeerd.
* ~~Losse kasten zijn niet van belang bij het meten. De oppervlakte van de overige ruimte wordt bepaald, incl. de oppervlakte die wordt ingenomen door een losse kast.~~

#### ~~2\. Oppervlakte trap(gat)~~

~~Van de oppervlakte onder een open dan wel gesloten vaste trap telt dat gedeelte waar de ruimte tussen vloer en onderkant trap ten minste 1,50m hoog is. De oppervlakte die door een in ingeschoven toestand liggende inschuifbare of opvouwbare trap wordt ingenomen, wordt niet meegeteld.~~

~~De oppervlakte van een trapgat wordt in mindering gebracht.~~

#### ~~3\. Vloeroppervlakte moederhaard, cv-ketel, boilerinstallatie en radiatoren~~

~~De vloeroppervlakte onder moederhaard, cv-ketel, boilerinstallatie en radiatoren wordt meegeteld.~~

~~Als zich in een overige ruimte, of een kast in een overige ruimte, een gas- en/of elektrameter bevindt, dan wordt de oppervlakte gewaardeerd onder aftrek van 30 x 60 cm (minimale afmeting meterkast bestaande bouw).~~

#### ~~4\. Oppervlakte kanalen of leidingen~~

~~De oppervlakte die wordt ingenomen door schoorsteenkanalen, ventilatiekanalen of stand- of grondleidingen (tenzij horizontale leidingen, zie hierna) wordt niet meegeteld.~~

~~De oppervlakte die wordt ingenomen door standleidingen (verticale leidingen) wordt niet meegeteld. De oppervlakte die wordt ingenomen door grondleidingen (horizontale leidingen), wordt wel meegeteld.~~

~~Bij een schoorsteenmantel en/of rookkanaal (die naar boven of beneden breed kan uitlopen) is de oppervlakte op 1,50m-hoogte bepalend.~~

#### 5\. Zolderruimte

Als geen _vaste_ trap aanwezig is, wordt het aantal punten van de vloeroppervlakte van de zolderruimte met 5 punten verminderd, maar niet met meer punten dan voor de oppervlakte van de zolderruimten wordt gegeven.

~~Is er op de zolderverdieping ook nog een vertrek aanwezig dat alleen bereikbaar is via het zoldergedeelte dan wordt de oppervlakte van het zoldergedeelte verminderd met de loopruimte om het vertrek te bereiken. De dan resterende zolderoppervlakte dient minimaal 2 m2 te bedragen en wordt dan gewaardeerd als overige ruimte.~~

#### ~~6\. Overloop~~

~~Een overloop is een verkeersruimte en wordt niet gewaardeerd. Als er met aftrek van de verkeersruimte en trap voldoende ruimte overblijft en deze (zolder)overloop kennelijk ook bedoeld is als bergruimte, dan wordt deze ruimte wel gewaardeerd (als overige ruimte).~~

#### 7\. Parkeerruimte

Een parkeerruimte waartoe bewoners van één adres op grond van de huurovereenkomst exclusieve toegang hebben, wordt gewaardeerd volgens deze rubriek. Een voorbeeld is een garagebox behorende tot de woning.

> De `Ruimtedetailsoort` `garage` wordt tot op heden alleen gewaardeerd als overige ruimte wanneer deze voldoet aan de voorwaarden.

### 2.4 Afronding oppervlakte op hele m2

De oppervlakte per overige ruimte wordt afgerond op 2 decimalen. De afronding van de oppervlakte van alle overige ruimte samen vindt plaats op hele vierkante meters na saldering van de oppervlakte van de afzonderlijke overige ruimten; bij 0,5 m2 of meer wordt naar boven afgerond, bij minder dan 0,5 m2 naar beneden. Waardering in punten vindt na saldering en afronding plaats.

_Voorbeeld:_

_Garage : lengte 3,16m x breedte 6,12m = 19,3392 m², afgerond : 19,34 m²_  
_Bijkeuken: lengte 2,11m x breedte 2,87m = 6,0557 m², afgerond : 6,06 m²_
_Totaal : 25,40 m² Afronding op hele m² : 25 m²._

_Dit vertaalt zich dan naar 25 \* 0,75 punt (per m2) = 18.75 punten._

## Rubriek 3 Verkoeling en verwarming

> Op het moment is het met de VERA-standaard niet mogelijk om op ruimte-niveau aan te geven of een ruimte verwarmd en/of verkoeld is. Zie https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/100. Daarom hebben wij `verwarmd` en `verkoeld` als boolean-kenmerken van een `EenhedenRuimte` toegevoegd.

### 3.1 Puntentoekenning

* Verwarmde vertrekken worden gewaardeerd met 2 punten.

* Verwarmde overige ruimten en verkeersruimten worden gewaardeerd met 1 punt met een maximum van 4 punten voor alle overige ruimtes en verkeersruimten (samen).

> Wij hanteren de volgende ruimtedetailsoorten als `verkeersruimte`:
>
> * hal
> * overloop
> * entree (onze eigen uitbreiding op de referentiedata)
> * gang (onze eigen uitbreiding op de referentiedata)
> * trappenhuis (onze eigen uitbreiding op de referentiedata)

_Extra voorziening_

Voorzieningen met zowel een verwarmingsfunctie als verkoelingsfunctie worden per vertrek gewaardeerd met 1 extra punt tot een maximum van 2 punten (bij meerdere vertrekken met een verkoelingsfunctie).

~~Woningen die zonder koeling voldoende koel kunnen blijven, worden per vertrek gewaardeerd met 1 extra punt tot een maximum van 2 punten. Of sprake is van zo’n woning, dient te worden bepaald met de NTA 8800 en blijkt uit een actueel NTA-energielabel waarin de koelfunctie is meegenomen en het risico voor oververhitting als ‘laag’ is afgegeven.~~

> De informatie voor of het risico voor oververhitting op 'laag' is afgegeven is niet beschikbaar in EP-online, niet als veld in VABI en ook niet in de referentiedata. Daarom hebben wij deze regel vooralsnog niet opgenomen in de woningwaardering package.

### 3.2 Onroerende zaak en onroerende aanhorigheden

~~Punten voor verwarming en verkoeling worden alleen toegekend als de verwarming of de voorziening met zowel een verwarmingsfunctie als verkoelingsfunctie tot de onroerende zaak en zijn onroerende aanhorigheid behoort.~~

~~Dit is bij een radiator het geval als deze is bevestigd aan de muur of in de grond. Een mobiele elektrische radiator of een mobiele airco behoort niet tot de onroerende zaak. Hetzelfde geldt voor gevelkachels en gashaarden. Een verdikte buis, pijp of moederhaard wordt wél gerekend tot de onroerende zaak, indien deze als zodanig bedoeld of herkenbaar is.~~

_Koelsystemen_

~~Centrale koelsystemen, zoals omkeerbare warmtepompen, passieve koeling door een bodemlus of een WKO-systeem moeten voorzien zijn van vloerkoeling, lagetemperatuur-radiatoren of radiatorconvectoren. Voor andere onroerend aanhorige koelsystemen, zoals een vaste airco, geldt dat deze een productgebonden energielabel moet hebben van minimaal A+ (bepaald volgens de Europese Ecodesign-richtlijn), en een minimaal vermogen moet kunnen leveren van 100 W/m2 bij een werkingstemperatuur tot 35 graden Celsius.~~

### 3.3 Aangrenzende ruimten met open doorgang

~~Vertrekken of overige ruimten die met elkaar in verbinding staan, worden in een bepaald geval als één verwarmd vertrek of overige ruimte gewaardeerd. Dit is het geval als zich tussen die twee verwarmde vertrekken of overige ruimten een opening bevindt, die breder is dan 50% van de muur, waarin deze opening zich bevindt. Het moet hierbij gaan om een niet-afsluitbare opening, die over een breedte van minimaal 0,85 m een minimumhoogte heeft van 2 m. De muur wordt gemeten in het vertrek of overige ruimte, waarin de tussenwand het smalst is. De figuur in paragraaf 2.5 van het vorige hoofdstuk geeft dit visueel weer.~~

### 3.4 Open keukens

Voor deze rubriek wordt een verwarmde open keuken als afzonderlijk verwarmd vertrek beschouwd en krijgt dus twee punten. ~~Onder een open keuken wordt hier verstaan een keuken die in open verbinding staat met een ander vertrek, terwijl zich tussen de keuken en het andere vertrek een opening bevindt, die breder is dan 50% van de tussenmuur.~~ Zowel de open keuken als het vertrek of overige ruimte waarmee de open verbinding bestaat, wordt voor deze rubriek individueel gewaardeerd met punten indien deze verwarmd zijn.

> Omdat wij in de package niet (kunnen) controleren op keukenkastjes, doen wij de aanname dat elke ruimte, die van zichzelf geen keuken is, met een aanrecht langer dan 1 meter als open keuken wordt gewaardeerd voor verkoeling en verwarming

## Rubriek 4 Energieprestatie

Een (groot) deel van het totale puntenaantal wordt bepaald door de energieprestatie van de woonruimte. Sinds 2011 speelt het energielabel een rol in het puntenstelsel, waarbij een energielabel of energie-index maximaal 10 jaar geldig is. De energieprestatie kan sinds 1 januari 2021 op drie manieren zijn vastgesteld:

1. Een oud energielabel: registratie heeft plaatsgevonden vóór 1 januari 2015. In 2021 en later liepen en lopen veel sinds 1 juli 2011 verstrekte energielabels af, want de geldigheidsduur is tien jaar.
2. De energie-index: registratie op of na 1 januari 2015 tot 1 januari 2021. In 2025 en later lopen veel sinds 1 januari 2015 verstrekte energie-indexen af, want de geldigheidsduur is tien jaar.
3. Het energielabel op basis van de NTA 8800: registratie op of na 1 januari 2021.

In EP-online is te vinden wat de energieprestatie van een woning is.

### 4.1 Puntentoekenning

Bij een energielabel bepaalt de labelklasse (A++++ t/m G) het aantal punten dat de verhuurder mag doorrekenen in de maximale huurprijs. Bij een energie-index is de indeling in letters vervangen door een cijfer. De energie-index wordt in de puntentelling meegenomen indien in EP-online staat aangegeven dat de energie-index geldig is voor de toepassing van het woningwaarderingsstelsel.

Zie hieronder de puntentoekenning van de energieprestatie bij een geldig energie-index en (oud of nieuw) energielabel.

NTA 8800

| NTA 8800 energielabel (afgegeven na 1 januari 2021) of NEN 7120 energielabel (afgegeven voor 1 januari 2021) | Energie-index (EI) | Eengezinswoning | Meergezinswoning / Duplexwoning |
| --- | --- | --- | --- |
| A++++ | n.v.t. | 62  | 58  |
| A+++ | n.v.t. | 57  | 53  |
| A++ | EI < 0,6 | 52  | 48  |
| A+  | 0,6 < EI ≤ 0,8 | 47  | 43  |
| A   | 0,8 < EI ≤ 1,2 | 41  | 37  |
| B   | 1,2 < EI ≤ 1,4 | 34  | 30  |
| C   | 1,4 < EI ≤ 1,8 | 22  | 15  |
| D   | 1,8 < EI ≤ 2,1 | 14  | 11  |
| E   | 2,1 < EI ≤ 2,4 | \-4\* | \-4\* |
| F   | 2,4 < EI ≤ 2,7 | \-9 | \-9 |
| G   | EI > 2,7 | \-15 | \-15 |

_\* Artikel 10d (energieprestatie) van de Uitvoeringswet huurprijzen woonruimte (amendement De Hoop, 36496, nr. 40) schrijft dwingend voor wat de puntentoekenning voor label E, F en G moet zijn. Abusievelijk is in het Besluit huurprijzen woonruimte een schrijffout ontstaan bij label E. Daar is in het WWS -5 opgenomen, waar de wet -4 voorschrijft. Nu de wet leidend is, wordt tot een wijzigingsbesluit dit oplost, via de afwijkingsmogelijkheid van artikel 5, tweede lid, van het Besluit huurprijzen woonruimte gebruik gemaakt om de juiste punten voor energielabel E toe te kennen, zijnde -4._

### 4.2 Overgangsrecht kleine woningen ≤ 40 m2

LET OP: DEZE UITZONDERING KOMT PER 1 JANUARI 2025 TE VERVALLEN.

Indien de energieprestatie is bepaald met de van toepassing zijnde NTA 8800 (nieuw energielabel) in de periode 1 januari 2021 - 1 juli 2024, geldt tot 1 januari 2025 een afwijkende waardering indien de gebruikersoppervlakte gelijk of minder is dan 40m2. Voor de oppervlakte wordt uitgegaan van de gebruikersoppervlakte van de woning die wordt bepaald bij de verstrekking van een energielabel met toepassing van NTA 8800.

Deze waardering bedraagt:

_Voor woningen met een gebruiksoppervlakte < 25 m2 geldt het volgende puntenaantal:_

Woningen met een gebruikersoppervlakte < 25m2

| NTA 8800 energielabel | Eengezinswoning | Meergezinswoning / Duplexwoning |
| --- | --- | --- |
| A++++ | 62  | 62  |
| A+++ | 62  | 62  |
| A++ | 60  | 56  |
| A+  | 55  | 51  |
| A   | 49  | 45  |
| B   | 42  | 38  |
| C   | 36  | 32  |
| D   | 32  | 28  |
| E   | \-4\* | \-4\* |
| F   | \-9 | \-9 |
| G   | \-15 | \-15 |

_\* Artikel 10d (energieprestatie) van de Uitvoeringswet huurprijzen woonruimte (amendement De Hoop, 36496, nr. 40) schrijft dwingend voor wat de puntentoekenning voor label E, F en G moet zijn. Abusievelijk is in het Besluit huurprijzen woonruimte een schrijffout ontstaan bij label E. Daar is in het WWS -5 opgenomen, waar de wet -4 voorschrijft. Nu de wet leidend is, wordt tot een wijzigingsbesluit dit oplost, via de afwijkingsmogelijkheid van artikel 5, tweede lid, van het Besluit huurprijzen woonruimte gebruik gemaakt om de juiste punten voor energielabel E toe te kennen, zijnde -4._

_Voor woningen met een oppervlakte ≥ 25m2 en < 40 m2 geldt het volgende puntenaantal:_

Woningen met een gebruikersoppervlakte ≥ 25m2 en < 40 m2

| _NTA 8800 energielabel_ | _Eengezinswoning_ | _Meergezinswoning / Duplexwoning_ |
| --- | --- | --- |
| A++++ | 62  | 62  |
| A+++ | 57  | 53  |
| A++ | 52  | 48  |
| A+  | 47  | 43  |
| A   | 41  | 37  |
| B   | 34  | 30  |
| C   | 22  | 15  |
| D   | 14  | 11  |
| E   | \-4\* | \-4\* |
| F   | \-9 | \-9 |
| G   | \-15 | \-15 |

_\* Artikel 10d (energieprestatie) van de Uitvoeringswet huurprijzen woonruimte (amendement De Hoop, 36496, nr. 40) schrijft dwingend voor wat de puntentoekenning voor label E, F en G moet zijn. Abusievelijk is in het Besluit huurprijzen woonruimte een schrijffout ontstaan bij label E. Daar is in het WWS -5 opgenomen, waar de wet -4 voorschrijft. Nu de wet leidend is, wordt tot een wijzigingsbesluit dit oplost, via de afwijkingsmogelijkheid van artikel 5, tweede lid, van het Besluit huurprijzen woonruimte gebruik gemaakt om de juiste punten voor energielabel E toe te kennen, zijnde -4._

### 4.3 Bouwjaar bepalend bij ontbreken geldig energielabel of energie-index

Indien op de peildatum van de puntentelling een geldig energielabel of energie-index ontbreekt of als de geldigheidsduur van het energielabel is verstreken dan bepaalt het bouwjaar van de woning het aantal punten.

De puntentelling bij toepassing bouwjaar is als volgt:

Energie-index

| _Bouwjaar_ | _Eengezinswoning_ | _Meergezinswoning / Duplexwoning_ |
| --- | --- | --- |
| 2002 en later | 41  | 37  |
| 2000 t/m 2001 | 34  | 30  |
| 1992 t/m 1999 | 22  | 15  |
| 1984 t/m 1991 | 14  | 11  |
| 1979 t/m 1983 | \-4\* | \-4\* |
| 1977 t/m 1978 | \-9 | \-9 |
| 1976 of ouder | \-15 | \-15 |

_\* Artikel 10d (energieprestatie) van de Uitvoeringswet huurprijzen woonruimte (amendement De Hoop, 36496, nr. 40) schrijft dwingend voor wat de puntentoekenning voor label E, F en G moet zijn. Abusievelijk is in het Besluit huurprijzen woonruimte een schrijffout ontstaan bij label E. Daar is in het WWS -5 opgenomen, waar de wet -4 voorschrijft. Nu de wet leidend is, wordt tot een wijzigingsbesluit dit oplost, via de afwijkingsmogelijkheid van artikel 5, tweede lid, van het Besluit huurprijzen woonruimte gebruik gemaakt om de juiste punten voor energielabel E toe te kennen, zijnde -4._

### 4.4 Monumenten

Voor rijks-, provinciale en gemeentelijke monumenten gelden in afwijking van andere woningen geen minpunten voor de energielabels E, F, en G en daaraan gelijkgestelde Energie-indexen en bouwjaren. De puntentoekenning bedraagt dan, in afwijking van bovenstaande tabellen, 0 punten.

### 4.5 ~~Afwijkingsbevoegdheid hogere energielabelklasse dan A++++~~

~~De hierboven vermelde tabellen met de puntentoekenning voor de labelklasse gaan tot A++++. De Huurcommissie heeft de bevoegdheid gekregen om af te wijken van de hierboven aangegeven puntenwaardering indien de gemaakte kosten om deze energieprestatie te bereiken, aanmerkelijk afwijken van hetgeen als gangbaar wordt beschouwd, of indien de energieprestatie aanmerkelijk beter is dan hetgeen als gangbaar bij een energielabelklasse A ++++ wordt beschouwd.~~

### 4.6 ~~Gerede twijfel energielabel~~

~~Als huurder twijfelt aan de juistheid van het toepasselijke energielabel dan heeft de Huurcommissie de bevoegdheid om een ‘eigen oordeel’ uit te spreken bij gerede twijfel van het energielabel. Een Huurcommissie eigen oordeel (HEO) kan worden uitgesproken indien de huurder aantoont dat sprake is van gerede twijfel van de juistheid van het energielabel/energie-index en dat het gewijzigde energielabel/energie-index van invloed zal zijn op de maximaal redelijke huurprijs.~~

~~Bij ‘gerede twijfel’ wordt beoordeeld of de huurder voldoende heeft aangetoond dat een verkeerd woningkenmerk of verkeerde woningkenmerken is/zijn gebruikt bij het vaststellen van het energielabel, waardoor de juistheid van de labelklasse voor de desbetreffende woning in het geding is. Zo’n fout kenmerk is bijvoorbeeld: het verkeerde soort glas, zoals enkel in plaats van dubbel glas. Of er staat een verkeerd type woning op het label, bijvoorbeeld een hoekwoning in plaats van een tussenwoning. Of de muren zijn slecht geïsoleerd, terwijl het energielabel aangeeft dat het huis juist goed geïsoleerd is.~~

~~De huurder dient gerede twijfel aan te tonen door middel van het energielabelafschrift en moet onderbouwen waarom een onjuist woningkenmerk is gebruikt. Het energielabelafschrift is te downloaden via [Mijnoverheid.](https://mijn.overheid.nl/)~~

~~Indien de Huurcommissie tot een eigen oordeel wil komen dan laat de Huurcommissie onderzoeken wat de energieprestatie van de woning is. Het eigen oordeel is uitsluitend in de voorliggende zaak van kracht, wordt niet geregistreerd in het register van de Rijksdienst voor Ondernemend Nederland en komt te vervallen na ontbinding van de huurovereenkomst.~~

### 4.7 Energieprestatievergoeding

Voor woningen die zelf (gedeeltelijk) in hun energieverbruik voorzien, door bijvoorbeeld zonnepanelen, kan bij het verhuren een energieprestatievergoeding (EPV) worden afgesproken. De woning zal dan moeten voldoen aan de eisen voor een EPV. Als dit het geval is dan is het aantal punten op basis van het puntenstelsel voor de energieprestatie lager. Om te voorkomen dat in de gevallen waarin een energieprestatievergoeding is overeengekomen, de opwekking van energie voor de huurder tevens wordt verdisconteerd in de huurprijs, wordt voor deze woningen een correctiefactor toegepast op het aantal punten voor de energieprestatie. In die gevallen wordt de energieprestatie gewaardeerd met 32 punten voor een ééngezinswoning en 28 punten voor meergezins- en duplexwoningen.

### 4.8 Onderscheid eengezinswoningen en meersgezinswoning (duplexwoningen)

Voor de puntentoekenningen in de tabellen wordt onderscheid gemaakt tussen eengezinswoningen meersgezinswoning (duplexwoningen).

* Eengezinswoning is een woning waarbij er geen andere woningen boven of onder de woning in kwestie bestaan. Hieronder vallen onder andere vrijstaande woningen, aaneen gebouwde woningen, zoals twee onder één kap gebouwde hele huizen en voorts rijtjeshuizen.
* Meergezinswoningen of duplexwoningen zijn alle woningen die geen eengezinswoning zijn.

> Let op: deze definitie is anders dan vaak gehanteerd wordt zie: https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/154

## Rubriek 5 Keuken

### 5.1 Eisen keuken

Punten worden alleen aan het onderdeel ‘keuken’ toegekend als de ruimte voldoet aan het volgende basisniveau:

* ~~aan- en afvoer van water en ten minste één vast aansluitpunt voor koken op gas of elektriciteit;~~
* een aanrechtblad met een aan een gesloten lengte van minimaal 1 m (lengte incl. spoelbak, incl. kookplaat);
* ~~twee inbouwkasten met een breedte van minimaal 50 cm;~~
* ~~waterdichte afwerking boven het waterdichte aanrechtblad en in de kookhoek vanaf de vloer tot een hoogte van minimaal 1,50 m.~~

Als de keuken niet voldoet aan het basisniveau, worden geen punten toegekend, ook niet voor de extra voorzieningen als bedoeld in paragraaf 5.4 hierna. Een spoelbak in een keuken die voldoet aan het basisniveau, krijgt alleen de waardering voor de rubriek keuken en niet ook nog als ‘wastafel’.

> Zorg ervoor dat alleen aanrechten met een spoelbak worden meegegeven en dat deze spoelbak niet ook nog als aparte `wastafel` wordt meegegeven.

### 5.2 Puntentoekenning lengte aanrecht

* Bij een aanrechtlengte minder dan 1 m, worden 0 punten toegekend.
* Bij een aanrechtlengte tussen de 1 en 2 m, worden 4 punten toegekend.
* Bij een aanrechtlengte van 2 m of langer, worden 7 punten toegekend.

De waardering van de keukeninstallatie wordt bepaald op basis van de lengte van het aanrecht, ~~waarbij sprake moet zijn van een waterdicht keukenblad~~

Een aanrecht met spoelbak, waarvan de lengte minder bedraagt dan 1 m, voldoet dus niet aan de eis van 1 m en wordt daarom niet als aanrecht gewaardeerd, maar als wastafel.  
~~Een aanrecht zonder onderkasten wordt ook gewaardeerd als wastafel.~~

Een waterdichte afwerking wordt in beginsel verondersteld aanwezig te zijn, maar kan pas worden meegenomen als deze aan te merken valt als onroerende aanhorigheid. Dat betekent dat een keuken met bijvoorbeeld een tegelwand of aangebrachte, waterdichte verf wel voldoet aan de eis van een waterdichte afwerking, maar als er slecht een plastic zeil voor een wand is gehangen niet.

### 5.3 Meetinstructies lengte aanrechtblad

De aanrechtlengte wordt over het midden van het bovenblad gemeten, inclusief ingebouwde spoelbakken en kookplaten.

De lengte van een niet direct aan het aanrecht aansluitend werkblad of van een blad dat is samengesteld uit een ander materiaal wordt bij de lengte meegeteld.

Indien een aanrechtblad langer is dan de aanwezige onderkasten met de bedoeling dat er onder het langere gedeelte van het aanrechtblad een losstaande koelkast, vaatwasser, wasmachine e.d., kan worden geplaatst, dan wordt dit gedeelte van het aanrechtblad mee gemeten mits er onder het blad aansluitmogelijkheden aanwezig zijn voor genoemde apparatuur.

Van een (standaard)aanrechtblad dat gedeeltelijk is ingemetseld of waar de wandbetegeling op het blad is aangebracht, wordt uitsluitend het bruikbare c.q. zichtbare gedeelte gemeten.

Indien er sprake is van een hoekaanrecht wordt de lengte van het aanrecht bepaald door (zie figuur):

1. De lange zijde van het langere aanrechtdeel te meten (zie horizontale blauwe lijn).
2. Vervolgens die lengte te salderen met de lange zijde van het kortere aanrechtdeel (zie verticale blauwe lijn).

De lengte van een kookeiland wordt bepaald door de lengte van de lange zijde.

> Zorg ervoor dat de lengte die wordt meegegeven in het inputmodel volgens deze regels zijn gemeten. De package doet geen aanpassingen aan de lengte.

### 5.4 Puntentoekenning extra voorzieningen

Het woningwaarderingsstelsel geeft voor het onderdeel keuken extra punten voor voorzieningen in de keuken. Hiervoor geldt een maximum tot het aantal punten dat voor de aanrechtlengte is bepaald. Een keuken met een aanrechtlengte tussen de 1 en 2 m kan tot maximaal 4 extra punten krijgen voor voorzieningen. Een keuken met een aanrechtlengte van 2 of meer meter kan tot maximaal 7 punten extra krijgen voor voorzieningen. 

Zie hieronder de limitatieve lijst met voorzieningen waarvoor extra punten worden toegekend.

Punten toekenning extra voorzieningen

|     |     |
| --- | --- |
| Inbouw afzuiginstallatie\* | 0,75 punt |
| Inbouw kookplaat inductie | 1,75 punten |
| Inbouw kookplaat keramisch | 1 punt |
| Inbouw kookplaat gas | 0,5 punt |
| Inbouw koelkast | 1 punt |
| Inbouw vrieskast | 0,75 punt |
| Inbouw oven elektrisch | 1 punt |
| Inbouw oven gas | 0,5 punt |
| Inbouw magnetron | 1 punt |
| Inbouw vaatwasmachine | 1,5 punten |
| Extra kastruimte boven het minimum (per 60 cm breedte, met een minimum van 60 cm hoogte) | 0,75 punt |
| Éénhandsmengkraan | 0,25 punt |
| Thermostatische mengkraan | 0,5 punt |
| Kokend waterfunctie (al dan niet apart of in aanvulling op de kraan) | \+ 0,5 punt |

_\* ~~Bij een afzuiginstallatie gaat het om een luchtafvoer met afzuiging naar buiten de woning of op basis van recirculatie met actieve koolstof- en vetfilters. Een afzuiginstallatie kan zowel een afzuig- of recirculatiekap boven de kookinstallatie zijn, als een in het aanrecht geïntegreerd afzuigsysteem.~~_

~~** Om aan het basisniveau voor de kwalificatie als keuken te voldoen, moeten twee inbouwkasten met een breedte van minimaal 50 cm (per stuk) aanwezig zijn. De totale minimumbreedte bedraagt dus 1 meter. Per 60 cm breedte extra kastruimte kan vervolgens, als ook aan de andere eisen wordt voldaan, 0,75 punt extra worden toegekend.~~

Wanneer een object twee voorzieningen heeft, bijvoorbeeld een ingebouwde combi magnetron/oven of een gecombineerde koel- en vrieskast, worden beide voorzieningen in dit object gewaardeerd conform bovenstaande lijst. ~~Voor de meting van keukenkasten wordt uitgegaan van de buitenmaat.~~

## Rubriek 6 Sanitair

### 6.1 Puntentoekenning sanitaire basisvoorzieningen

Het woningwaarderingsstelsel geeft punten aan sanitaire basisvoorzieningen:

Puntentoekenning sanitaire basisvoorzieningen

|     |     |
| --- | --- |
| toilet in een aparte ruimte | 3 punten |
| toilet in een badkamer | 2 punten |
| hangend toilet in aparte ruimte | 3,75 punten |
| hangend toilet in badkamer | 2,75 |
| wastafel\* | 1 punt |
| meerpersoonswastafel | 1,5 punten |
| douche | 4 punten |
| bad | 6 punten |
| bad en douche | 7 punten |

_\* tot een maximum van 1 punt per vertrek of overige ruimte m.u.v. de badkamer._

**_Toilet_**

Punten worden toegekend aan een toilet met waterspoeling als het toilet is geplaatst in een daartoe bestemde ruimte ~~en als het toilet binnen het woongebouw is gelegen. Wanneer sprake is van een toilet dat buiten de woning maar binnen het woongebouw is gelegen, dan geldt dat het toilet in de waardering wordt meegenomen als het gebruik van het toilet door derden is uit te sluiten~~. Toiletten buiten toiletruimten en badkamers komen niet in aanmerking voor waardering.

**_Wastafel_**

~~Als wastafels worden alle bakken geteld voor wassen en spoelen die op de waterleiding én op het huisriool zijn aangesloten. Een dergelijke bak wordt niet als wastafel gewaardeerd indien boven de bak een douche is aangebracht. Een bad of spoelbakken in een keukenaanrecht, bidet of lavet wordt niet als wastafel, douche of bad gewaardeerd.~~ Wastafels worden gewaardeerd tot een maximum van 1 punt per vertrek of overige ruimte, m.u.v. de badkamer.

Van een meerpersoonswastafel is sprake bij een wastafel ~~met een minimale breedte van 70 cm, voorzien van twee kranen~~. Deze wastafels worden tot maximaal 1,5 punt per vertrek of overige ruimte, m.u.v. de badkamer, gewaardeerd. De kranen worden afzonderlijk gewaardeerd.

Zoals genoemd in paragraaf 5.2 waardeert de Huurcommissie een fonteintje en een aanrecht dat niet voor punten in aanmerking komt, waarvan de aanrechtlengte korter is dan één meter, als wastafel. In alle andere gevallen wordt een spoelbak in de keuken dus niet als wastafel gewaardeerd.

**_Bad en douche_**

Als douche wordt meegeteld iedere door de verhuurder aangebrachte installatie voor het nemen van een stortbad. Hieronder valt eveneens een zogenaamde douchecabine, die voldoet aan bovengenoemde voorwaarden, als de douchcabine in een vertrek (anders dan bad- of doucheruimte) of overige ruimte is geplaatst. De oppervlakte van dat vertrek of van die overige ruimte wordt in dat geval niet verminderd met de door de douchecabine ingenomen oppervlakte.

Aan baden worden 6 punten toegekend, ongeacht de lengte van het bad, ~~als een volwassen persoon er in een normale zithouding in kan plaatsnemen. Indien een bad is voorzien van een (hand)douche, dan wordt het douchegarnituur niet afzonderlijk geteld~~.

Indien in de badruimte behalve het bad tevens een afzonderlijke douche is aangebracht, geldt een waardering van 7 punten.

~~Als het aansluitpunt voor warm en koud water bedoeld is voor gecombineerd gebruik van zowel een wastafel als de naastgelegen douche of bad (bijvoorbeeld door middel van een zogenaamde zwenkarm), dan wordt uitsluitend de douche of het bad gewaardeerd. Dus niet én 1 punt voor wastafel én 4 of 6 punten voor douche of respectievelijk bad.~~

### 6.2 Puntentoekenning extra voorzieningen

Het woningwaarderingsstelsel geeft voor het onderdeel sanitair extra punten voor voorzieningen in de bad- of doucheruimte. Hiervoor geldt een maximum tot het aantal punten dat reeds voor douche, bad en/of bad/douche is verkregen. Anders gezegd: maximaal een verdubbeling van de toegekende punten voor douche, bad en/of bad/douche.

**_Eisen bad-of doucheruimte_**

Punten voor extra voorzieningen worden enkel toegekend indien deze zich bevinden in een bad- of doucheruimte. Bad- of doucheruimten moeten voldoen aan de volgende eisen:

* ~~Een waterdichte vloerafwerking~~\*.
* ~~De ruimte heeft over ten minste 50% van de oppervlakte een vrije hoogte van 2,00 m. (gemeten vanaf de vloer tot het zichtbare plafond).~~
* ~~Waterdichte afwerking tot 1,50 m hoogte voor badruimte en 1,80 m voor doucheruimte;~~
* Een wastafel ~~inclusief (tweehands-)mengkraan en een spiegel.~~
* Een douche of bad ~~met aansluitpunten voor warm en koud water (niet zijnde een warmwater apparaat) en voorzien van een warm- en koudwaterkraan of een mengkraan.~~

\* Een bad in een vertrek met een niet-waterdichte vloer wordt door de Huurcommissie wel gewaardeerd, omdat het bad zelf als een waterdichte afwerking wordt gezien.

**_Lijst voorzieningen_**

Zie hieronder de limitatieve lijst met voorzieningen waarvoor extra punten worden toegekend.

Voorzieningen in de bad- of doucheruimte

|     |     |
| --- | --- |
| Bubbelfunctie van het bad | 1,5 punten |
| Gemonteerde volledige afscheiding van de douche\* | 1,25 punten |
| Handdoekenradiator | 0,75 punt |
| Ingebouwd kastje met in- of opgebouwde wastafel | 1 punt |
| Kastruimte (minimale breedte van 40cm, en minimale hoogte van 40cm) | 0,75 punt (tot een maximum van 0,75) |
| Stopcontact (maximaal twee per wastafel) | 0,25 punt |
| Éénhandsmengkraan | 0,25 punt |
| Thermostatische mengkraan | 0,5 punt |

_\* ~~In het geval van een gemonteerde volledige afscheiding van de douche vindt de waardering van 1,25 punten plaats wanneer de doucheruimte beschikt over een onroerend aanhorige afscheiding met een waterdichte afwerking aan alle zijden van de douche. Ter illustratie: glazen deuren vallen hier wel onder, maar een douchegordijn (dat snel weggenomen kan worden) niet.~~_

> Voor een ingebouwde kast met wastafel moet de wastafel als aparte voorziening worden meegegeven.

## ~~Rubriek 7 Woonvoorzieningen voor gehandicapten~~

### ~~7.1 Puntentoekenning~~

~~Het woningwaarderingsstelsel kent punten toe voor woonvoorzieningen voor gehandicapten. Per € 332,00 van de door de verhuurder bestede kosten aan ingrepen in of aan de woonruimte ten behoeve van een gehandicapte kan, voor zover deze kosten in een redelijke verhouding staan tot de geboden kwaliteit en het niet gesubsidieerde kosten betreft, één punt worden toegekend.~~

### ~~7.2 Woonvoorzieningen~~

~~Om de bestede kosten in of aan de woonruimte ten behoeve van een gehandicapte in de puntentelling te betrekken, is het nodig dat het gaat om:~~

1. ~~maatwerkvoorzieningen: op de behoeften, persoonskenmerken en mogelijkheden van een persoon afgestemd geheel van diensten, hulpmiddelen, woningaanpassingen en andere maatregelen ten behoeve van zelfredzaamheid, participatie of beschermd wonen en opvang, of;~~
2. ~~woningaanpassingen: een bouwkundige of woontechnische ingreep in of aan een woonruimte, als bedoeld in artikel 1.1.1, eerste lid, van de Wet maatschappelijke ondersteuning 2015, of;~~
3. ~~gesubsidieerde voorzieningen of ingrepen op grond van een andere wettelijke regeling.~~

~~Extra punten worden voor deze woonvoorzieningen, woningaanpassingen of ingrepen toegekend indien aan de volgende cumulatieve voorwaarden is voldaan:~~

* ~~de ingreep moet hebben plaatsgevonden op of ná 01-04-1994;~~
* ~~de ingreep moet voor een deel zijn gesubsidieerd;~~
* ~~de ingreep dient voor “de gehandicapte”\* te zijn aangebracht.~~

_\*~~Onder gehandicapte wordt verstaan een persoon die ten gevolge van ziekte of gebrek aantoonbare beperkingen ondervindt.~~_

~~Buiten de waardering blijven voorzieningen ten behoeve van een gehandicapte, waarvoor subsidie is verstrekt waarmee de volledige kosten worden gedekt. Extra vloeroppervlakte (als bedoeld in de subsidieregelingen) wordt aangemerkt als gesubsidieerde voorziening.~~

~~Het komt voor dat een voorziening slechts ten dele werd beschouwd als een specifieke aanpassing voor een gehandicapte en daarom slechts ten dele is gesubsidieerd. In zo’n geval worden alleen die onderdelen van de voorziening gewaardeerd, die ook in een vergelijkbare woning als standaardvoorziening voorkomen.~~

~~Indien de huurovereenkomst met de gehandicapte is beëindigd dan vervalt de toepassing van deze rubriek, tenzij de nieuwe huurder tevens gehandicapt is.~~

### ~~7.3 Vergoeding kosten~~

~~Per € 332,00 netto-investering door de verhuurder (dus het bedrag dat overblijft na aftrek van subsidie en eigen bijdrage van de huurder) wordt één punt toegekend. Voorwaarde is wel dat de kosten in een redelijke verhouding staan tot de geboden kwaliteit. De wetgever gaat ervan uit dat met deze puntenwaardering de verhuurder een redelijke rendementswaarborg heeft voor het door hem geïnvesteerde vermogen (te weten de kosten van de ingrepen, verminderd met de eigen bijdrage van de huurder en de financiële tegemoetkoming van gemeente of (bij dure woonvoorzieningen) enige instantie die ingevolge een wettelijke regeling die tegemoetkoming verleent.~~

## Rubriek 8 Buitenruimten

### 8.1 Puntentoekenning

* Voor privé-buitenruimten worden in ieder geval 2 punten toegekend en vervolgens per vierkante meter 0,35 punt.  

    _Voorbeeld: 10 vierkante meter privé-buitenruimte levert 5,5 punt op (2 + 10 x 0,35)._  

* Voor gemeenschappelijk buitenruimten worden 0,75 per vierkante meter toegekend, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.  

    _Voorbeeld: een woongebouw met een gemeenschappelijk dakterras van 30 m2 waartoe drie adressen toegang hebben, wordt gewaardeerd met: (0,75 x 30) / 3 = 7,5._
* Een aftrek van 5 punten wordt toegepast als de woning in het geheel geen privé-buitenruimte, gemeenschappelijk buitenruimte of loggia heeft.

> Hoewel deze zin suggereert dat de loggia niet valt onder privé-buitenruimte of gemeenschappelijke buitenruimte, gaan wij er vanuit dat de loggia wel onder één van beide categorieën valt en dat loggia in deze zin op een ongelukkige manier is toegevoegd om te benadrukken dat een loggia een buitenruimte is.

* Maximaal 15 punten worden toegekend voor buitenruimten.

### 8.2 Definitie privé-buitenruimte

~~Privé-buitenruimte zijn tot de woning behorende buitenruimten, waarvan de huurder van de desbetreffende woning volgens de huurovereenkomst het exclusieve gebruiksrecht en toegang heeft.~~ Dit kunnen onder meer voor-, zij- of achtertuinen, balkons, platjes of terrassen zijn, maar ook een oprit exclusief behorende tot de woning. Wanneer zich binnen de privé-buitenruimte een parkeerplek bevindt, geldt de parkeerplek en de weg daar naartoe als privé-buitenruimte. Gemeenschappelijke parkeerruimten worden gewaardeerd volgens rubriek 10.

Met exclusief gebruiksrecht van privé-buitenruimte wordt bedoeld dat uitsluitend de huurder het recht heeft om te bepalen welk gebruik hij maakt van de privé-buitenruimten die tot de woning behoren.

Voor de privé-buitenruimte geldt geen minimumafmeting.

### 8.3 Definitie gemeenschappelijke buitenruimte

Gemeenschappelijke buitenruimten hebben een minimumafmeting van 2 m x 1,5 m, 1,5 m (hoogte, breedte, diepte) en zijn tot het woongebouw behorende buitenruimten waar de bewoners van tenminste twee adressen ~~in het woongebouw volgens de huurovereenkomst exclusieve toegang en~~ gebruiksrecht toe hebben. ~~De huurder(s) moet(en) daarnaast toegang hebben tot de gemeenschappelijke buitenruimte zonder gebruikmaking van vertrekken, overige ruimten of verkeersruimten die uitsluitend ter beschikking staan aan de verhuurder of aan (een) andere huurder(s). Gedeelde buitenruimten die als parkeerplek bedoeld zijn, worden gewaardeerd volgens rubriek 10.~~

Hieronder wordt ook verstaan een gebruiksrecht dat toekomt aan een collectief van huurders, maar waarbij het gebruiksrecht in feite exclusief voor de huurder is omdat de huurder het gebruik door derden kan weren.

### 8.4 Balkons, dakterrassen en loggia’s

~~Balkons, dakterrassen en loggia’s moeten aan de volgende eisen voldoen om voor punten in aanmerking te komen. Ze zijn:~~

* ~~voorzien van een beloopbare afwerking, zoals vlonders, tegels e.d.;~~
* ~~rondom voorzien van een afscheiding die tevens dient als valbeveiliging; en~~
* ~~via een deur\* of schuifpui toegankelijk zijn.~~


\* _~~Indien het balkon of dakterras is voorzien van beweegbare ramen en/of deuren in de gevel, die bestemd zijn om als toegang tot de buitenruimte te worden gebruikt, dan wordt het balkon of het terras met punten gewaardeerd.~~_

Franse balkons worden niet als buitenruimten beschouwd. Een Frans balkon is een opening in de gevel met naar binnen draaiende deuren, voorzien van een balustrade direct tegen het kozijn of de gevel. ~~Zeembalkons worden, zolang zij voldoen aan de hiervoor aangegeven eisen van een balkon, wel gewaardeerd als buitenruimte.~~

### 8.5 Meetinstructies

~~Van de buitenruimten wordt de gehele onbebouwde oppervlakte gemeten, gemeten loodrecht op de voor-, achter of zijgevel. Bij balkons wordt gemeten vanaf de binnenzijde van het balkonhek. Bij (gedeeltelijk) inpandige balkons wordt bovendien gemeten ten opzichte van het terugliggende deel van de gevel.~~

~~Als uitzondering op de regel voor het meten van de gehele onbebouwde oppervlakte, wordt de oppervlakte, die wordt ingenomen door een balkonkast of kolenhok e.d., bij de oppervlakte van de desbetreffende buitenruimte meegerekend.~~

### 8.6 Puntenberekening en saldering

De oppervlakten voor privé en gemeenschappelijke buitenruimten worden afzonderlijk berekend. Als sprake is van meerdere buitenruimten die tot dezelfde categorie behoren (privé of gemeenschappelijk) dan wordt per categorie de oppervlakte van die meerdere buitenruimtes opgeteld (afgerond op twee decimalen). En daarna wordt de oppervlakte van beide categorieën bij elkaar opgeteld.

In totaal kan maximaal 15 punten worden toegekend.

## Rubriek 9 Gemeenschappelijke vertrekken, overige ruimten en voorzieningen

### 9.1 Puntentoekenning

* Een gemeenschappelijk vertrek wordt gewaardeerd met 1 punt per vierkante meter, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.
* Een gemeenschappelijke overige ruimte wordt gewaardeerd met 0,75 punt per vierkante meter, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.
* Voorzieningen (verkoeling en verwarming, keuken, sanitair~~, gehandicaptenvoorziening~~) die zich bevinden in gemeenschappelijke vertrekken en overige ruimten worden gewaardeerd conform het woningwaarderingsstelsel, gedeeld door het aantal adressen.

> Het aantal adressen dient doorgegeven te worden op het attribuut `gedeeld_met_aantal_eenheden`, waarbij de eenheid zelf meegeteld dient te worden in het totaal. Een waarde van 2 of hoger wordt geïnterpreteerd als een gemeenschappelijke ruimte.

**Warme maaltijden**

Indien het verstrekken van warme maaltijden onderdeel vormt van de huurovereenkomst dan worden ook de aanwezige gemeenschappelijke (spoel)keuken en bijbehorende opslagruimte in de waardering meegenomen. Het gaat hier om de puntenwaardering van de oppervlakte van die ruimten, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

> Indien dit zo is, geef bijvoorbeeld een `keuken` mee met `gedeeld_met_aantal_eenheden`.

**Gemeenschappelijke ruimten en voorzieningen in een zorgwoning**

De ervaring leert dat bij het waarderen van de gemeenschappelijke ruimten en voorzieningen in een zorgwoning of woon/zorgcomplex de waardering per woning veelal uitkomt op een totaal van ongeveer 3 punten. Om arbeidsintensief meetwerk te voorkomen waardeert de Huurcommissie in dat geval een waardering van 3 punten per woning.

### 9.2 Definitie gemeenschappelijke vertrekken en overige ruimten

Gemeenschappelijke vertrekken en overige ruimten zijn tot het woongebouw behorende binnenruimten waarvan de bewoners van tenminste twee adressen in het woongebouw volgens de huurovereenkomst exclusieve toegang en gebruiksrecht hebben. ~~De huurder(s) moet(en) daarnaast toegang hebben tot de gemeenschappelijke binnenruimte zonder gebruikmaking van vertrekken, overige ruimten of verkeersruimten die uitsluitend ter beschikking staan aan de verhuurder of aan (een) andere huurder(s).~~

~~Uitgesloten zijn vertrekken en overige ruimten waarvoor ook door derden een vergoeding/huurprijs wordt betaald alsmede vertrekken en ruimten die door de eigenaar/verhuurder in gebruik zijn (bijv. kantoor- ruimte, opslagruimte, e.d.).~~

Gemeenschappelijke bergingen worden gewaardeerd als overige ruimte als:

* ~~zij binnen het woongebouw liggen of tot de onroerende aanhorigheden behoren;~~
* ~~de vergoeding daarvoor in de huurprijs van de woning is begrepen;~~
* de oppervlakte, na deling door het aantal adressen, per woning minstens 2m2 bedraagt.

De toekenning van punten bij een gemeenschappelijke berging is als volgt: totale oppervlakte, afronden in m2, delen door het aantal adressen en waarderen als “overige ruimte”. Kasten worden meegeteld, mits zij voldoen aan de voorwaarden als genoemd in paragraaf 2.2. Dat betekent dat kasten uitkomend in een verkeersruimte worden niet meegeteld.

Met vertrekken en overige ruimten wordt onder deze rubriek voor het overige aangesloten bij de definities en meetinstructies zoals toegelicht in paragraaf 1.3 en 2.3 van dit hoofdstuk.

### 9.3 Rekenmethode en voorbeeldberekening

_Rekenmethode_

1. Bepaal of het een vertrek of een overige ruimte is en bereken de oppervlaktepunten:
    1. Gemeenschappelijke vertrekken worden met 1 punt per m2 gewaardeerd.
    2. Gemeenschappelijke overige ruimten worden met 0,75 punt per m2 gewaardeerd.
2. Bepaal de punten voor verkoeling en verwarming conform rubriek 3.
3. Bepaal eventueel van toepassing zijnde extra punten conform rubriek 5, 6 en/of 7.
4. Saldeer de punten uit de hierboven genoemde stappen.
5. Deel het aantal punten door het aantal adressen dat toegang heeft tot de gemeenschappelijke binnenruimten.

Voorbeeld

1. _Ruimte A voldoet aan de eisen van een vertrek en wordt gewaardeerd met 20 x 1 punt (oppervlakte) conform rubriek ‘vertrek’. Ruimte B voldoet aan de eisen van een overige ruimte en wordt gewaardeerd met 1,5 (2 x 0,75) punt conform rubriek ‘overige ruimte’._
2. _Vertrek A is verwarmd middels een radiator en krijgt daarvoor 2 punten conform rubriek ‘verkoeling en verwarming’. De toiletruimte is onverwarmd en ontvangt daarvoor geen punten._
3. _In vertrek A wordt voldaan aan de minimumeisen van een keuken conform rubriek ‘keuken’. Voor deze rubriek wordt 10 punten toegekend (7 voor het aanrecht, en 3 voor de extra voorzieningen). De toiletruimte B krijgt 4,75 punt (3,75 voor het hangend toilet en 1 voor de wastafel)._
4. _Saldering levert op: 20 + 1,5 + 2 + 10 + 4,75 = 38,25._
5. _Delen door het aantal adressen levert op: 38,25 punten / 4 = 9.5625 per adres._
6. _Afronden geschiedt op een kwart punt per adres, in dit geval dus op 9,50._

> Voor ons is het niet helemaal duidelijk op basis van de tekst en de voorbeeldrekening hoe het zit met de maximering op punten. Wij zijn er vanuit gegaan dat ook de maximering van de hoeveelheid punten gedeeeld moet worden door het aantal adressen. Bijvoorbeeld maximaal 0.75 punten voor kastruimte in de badruimte wordt met toegang van twee adressen ~0.38.

## Rubriek 10 Gemeenschappelijke parkeerruimten

### 10.1 Puntentoekenning

> Bij het rekenvoorbeeld aan het einde van deze rubriek wordt uitgelegd hoe de woningwaardering package te gebruiken is om een eenheid te waarderen op de rubriek gemeenschappelijke parkeerruimten.

Voor verschillende typen gemeenschappelijke parkeerplekken, afhankelijk van afdekking van de buitenlucht, worden punten toegekend:

* Type I: parkeerplek in afgesloten parkeergarage behorende tot het complex krijgt 9 punten, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.
* Type II: parkeerplek buiten behorende tot het complex of de woning met dak krijgt 6 punten, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft. Hieronder wordt ook begrepen een carport.
* Type III: parkeerplek buiten behorende tot het complex of de woning zonder dak krijgt 4 punten, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft.

2 extra punten worden toegekend, gedeeld door het aantal adressen dat toegang en gebruiksrecht heeft, als de parkeerplek beschikt over een laadpaal voor elektrisch rijden, en exclusief is voor gebruik door bewoners.

> Onderstaande `Ruimtedetailsoorten` corresponderen met bovenstaande parkeerplek types:
>
> * Type I: `Ruimtedetailsoort.parkeervak_auto_binnen` met code `VAI`
> * Type II: `Ruimtedetailsoort.carport` met code `CAR`
> * Type III: `Ruimtedetailsoort.parkeervak_auto_buiten_niet_overdekt` met code `VAU`

### 10.2 Definitie gemeenschappelijke parkeerruimte

Een gemeenschappelijke parkeerruimte is een ruimte die toegankelijk is voor bewoners van tenminste twee adressen die daar exclusief gebruiksrecht op hebben, waarin zich tenminste één parkeerplek bevindt (zoals een gemeenschappelijke parkeergarage onder een wooncomplex of een gemeenschappelijke parkeerplaats buiten met één of meerdere parkeerplekken). De parkeerplek mag niet openbaar te gebruiken zijn, maar moet bij een complex of adres horen en in de huurovereenkomst moet exclusief gebruiksrecht zijn toegekend.

Een parkeerruimte waartoe bewoners van één adres op grond van de huurovereenkomst exclusieve toegang hebben, wordt gewaardeerd volgens rubriek 2,  (bijvoorbeeld een garagebox behorende tot de woning) of rubriek 8 (bijvoorbeeld een oprit exclusief behorende tot de woning).

Een parkeerplek is een afgebakend vak en heeft een oppervlakte van minimaal 12m2 waarin een gangbare personenauto in zijn geheel past. Een afgebakend vak betekent dat het kenbaar moet zijn waar zich een parkeerplek bevindt. Dit kan bijvoorbeeld door een bord, al dan niet in combinatie met lijnmarkeringen op de grond of een bepaald type of kleur tegel om het vak af te kaderen.

### 10.3 Onroerende aanhorigheid

Punten voor een parkeervoorziening worden alleen toegekend als deze als onroerende aanhorigheid gekwalificeerd wordt. Hiervan is sprake als de parkeervoorziening naar haar aard onlosmakelijk verbonden is met de woonruimte (bijvoorbeeld wanneer de parkeerplek direct in verbinding staat met de woonruimte of tot het adres of complex behoort, zoals bij een gemeenschappelijke oprit of gemeenschappelijke garage) of omdat de parkeervoorziening volgens verkeersopvatting onderdeel of krachtens de huurovereenkomst deel uitmaakt van de gehuurde woning.

Hiervan is sprake als  in de huurovereenkomst is afgesproken dat de parkeervoorziening tot de onroerende zaak behoort en de woonruimte en parkeerplaats verhuurd moeten zijn zonder dat ze van elkaar contractueel te scheiden zijn. Als de parkeerplek geen onroerende aanhorigheid betreft, heeft de verhuurder de mogelijkheid dit als los goed te verhuren volgens artikel 7:201 BW.

### 10.4 Rekenmethode en voorbeeldberekening

_Rekenmethode_

1. Bepaal tot welk type de parkeerplek behoort (dus type I, II of III, zie hierboven).
2. Als er sprake is van een laadpaal voor exclusief gebruik door de bewoners, geldt twee punten extra per parkeerplek met laadpaal.
3. Bij meerdere parkeerplekken worden de punten bij elkaar opgeteld.
4. Daarna wordt dit puntentotaal gedeeld door het aantal adressen dat gebruik kan maken van de parkeerplek(ken). Indien sprake is van een privé parkeerplek voor één adres, wordt gedeeld door 1.

_Voorbeeldberekening_

Tien adressen delen vijf type II-parkeerplekken met laadpaal en twee type III-parkeerplekken zonder laadpaal.

1. Vijf parkeerplekken type II (zes punten) + elke een laadpaal (twee punten) en twee parkeerplekken type III (4 punten) = 5 x (6+2)+ 2 x 4 = 48.
2. 48 / 10 adressen = 4,8 per adres.
3. Afronden geschiedt op een kwart punt per adres, in dit voorbeeld dus op 4,75.

> Omdat de woningwaardering package op eenheidniveau de punten voor het woningwaarderingstelsel berekent, is het niet mogelijk om `Ruimtedetailsoort.parkeergarage` en `Ruimtedetailsoort.parkeerterrein` te waarderen. Deze twee ruimtedetailsoorten maken bovenstaande berekening, waarbij de verschillende types geteld worden, met het huidige VERA-model te complex. Om punten te krijgen voor deze rubriek moeten de type parkeervakken los worden ingeschoten. Daartoe is het attribuut `Eenhedenruimte.aantal` als uitbreiding op het VERA-model toegevoegd. Hierdoor is het mogelijk om aan te geven hoeveel van bovenstaande parkertypes de eenheid toegang heeft zonder dat elk parkeervak van een parkeergarage of parkeerterrein meegegeven dient te worden. Daarnaast is ook `Eenhedenruimte.gedeeld_met_aantal_eenheden` als uitbreiding toegevoegd. Dit attribuut dient ook op elk type parkeerplek meegegeven te worden. Om bovenstaand rekenvoorbeeld door de woningwaardering package te laten berekenen, kunnen de gemeenschappelijke parkeerplekken als volgt (in JSON-formaat) meegegeven worden.

```json
{
  "id": "12006000004",
  "ruimten": [
    {
      "id": "1",
      "gedeeld_met_aantal_eenheden": 10,
      "aantal": 5,
      "soort": {
        "code": "PAR",
        "naam": "Parkeergelegenheid"
      },
      "detailSoort": {
        "code": "CAR",
        "naam": "Carport"
      },
      "naam": "Carport",
      "oppervlakte": 12,
      "breedte": 3,
      "lengte": 4,
      "bouwkundigeElementen": [
        {
          "id": "laadpaal_1",
          "naam": "Laadpaal",
          "soort": {
            "code": "Voo",
            "naam": "Voorziening"
          },
          "detailSoort": {
            "code": "LAA",
            "naam": "Laadpaal"
          }
        }
      ]
    },
    {
      "id": "2",
      "gedeeld_met_aantal_eenheden": 10,
      "aantal": 2,
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

> Let op: in bovenstaand voorbeeld, wanneer een laadpaal als bouwkundig element wordt meegegeven, wordt deze bij de ruimte ook keer het `Eenhedenruimte.aantal` meegeteld voor het berekenen van de punten. In bovenstaand voorbeeld wordt de laadpaal dus vijf (5) keer meegeteld.

## Rubriek 11 Punten voor de WOZ-waarde

Een groot deel van het totale puntenaantal wordt bepaald door de punten die een woonruimte krijgt voor de WOZ-waarde van het gehuurde. WOZ staat voor Wet waardering onroerende zaken. De WOZ-waarde geeft de geschatte marktwaarde van de woning weer zoals volgt uit de Wet waardering onroerende zaken. Deze waarde wordt in principe ieder kalenderjaar door de gemeente vastgesteld, die in de WOZ-beschikking van de desbetreffende woning wordt weergegeven. De waardepeildatum van de WOZ-waarde ligt op 1 januari van het voorafgaande kalenderjaar. Ter illustratie: de WOZ-waarde in de WOZ-beschikking van 2024 heeft een waardepeildatum van 1 januari 2023.

Als geen relevante WOZ-waarde bekend is, kan als alternatief 85% van de taxatiewaarde van de woning worden gebruikt volgend uit een door een Register-Taxateur opgesteld (hybride)taxatierapport. De verhuurder draagt de verantwoordelijkheid voor het opstellen (op laten stellen) van dit rapport. Als de verhuurder geen taxatierapport heeft aangeleverd, dan wordt met de minimum WOZ-waarde gerekend.

> In bovenstaand geval dient het alternatief van 85% van de taxatiewaarde als een WOZ-waarde in het datamodel opgegeven te worden.

### 11.1 Berekening punten voor de WOZ-waarde

Op basis van de WOZ-waarde vindt een berekening plaats die een puntenaantal oplevert voor de woningwaardering. Hiervoor worden kengetallen gebruikt die ieder jaar opnieuw worden vastgesteld door de minister.[^4] De kengetallen van de afgelopen drie jaar staan in tabel 1 hieronder weergegeven.

De berekening voor het puntenaantal op basis van de WOZ-waarde bestaat uit twee onderdelen.

Onderdeel I:

* 1 punt wordt gegeven voor iedere € 15.329 van de laatstelijk vastgestelde WOZ-waarde met **peildatum 1 januari 2024**, taxatiewaarden en minimumwaarden;
* 1 punt wordt gegeven voor iedere € 14.543 van de laatstelijk vastgestelde WOZ-waarde met **peildatum 1 januari 2023**.

Dus afhankelijk van in welk jaar de WOZ-waarde laatstelijk is vastgesteld, wordt gerekend met € 15.329 (1 januari 2024) of € 14.543 (1 januari 2023).

De taxatiewaarden worden toegepast in geval geen relevante WOZ-waarde bekend is. De minimumwaarden worden toegepast ingeval geen relevante WOZ-waarde en geen taxatiewaarde bekend is.

Onderdeel II:

* 1 punt wordt gegeven voor iedere € 242 van de WOZ-waarde, taxatiewaarden en minimumwaarden met **peildatum 1 januari 2024** per m2
* 1 punt wordt gegeven voor iedere € 229 van de WOZ-waarde met **peildatum 1 januari 2023** per m2 .

Hiervoor geldt dus hetzelfde als bij Onderdeel I: afhankelijk van de peildatum van de laatstelijk vastgestelde WOZ-waarde wordt gerekend met € 242 of € 229.

De taxatiewaarden worden toegepast in geval geen relevante WOZ-waarde bekend is. De minimumwaarden worden toegepast ingeval geen relevante WOZ-waarde en geen taxatiewaarde bekend is.

In dit onderdeel van de berekening dient ook het aantal m2 van parkeerplekken uit rubriek 10, voor zover het een parkeerplek type I (een parkeerplek in een afgesloten parkeergarage behorende tot het complex) betreft, te worden meegenomen. Hiervoor kan de standaard maatvoering van 12 m2 per plaats gehanteerd worden.

> Wij gaan er vanuit dat de oppervlakte van de parkeerplekken ook nog gedeeld moet worden door het aantal adressen dat toegang heeft tot de parkeerplek, omdat er anders onredelijk veel punten kunnen worden toegewezen voor parkeerplekken. Wij hanteren geen standaardmaat van 12m2, omdat een parkeerplek Type I kleiner dan12m2 niet onder rubriek 10 valt.

De punten van de twee onderdelen worden bij elkaar opgeteld. Dit levert een puntenaantal op voor het onderdeel WOZ-waarde.

_Rekenvoorbeeld_:

_De WOZ-waarde van een woning is voor het kalenderjaar 2024 vastgesteld op € 300.000, met peildatum 1 januari 2023, en de oppervlakte van de vertrekken en overige ruimten van de woning is 60 m2._

* _Onderdeel I: € 300.000 / € 14.543 = 20,63 punten_
* _Onderdeel II: € 300.000 / 60 (m2) / € 229 = 21,83 punten_

_Het totale puntenaantal is 20,63 + 21,83 = 42,46. Na afronding is het puntenaantal 42,5 punten. In dit rekenvoorbeeld zijn de kengetallen gebruikt die per 1 juli 2024 gelden, zie tabel 1 hieronder._

[^4]: Deze kengetallen worden jaarlijks per 1 januari geïndexeerd met de gemiddelde verandering van de WOZ-waarde en staan vermeld in de jaarlijkse circulaire ‘huurprijsbeleid’.

### 11.2 Nieuwbouwwoningen en woningen gelegen in COROP-gebied Amsterdam of Utrecht

Om de bouw van huurwoningen in de middensector te bevorderen heeft de wetgever bepaald dat voor nieuwbouwwoningen opgeleverd in kalenderjaar 2015-2019 en kleine nieuwbouwwoningen (<40 m2) gelegen in COROP-regio’s Amsterdam en Utrecht een andere berekening geldt. Deze berekening leidt tot een hoger aantal punten voor het onderdeel WOZ-waarde.

**Nieuwbouwwoningen 2015-2019**

Indien de bouwkundige oplevering of hoogniveau renovatie van de woning heeft plaatsgevonden in de jaren 2015-2019 en die woning voor de onderdelen 1 t/m 10 en 12 van het woningwaarderingsstelsel minimaal 110 punten heeft behaald dan worden, voor het aantal punten voor de WOZ-waarde, minimaal 40 punten toegekend. Dit garandeert een minimaal puntenaantal.

> In de versie januari 2025 van het beleidsboek staat nergens meer gedefinieerd wat hoogniveau renovatie is. Hierom passen we deze regeling niet specifiek toe voor 'hoogniveau renovatie'.

Indien de bouwkundige oplevering plaatsvindt ná het kalenderjaar 2019 en/of de woning behaalt niet de 110 punten op basis van de overige onderdelen van het puntenstelsel dan geldt de ‘gewone’ berekening die in de paragraaf hierboven is weergegeven.

Deze regeling komt te vervallen per 2039.

**~~Woningen gelegen in COROP-gebied (2018-2022)~~**

~~Indien de bouwkundige oplevering of hoogniveau renovatie van een woning, die kleiner is dan 40 m2, heeft plaatsgevonden in de jaren 2018-2022 en de woning is gelegen in de Corop-gebieden7 Amsterdam en Utrecht, dan wordt het puntenaantal voor de WOZ-waarde berekend op basis van een ander kengetal dan wat in de paragraaf hierboven is weergegeven. In het tweede onderdeel van de berekening wordt de WOZ-waarde gedeeld door het aantal m2 van de oppervlaktes van de woning, gedeeld door het kengetal € 229 (peildatum 1 januari 2023). Bij kleine nieuwbouwwoningen (<40 m2) gelegen in COROP-regio’s Amsterdam en Utrecht wordt dan niet het kengetal € 229 gebruikt maar € 97 bij de peildatum 1 januari 2023. Bij de peildatum 1 januari 2022 wordt niet het bedrag van € 222 gebruikt, maar € 94.~~

~~Indien de bouwkundige oplevering plaatsvindt ná het kalenderjaar 2022 of de woning is groter dan 40 m2 of de woning is niet gelegen in de COROP-gebieden Amsterdam en Utrecht, dan geldt de ‘gewone’ berekening die in de paragraaf hierboven is weergegeven.~~

~~In bijlage 3 van dit beleidsboek staan de gemeenten opgesomd die zijn gelegen in de COROP-gebieden Amsterdam en Utrecht.~~

~~Deze regeling komt te vervallen per 2042.~~

~~7 Corop-gebied is een statistische eenheid ontworpen door de Coördinatie Commissie Regionaal Onderzoeksprogramma. Dit gebied betreft een cluster van één of meer aangrenzende gemeenten in dezelfde provincie, ontworpen voor regionaal onderzoek.  ~~
 

_~~Rekenvoorbeeld:~~_

_~~De WOZ-waarde van een woning in Amsterdam is voor het kalenderjaar 2024, met peildatum 1 januari 2023, vastgesteld op € 300.000 en de oppervlakte van de vertrekken en overige ruimten van de woning is 35 m2.~~_

*   _~~Onderdeel I: € 300.000 / € 14.453 = 20,76 punten~~_
*   _~~Onderdeel II: € 300.000 / 35 (m2) / € 97 = 88,37 punten~~_

_~~Het totale puntenaantal is 20,76 + 88,37 = 109,13. Na afronding is het puntenaantal 109 punten. In dit rekenvoorbeeld zijn de kengetallen gebruikt met peildatum 1 januari 2023, zie tabel 1 hieronder.~~_

_Tabel 1 Kengetallen WOZ_

| Peildatum | Onderdeel I | Onderdeel II | Onderdeel II bij kleine nieuwbouwwoningen in Corop-gebieden Amsterdam en Utrecht |
| --- | --- | --- | --- |
| Per 1 januari 2020 | € 11.041 | € 172 | € 73 |
| Per 1 januari 2021 | € 12.090 | € 189 | € 80 |
| Per 1 januari 2022 | € 14.146 | € 222 | € 94 |
| Per 1 januari 2023 | € 14.453 | € 229 | € 97 |
| Per 1 januari 2024 | € 15.329 | € 242 | € 103 |

### 11.3 Ontbreken WOZ-waarde en minimumwaarde

Als geen relevante WOZ-waarde bekend is, kan als alternatief 85% van de taxatiewaarde van de woning worden gebruikt volgend uit een door een Register-Taxateur opgesteld (hybride)taxatierapport. De verhuurder draagt de verantwoordelijkheid voor het opstellen van dit rapport. De taxatiewaarde geldt totdat een WOZ-waarde is vastgesteld en vervalt voor toepassing van deze rubriek. Als de verhuurder geen taxatierapport heeft aangeleverd dan wordt met de minimum WOZ-waarde gerekend.

_Minimumwaarde_

De minimum WOZ-waarde wordt ook gebruikt voor specifieke woningen van specifieke verhuurders, zoals ‘containerwoningen’ die zijn bestemd voor studentenhuisvesting. In die gevallen wordt een minimum WOZ-waarde gehanteerd indien de WOZ-waarde lager is dan deze minimumwaarde. Deze waarde met peildatum 1 januari 2023 bedraagt € 73.607. Zie de tabel hieronder voor de minimumwaarde van de afgelopen jaren.

_Tabel 2_

| Peildatum | Minimumwaarde |
| --- | --- |
| Per 1 januari 2021 | € 61.198 |
| Per 1 januari 2022 | € 71.602 |
| Per 1 januari 2023 | € 73.607 |
| Per 1 januari 2024 | € 77.582 |

**Tijdelijke woning**

In geval van een tijdelijke woning hanteert de register-taxateur de objectafbakeningsvoorschriften en waarderingsvoorschriften van hoofdstuk III van de Wet WOZ met uitzondering van de voorschriften op grond van artikel 17, vierde lid, en artikel 18, eerste en tweede lid, van de Wet WOZ. In plaats van de voorschriften van artikel 18, eerste en tweede lid, gaat de register-taxateur uit van de staat van de woning na oplevering.

Onder tijdelijke woning wordt voor deze rubriek een woning verstaan die voor een bepaalde tijd op een tijdelijke locatie (met toegelaten functie wonen of tijdelijke afwijking Omgevingsplan) mogen worden gebouwd. Dit zijn woningen die voldoen aan de eisen die gelden voor nieuwbouw óf die getoetst zijn aan tijdelijke woningen zoals gedefinieerd in het Besluit bouwwerken leefomgeving (termijn van ten hoogste 15 jaar).

### 11.4 Gebouwd eigendom in aanbouw

~~Indien de WOZ-waarde betrekking heeft op een ‘gebouwd eigendom in aanbouw’, als bedoeld in artikel 17 lid 4 Wet WOZ, dan wordt voor de puntentoekenning uitgegaan van de waarde van de woning als ware de bouw is voltooid. De WOZ-beschikking zal het voortgangspercentage vermelden. De Huurcommissie heeft dan tot taak de WOZ-waarde gerelateerd aan de voortgang van de aanbouw om te rekenen naar de waarde “als ware de bouw voltooid”, dus naar 100%.~~

~~Onder een ‘gebouwd eigendom in aanbouw’ wordt verstaan een onroerende zaak of gedeelte daarvan waarvoor een omgevingsvergunning is verleend en die door bouw nog niet geschikt is voor gebruik overeenkomstig haar beoogde bestemming. Het gaat hier om de situatie waarbij nieuwbouw/verbouw is begonnen na 1 januari van een lopend jaar en die niet is afgerond voor 1 januari van het daaropvolgende jaar.~~

~~Hiervan is bijvoorbeeld sprake als, in het kader van de WOZ-beschikking 2023 dat als peildatum 1 januari 2022 heeft, de werkzaamheden aan het gehuurde zijn aangevangen na 1 januari 2022 en zijn voltooid ná 1 januari 2023. De WOZ-beschikking 2024, dat als peildatum 1 januari 2023 heeft, zal in dat geval niet de waarde weergeven “als ware de bouw voltooid”. In dat geval kan de woning worden aangemerkt als ‘een gebouwd eigendom in aanbouw’ als bedoeld in artikel 17 lid 4 Wet WOZ en moet de Huurcommissie de waarde omrekenen naar 100%.~~

> Wanneer sprake is van gebouwd eigendom in aanbouw, dient de naar 100% omgerekende WOZ-waarde met de juiste waardepeildatum doorgegeven te worden.

### 11.5 Maximering WOZ-punten tot maximaal 33%

Het aandeel van de WOZ-waarde in de puntenwaardering is gemaximeerd. Hierbij geldt dat maximaal 33% van het totale puntenaantal van een woning bepaald mag worden door de WOZ-waarde van de woning. Dit wordt ook wel de ‘cap op de WOZ’ genoemd. Deze regeling is van toepassing voor zowel nieuwe als bestaande huurcontracten.

Wanneer een woning zonder de cap op de WOZ een waardering heeft van meer dan 186 punten en door deze beperking een waardering krijgt die lager is dan 187 punten, geldt een waardering van 186 punten voor de woning.

**Uitzonderingen**

Deze beperking geldt echter niet voor woningen waarvan de waardering zonder die beperking lager is dan 187 punten~~ en voor kleine nieuwbouwwoningen 8 (<40 m2) gelegen in COROP-regio’s Amsterdam en Utrecht die zijn opgeleverd in de jaren 2018-2022~~.

Daarnaast wordt in nog twee andere gevallen de cap op de WOZ niet toegepast. In het geval dat de minimumwaarde is toegepast vindt namelijk ook geen aftopping plaats aangezien de WOZ-waarde niet meer dan 33% zal bedragen. Het tweede geval gaat het om nieuwbouwwoningen gebouwd in de jaren 2015-2019 waarvoor minimaal 110 punten zijn behaald voor de onderdelen 1 tot en met 10 en 12 van het woningwaarderingsstelsel. Ook in dat geval wordt de cap op de WOZ niet toegepast. In deze situatie wordt minimaal 40 punten voor het onderdeel WOZ-waarde toegekend en dit komt overeen met 26,6%, waardoor geen aftopping plaatsvindt. Deze gevallen zijn niet expliciet in de wet uitgezonderd, omdat het puntenaantal voor de WOZ-waarde rekenkundig, in deze gevallen, nooit meer dan 33% kan bedragen. Daarom zijn ze niet opgenomen in onderstaand schema.

8 Hieronder vallen ook gerenoveerde woningen waarbij de energieprestatie voldoet aan de eisen van artikel 5.2 van het Bouwbesluit 2012 die gelden voor nieuwbouwwoningen. 

_Rekenvoorbeelden_

_**Rekenvoorbeeld 1**: door toepassing van de cap op de WOZ wordt het aantal punten in rubriek WOZ-waarde verlaagd van 134 naar 66. Het totale puntenaantal blijft boven de 187 punten._

|     | **WOZ-punten** | **Punten in de overige rubrieken** | **Totaal puntenaantal** | **Te liberaliseren?** |
| --- | --- | --- | --- | --- |
| Zonder toepassing van de cap op de WOZ | 134 (= 50%) | 134 (= 50%) | 268 punten (= 100%) | Ja  |
| Met toepassing van de cap op de WOZ | 66 (= 33%) | 134 (= 67%) | 200 punten (= 100%) | Ja  |

De cap op de WOZ geldt niet voor woningen waarvan de waardering zonder die beperking lager is dan 187 punten. Deze regel wordt toegepast het volgende rekenvoorbeeld.

_**Rekenvoorbeeld 2**: de cap op de WOZ wordt niet toegepast, omdat het puntenaantal lager is dan 187 (namelijk 160). De WOZ-punten mogen een groter aandeel hebben dan 33%._

|     | **WOZ-punten** | **Punten in de overige rubrieken** | **Totaal puntenaantal** | **Te liberaliseren?** |
| --- | --- | --- | --- | --- |
| Zonder toepassing van de cap op de WOZ | 80 (= 50%) | 80 (= 50%) | 160 punten (= 100%) | Nee |
| Omdat de woning minder dan 187 punten heeft, wordt de cap op de WOZ niet toegepast. Het aantal blijft 160 punten. |     |     |     | Nee |

Indien met toepassing van de cap het puntenaandeel voor de WOZ-waarde wordt beperkt op ten hoogste 33%, wordt het aantal punten voor de WOZ-waarde afgerond naar beneden op hele punten. Wanneer een woning zonder die beperking een waardering heeft van meer dan 186 punten en door deze beperking een waardering krijgt die lager is dan 187 punten, geldt een waardering van 186 punten voor de woning.

_**Rekenvoorbeeld 3**: door toepassing van de cap op de WOZ krijgt de woning een puntenaantal lager dan 187 punten (namelijk 162 punten). Wanneer een woning zonder die beperking een waardering heeft van meer dan 186 punten en door deze beperking een waardering krijgt die lager is dan 187 punten, daarom geldt een waardering van 186 punten voor de woning._

|     | **WOZ-punten** | **Punten in de overige rubrieken** | **Totaal puntenaantal** | **Te liberaliseren?** |
| --- | --- | --- | --- | --- |
| Zonder toepassing van de cap op de WOZ | 109 ( = 50%) | 109 (= 50%) | 218 punten (= 100%) | Ja  |
| Met toepassing van de cap op de WOZ | 53,7 ( = 33%), afgerond 53 | 109 ( = 67%) | 162 punten (= 100%) | Nee |
| De nieuwe waardering is lager dan 187 punten, dus geldt: |     |     | 186 punten | Nee |

### 11.6 Cohortensystematiek

Voor de toepassing van de WOZ-waarde geldt een cohortensystematiek. Dit betekent dat de peildatum van de WOZ-waarde bepaalt met welke getallen er dient te worden gerekend volgens deze rubriek. Als bijvoorbeeld een WOZ-beschikking 2024 is afgegeven met peildatum 1 januari 2023 dan gelden de kengetallen die horen bij peildatum 1 januari 2023, zie tabel 1 en 2 hierboven.

## Rubriek 12 Bijzondere voorzieningen: zorgwoning en aanbelfunctie

### 12.1 Zorgwoning

Als sprake is van een zorgwoning, dan wordt het puntentotaal van de rubrieken 1 tot en met 11 van het woningwaarderingsstelsel met 35% verhoogd. Dit resulteert in een hogere maximale huurprijs. Dit resulteert in een hogere maximale huurprijs en telt daarom mee in het bepalen van de sector waarin de woonruimte valt. 

> De onderstaande doorgehaalde voorwaarden worden niet gecontroleerd door de woningwaardering package. Wanneer een eenheid de doelgroep Zorg heeft, wordt de woning automatisch als zorgwoning gewaardeerd.

**~~Voorwaarden zorgwoning~~**

~~Er is sprake van een zorgwoning als aan de volgende vijf voorwaarden is voldaan.~~

1. **~~De zorgwoning betreft een zelfstandige woning~~**  
    ~~Hoe het begrip zelfstandige woning door de Huurcommissie wordt ingevuld is te vinden in paragraaf 2.3.1 van dit beleidsboek.~~    
2. **~~De zelfstandige woning is gelegen in een woongebouw~~**  

3. **~~De woning en het woongebouw waarin de woning is gelegen zijn bestemd voor mensen met een fysieke beperking~~**  
    ~~Dat de woning en het woongebouw bestemd zijn voor mensen met een fysieke beperking moet in ieder geval blijken uit een a) drempelloze toegankelijkheid en b) doorgankelijkheid.~~  

    ~~Deze drempelloze toegankelijkheid en doorgankelijkheid houden tenminste in dat alle gangen, waar de bewoners doorheen moeten om de eigen woning en andere relevante (gemeenschappelijke) ruimten in het woongebouw te bereiken, een minimale breedte hebben van 1,2 m. Bovendien moet er sprake zijn van een lift of hellingbaan indien de eigen woning en andere relevante ruimten drempels hebben van 2 cm of hoger.~~  
 

4. **~~De huurovereenkomst\* van de woning voorziet op de aanwezigheid van technische voorzieningen in het gebouw die het mogelijk maken dat een individuele persoonsalarmering verbinding kan maken met de noodalarmcentrale in zowel de woning als het complex waarvan de woning deel uitmaakt.~~**  
    ~~Het woongebouw moet zodanig zijn uitgerust dat een afgegeven persoonsalarm door individuele persoonsalarmering overal verbinding kan maken met de noodalarmcentrale in zowel de woning als het complex waarvan de woning deel uitmaakt. Het moet dus bijvoorbeeld ook mogelijk zijn, dat de uitrusting in het gebouw in staat moet zijn om een persoonsalarm op te vangen indien dat uit de lift van het complex wordt verzonden, of uit de tot het complex behorende buitenruimte.~~  

    ~~Voorbeelden van technische voorzieningen zijn een noodoproepinstallatie of een persoonlijk alarmsysteem dat op de persoon wordt gedragen met een halskoord.~~  

5. **~~De huurovereenkomst\* van de woning moet zien op het gebruik van gemeenschappelijke ruimten voor maaltijden of recreatie~~**  
    ~~Het gebruik van gemeenschappelijke ruimten voor maaltijden of recreatie moet deel uitmaken van een huurovereenkomst om een woning als zorgwoning te kunnen kwalificeren in de zin van het Besluit huurprijzen woonruimte. Deze ruimten dienen tot het woongebouw te behoren of als onroerende aanhorigheid van het complex te kunnen worden aangemerkt. Het exclusieve gebruik van deze ruimten door de huurders van het woongebouw is geen vereiste. Wel dienen de ruimten primair ter beschikking te staan aan de huurders van het woongebouw.~~  

    ~~Als de gemeenschappelijke ruimten voor maaltijden of recreatie niet binnen hetzelfde maar geheel of gedeeltelijk in een naastgelegen (woon)gebouw zijn gelegen, dienen deze voorzieningen binnendoor (gesloten loopbrug, corridor, etc.) bereikbaar te zijn om als zorgwoning in de zin van het Besluit huurprijzen woonruimte te kwalificeren.~~  

    _~~\* Indien sprake is van een gemengde woon-zorgovereenkomst dan is het woningwaarderingsstelsel, waaronder de toeslag die geldt bij een zorgwoning, alleen van toepassing indien het huurelement in de gemengde overeenkomst overheerst.~~_

### 12.2 Aanbelfunctie met video- en audioverbinding

Een aanbelfunctie met video- en audioverbinding waarbij de voordeur automatisch kan worden geopend vanuit de woning wordt gewaardeerd met 0,25 punt.

Hieronder wordt een systeem verstaan dat tweewegcommunicatie mogelijk maakt met beeld en geluid tussen degene die aanbelt en een aanwezige in de woonruimte. Daarbij dient er tevens sprake te zijn van de mogelijkheid tot het openen van de (gemeenschappelijke) voordeur vanuit de woonruimte (op afstand) die toegang geeft tot het complex waarvan de woning onderdeel uitmaakt.

### 12.3 Laadpalen

Een laadpaal voor elektrisch rijden die exclusief bestemd is voor gebruik door de bewoners, wordt gewaardeerd met 2 punten. Dit geldt alleen als de laadpaal bestemd is voor het elektrisch opladen van een gemotoriseerd voertuig, niet zijnde een bromfiets, fiets met trapondersteuning of gehandicaptenvoertuig.

In geval een gemeenschappelijke parkeerruimte beschikt over een laadpaal, wordt voor de berekeningswijze aangesloten bij Rubriek 10.
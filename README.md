![](https://img.shields.io/pypi/pyversions/woningwaardering)
![Build Status](https://github.com/woonstadrotterdam/woningwaardering/actions/workflows/cicd.yml/badge.svg)
[![Version](https://img.shields.io/pypi/v/woningwaardering)](https://pypi.org/project/woningwaardering/)
![](https://img.shields.io/github/license/woonstadrotterdam/woningwaardering)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Woningwaardering

> ⚠️ Release v3.x.x kan gebruikt worden voor het berekenen van de woningwaardering volgens het woningwaarderingsstelsel voor zelfstandige woonruimten volgens [het beleidsboek van de huurcommissie van januari 2025 (Wet Betaalbare Huur)](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken_html). Aan de berekeningen en output van deze package kunnen geen rechten worden ontleend. Raadpleeg de [README](https://github.com/woonstadrotterdam/woningwaardering#), [de toelichting op de implementatie van het beleidsboek](https://github.com/woonstadrotterdam/woningwaardering/tree/main/docs/implementatietoelichting-beleidsboeken) en [de openstaande issues](https://github.com/woonstadrotterdam/woningwaardering/issues) aandachtig om de package op een constructieve manier te gebruiken en de resultaten correct te interpreteren.

![voorbeeld-output](https://raw.githubusercontent.com/woonstadrotterdam/woningwaardering/main/docs/afbeeldingen/voorbeeld_output.jpg)
_Visueel voorbeeld van de output van de package voor een zelfstandige woonruimte._

📊 **Status**

![](https://progress-bar.xyz/100/?title=zelfstandige_woonruimten_jan_2025&width=120)  
![](https://progress-bar.xyz/100/?title=onzelfstandige_woonruimten_jan_2025&width=108)

Het Microservices team van Woonstad Rotterdam is in Q1 2024 begonnen met het ontwikkelen met een open-source Python-package waarmee het mogelijk wordt om het puntensysteem van het [woningwaarderingsstelsel](https://aedes.nl/huurbeleid-en-betaalbaarheid/woningwaarderingsstelsel-wws) toe te passen. We gaan hierbij uit van de [VERA-standaard](https://www.coraveraonline.nl/index.php/VERA-standaard) [[referentiedata v4.1.241004](https://github.com/Aedes-datastandaarden/vera-referentiedata), [openapi v4.1.5](https://github.com/Aedes-datastandaarden/vera-openapi)] van de corporatiesector voor de in- en output van de package. Dit project heeft drie hoofddoelen:

- het mogelijk maken van het berekenen van de woningwaardering op basis van een digitale representatie van een woning:
  - steeds meer woningcorperaties en bedrijven digitaliseren hun woningbestand, bijvoorbeeld met behulp van een bouwwerkinformatiemodel (BIM).
  - de combinatie van digitale representaties van woningen en deze package maakt het mogelijk om de woningwaardering in bulk te berekenen.
  - door deze package als API te gebruiken kan de woningwaardering in een webapplicatie worden geïntegreerd.
- om tot een completere en inzichtelijkere woningwaarderingsstelsel-berekening te komen dan die nu beschikbaar zijn via tools zoals bijvoorbeeld die van de [huurcommissie](https://www.huurcommissie.nl/huurders/sociale-huurwoning/maximale-huurprijs-berekenen).
- om als woningcorporatie of bedrijf te blijven voldoen aan de wetging zoals [Wet Betaalbare Huur](https://www.volkshuisvestingnederland.nl/onderwerpen/wet-betaalbare-huur).

---

![werking-package](https://raw.githubusercontent.com/woonstadrotterdam/woningwaardering/main/docs/afbeeldingen/diagram.png)
_Voorbeeld van hoe wij de woningwaardering package gebruiken bij Woonstad Rotterdam_.

---

Voor meer details over wat er precies is geïmplementeerd van het beleidsboek van januari 2025 verwijzen wij naar de [documentatie](https://github.com/woonstadrotterdam/woningwaardering/blob/main/docs/implementatietoelichting-beleidsboeken/) over de implementatie van dit beleidsboek.
Voor meer informatie over hoe documentatie van het beleidsboek is gemaakt, verwijzen wij naar het hoofdstuk [Implementatie beleidsboek huurcommissie](https://github.com/woonstadrotterdam/woningwaardering?tab=readme-ov-file#implementatie-beleidsboek-huurcommissie) in deze `README`.

Voor vragen kunt u contact opnemen met Team Microservices via [Tomer Gabay](mailto:tomer.gabay@woonstadrotterdam.nl), [Tiddo Loos](mailto:tiddo.loos@woonstadrotterdam.nl) of [Ben Verhees](mailto:ben.verhees@woonstadrotterdam.nl).

## Inhoudsopgave

- [Woningwaardering](#woningwaardering)
  - [Inhoudsopgave](#inhoudsopgave)
  - [1. Opzet woningwaardering-package](#1-opzet-woningwaardering-package)
    - [Implementatie beleidsboek huurcommissie](#implementatie-beleidsboek-huurcommissie)
    - [Repository-structuur](#repository-structuur)
    - [Design](#design)
    - [Lookup tabellen](#lookup-tabellen)
    - [Warnings](#warnings)
      - [Warning vs Exception](#warning-vs-exception)
    - [Installatie](#installatie)
      - [Monumenten](#monumenten)
    - [Gebruik](#gebruik)
      - [Optie 1; bijvoorbeeld via JSON bestand](#optie-1-bijvoorbeeld-via-json-bestand)
      - [Optie 2; via Python zelf](#optie-2-via-python-zelf)
  - [2. Datamodel uitbreidingen](#2-datamodel-uitbreidingen)
    - [Ruimtedetailsoort kast](#ruimtedetailsoort-kast)
    - [Verbonden ruimten](#verbonden-ruimten)
    - [Gedeeld met aantal eenheden](#gedeeld-met-aantal-eenheden)
    - [Bouwkundige elementen](#bouwkundige-elementen)
    - [Verkoeld en verwarmd](#verkoeld-en-verwarmd)
    - [Datum afsluiten huurovereenkomst](#datum-afsluiten-huurovereenkomst)
    - [Aanbelfunctie met video- en audioverbinding](#aanbelfunctie-met-video--en-audioverbinding)
    - [Installaties](#installaties)
    - [Aantal](#aantal)
    - [Parkeergelegenheden](#parkeergelegenheden)
  - [3. Contributing](#3-contributing)
    - [Setup](#setup)
    - [Naamgeving van classes](#naamgeving-van-classes)
      - [Genereren opzet woningwaarderingstelsels en -groepen](#genereren-opzet-woningwaarderingstelsels-en--groepen)
      - [Stelsels](#stelsels)
      - [Stelselgroepen](#stelselgroepen)
    - [Releasemanagement](#releasemanagement)
      - [Versienummering](#versienummering)
      - [Releaseproces](#releaseproces)
    - [Testing](#testing)
      - [Test coverage rapport](#test-coverage-rapport)
      - [Conventies voor tests](#conventies-voor-tests)
      - [Test modellen](#test-modellen)
    - [Logger Guidelines](#logger-guidelines)
    - [Datamodellen](#datamodellen)
      - [Datamodellen uitbreiden](#datamodellen-uitbreiden)
    - [Referentiedata](#referentiedata)

## 1. Opzet woningwaardering-package

### Implementatie beleidsboek huurcommissie

Voor het berekenen van een woningwaardering worden de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) voor de waarderingstelsels voor zelfstandige en onzelfstandige woningen gevolgd.
De beleidsboeken van de Huurcommissie Nederland volgen Nederlandse wet- en regelgeving zoals beschreven in [Artikel 14 van het "Besluit huurprijzen woonruimte"](https://wetten.overheid.nl/BWBR0003237/2024-01-01#Artikel14).

Om berekeningen te maken met betrekking tot een woningwaardering wordt het gepubliceerde beleid vertaald naar Python-code.
Een woningwaardering wordt gemaakt op basis van woningelementen.
De stelselgroepen waarop gescoord wordt, zijn vastgelegd in het [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP) op www.coraveraonline.nl.
Deze worden aangehouden in de opzet van de `woningwaardering`-package.
Voor elke stelselgroep wordt een apart Python-object gemaakt met een naam die overeenkomt met [woningwaarderingstelselgroep](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP).

De woningwaardering package volgt de [beleidsboeken van de Nederlandse Huurcommissie](https://www.huurcommissie.nl/huurcommissie-helpt/beleidsboeken) en daarmee de Nederlandse wet en regelgeving m.b.t. het waarderen van woningen. Tijdens de ontwikkeling van deze package komt het voor dat we inconsistenties in de beleidsboeken vinden of dat er ruimte is voor interpretatie. Daarnaast kan het voorkomen dat dat de VERA modellen, met eventuele uitbreidingen, niet toereikend zijn om de stelselgroep voglens het beleidsboek tot op de letter nauwkeurig te implementeren. In [implementatietoelichting-beleidsboeken](https://github.com/woonstadrotterdam/woningwaardering/tree/main/docs/implementatietoelichting-beleidsboeken) onderbouwen wij hoe elke stelselgroep is geïmplementeerd en welke keuzes daarin gemaakt zijn.  
In deze documenten wordt bijgehouden welke onderdelen van het beleidsboek wel en niet zijn geïmplementeerd per stelselgroep. De gepubliceerde tekst uit het beleidsboek wordt gekopieerd en wanneer een onderdeel niet in de code van de package is geïmplementeerd zal dit worden aangegeven met ~~doorgestreepte tekst~~.  
De reden van het niet implementeren van een regelonderdeel is vrijwel altijd dat het technisch niet mogelijk is op basis van het inputmodel van de VERA-standaard. Een voorbeeld hiervan is dat voor oppervlakte van vertrekken de minimale breedte van een vertrek over de volledige lengte 1,5m moet zijn. Omdat wij de data van de minimale breedte over de volledige lengte niet binnenkrijgen via het inputmodel kunnen wij dit onderdeel van de regel niet implementeren. **Dit betekent dat het aan de gebruiker is om met deze regelonderdelen rekening te houden bij het eenheid-inputmodel.** Een deel van de deze regelonderdelen wordt al afgevangen indien het eenheid-inputmodel voldoet aan de NEN-norm.
Regels die wel zijn geïmplementeerd zijn niet doorgestreept.
Keuzes die zijn gemaakt en of interpretaties die zijn gedaan, worden in een gemarkeerd blok weergegeven zoals hieronder is gedaan.

> Dit is een tekstblok waarmee commentaar van een developer wordt aangegeven in het beleidsboek.

### Repository-structuur

De repository-structuur is ingedeeld volgens de [referentiedata van stelselgroepen van de VERA-standaard](https://www.coraveraonline.nl/index.php/Referentiedata:WONINGWAARDERINGSTELSELGROEP); eerst de stelsels (bijvoorbeeld _zelfstandig_, _onzelfstandig_) en vervolgens de stelselgroepen (bijvoorbeeld _Energieprestatie_, _Wasgelegenheid_).
In de folders van de stelselgroepen bevindt zich de code voor het berekenen van de punten per stelselgroep. Indien bepaalde logica voor zowel zelfstandige als onzelfstandige woningen gelden, dan bevinden deze regels zich in de folder _gedeelde_logcia_.

### Design

Het design van de `woningwaardering`-package is zo gekozen dat stelselgroep-objecten en bijbehorende regels modulair zijn.

### Lookup tabellen

In lookup tabellen worden constanten en variabelen opgeslagen die nodig zijn bij het berekenen van de punten voor een stelselgroep.
In de `woningwaardering` package wordt CSV gebruikt als bestandstype voor het opslaan van een lookup tabel.
De keuze is op CSV gevallen omdat lookup data soms bestaat uit meerdere datarijen waardoor dit vaak minder leesbaar wordt wanneer dit bijvoorbeeld in json of yaml wordt opgeslagen.

### Warnings

In de `woningwaardering` package worden `UserWarnings` gegenereerd wanneer de inputdata niet volledig of correct wordt aangeleverd.
Deze waarschuwingen worden gegeven met een warning bericht en een type warning, bijvoorbeeld:

```python
warnings.warn("Dit is een warning", UserWarning)
```

Standaard genereert de `woningwaardering` package een error wanneer een `UserWarning` wordt gegeven.
Hoewel de package kan werken met incomplete data, is ervoor gekozen om standaard te falen bij incomplete inputdata, zodat de gebruiker hiervan op de hoogte wordt gebracht.
Het is echter ook mogelijk om het warning filter terug te zetten naar de standaardinstellingen, waardoor een warning m.b.t. incomplete data niet leidt tot een error, maar slechts een _warning_:

```python
warnings.simplefilter("default", UserWarning)
```

Alle waarschuwingen die worden gegenereerd met `warnings.warn()`, worden standaard gelogd met `logger.warning()` en weergegeven in het standaardfout bestand.
Mocht door de gebruiker logging worden uitgezet, dan zullen de UserWarnings altijd te zien zijn voor de gebruiker in de output van de _stderr_.

#### Warning vs Exception

Er wordt doorgaans in de stelgroepversies gebruik gemaakt van `warnings.warn()` in plaats van het raisen van een exception.
Hierdoor bestaat de mogelijkheid om stelselgroepen te berekenen voor stelselgroepen waarvoor de data wel compleet genoeg is, mits de `warnings.simplefilter` naar `default` is gezet.

#### Criterium ID's

De `CriteriumId` class wordt gebruikt om ID's te genereren voor criteria in de woningwaardering. Deze ID's worden opgebouwd uit verschillende onderdelen die worden samengevoegd met dubbele underscores (`__`).

De opbouw van een criterium ID kan de volgende onderdelen bevatten:

- Stelselgroep (verplicht, bijvoorbeeld 'buitenruimten' of 'energieprestatie')
- Ruimte ID (optioneel, bijvoorbeeld 'Space_108014713')
- Criterium (optioneel, bijvoorbeeld 'factor_II' of 'woz_waarde')
- Gedeeld met aantal (optioneel, voor gedeelde voorzieningen)
- Gedeeld met soort (optioneel, 'adressen' of 'onzelfstandige_woonruimten')
- Totaal indicator (optioneel)

Voorbeelden van gegenereerde ID's:

- `buitenruimten__Space_108014713` (voor een specifieke ruimte)
- `buitenruimten__totaal__prive` (voor een privé totaal)
- `gemeenschappelijke_binnenruimten_gedeeld_met_meerdere_adressen__totaal__gedeeld_met__4__adressen` (voor gedeelde voorzieningen)

Bij gedeelde voorzieningen wordt automatisch 'prive' toegevoegd als het aantal 1 of minder is, en anders wordt het aantal en soort toegevoegd (bijvoorbeeld `gedeeld_met__4__adressen`).

Met deze ID's kan gerefereerd worden aan specifieke criteria in de output van de woningwaardering.

#### Criteriumsleutels

Bij sommige stelselgroepen heb je een aantal criteria die een gemeenschappelijke groep vormen. Bijvoorbeeld bij _verkoeling en verwarming_ mag je maximaal 2 extra punten krijgen voor vertrekken die verkoeld én verwarmd zijn. Daarnaast mag je ook maximaal 4 punten krijgen voor het aantal verwarmde overige- en verkeersruimten. Om te kunnen berekenen wat de som is van een subgroep en bijvoorbeeld maximering toe te passen maken wij gebruik van zogenoemde `criteriumSleutels`. Indien een waardering onderdeel is van een subgroep, dan wordt aan deze waardering in het veld `bovenliggendCriterium` de `id` toegevoegd van de waardering die hoort bij de subgroep. In het voorbeeld hieronder is bijvoorbeeld de subgroep `Verwarmde vertrekken` binnen `verkoeling en verwarming` duidelijk te zien in de output-tabel. Voorgedefinieerde criteriumsleutels vind je in `woningwaardering/stelsels/criteriumsleutels.py`. Momenteel ondersteunen wij nog geen meerdere niveau's van subgroepen. Een criterium dat voor een ander criterium een bovenliggend criterium is, mag zelf geen bovenliggend criterium hebben.

### Installatie

Installeer de package met `pip install woningwaardering`. Vervolgens kun je de package importeren en gebruiken op verschillende manieren.

#### Monumenten

De woningwaardering package kan op basis van data van het Kadaster en Cultureel Erfgoed de monumentale status van een woning bepalen. Deze functionaliteit is optioneel en kan worden geïnstalleerd met `pip install woningwaardering[monumenten]`.

### Gebruik

#### Optie 1; bijvoorbeeld via JSON bestand

```python
import warnings
from datetime import date

from woningwaardering import Woningwaardering
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheidbericht,
)
from woningwaardering.stelsels.utils import naar_tabel

warnings.simplefilter("default", UserWarning)

wws = Woningwaardering(
    peildatum=date(2025, 1, 1)  # bij niet meegeven wordt de huidige dag gebruikt.
)
with open(
    "tests/data/generiek/input/37101000032.json",
    "r+",
) as file:
    eenheid = EenhedenEenheidbericht.model_validate_json(file.read())

    # Woningwaardering class kiest op basis van de input het zelfstandig of onzelfstandige stelsel.
    woningwaardering_resultaat = wws.waardeer(eenheid)
    print(
        woningwaardering_resultaat.model_dump_json(
            by_alias=True, indent=2, exclude_none=True
        )
    )
    tabel = naar_tabel(woningwaardering_resultaat)

    print(tabel)
```

<details>
<summary>Voorbeeld output in JSON</summary>

```json
{
  "groepen": [
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OVZ",
          "naam": "Oppervlakte van vertrekken"
        }
      },
      "punten": 141.0,
      "woningwaarderingen": [
        {
          "aantal": 21.05,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014589",
            "naam": "Slaapkamer 1",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 41.0,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108010632",
            "naam": "Woonkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 20.37,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108006229",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 7.5,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014563",
            "naam": "Badruimte",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 15.98,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108017433",
            "naam": "Slaapkamer 2",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 19.15,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108017431",
            "naam": "Slaapkamer 3",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 15.82,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014593",
            "naam": "Slaapkamer 4",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OOZ",
          "naam": "Oppervlakte van overige ruimten"
        }
      },
      "punten": 5.25,
      "woningwaarderingen": [
        {
          "aantal": 6.65,
          "criterium": {
            "id": "oppervlakte_van_overige_ruimten__Space_108017427",
            "naam": "Berging",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 14.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014589",
            "naam": "Slaapkamer 1",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108010632",
            "naam": "Woonkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108006229",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014563",
            "naam": "Badruimte",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108017433",
            "naam": "Slaapkamer 2",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108017431",
            "naam": "Slaapkamer 3",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014593",
            "naam": "Slaapkamer 4",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          },
          "punten": 14.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BUI",
          "naam": "Buitenruimten"
        }
      },
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "aantal": 3.14,
          "criterium": {
            "id": "buitenruimten__Space_108014713",
            "naam": "Balkon 1",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 1.1
        },
        {
          "aantal": 3.14,
          "criterium": {
            "id": "buitenruimten__Space_108010812",
            "naam": "Balkon 2",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 1.1
        },
        {
          "aantal": 49.11,
          "criterium": {
            "id": "buitenruimten__Space_108006357",
            "naam": "Tuin",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 17.19
        },
        {
          "aantal": 15.93,
          "criterium": {
            "id": "buitenruimten__Space_108006467",
            "naam": "Dakterras",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 5.57
        },
        {
          "criterium": {
            "id": "buitenruimten__aanwezig__prive",
            "naam": "Buitenruimten aanwezig",
            "bovenliggendeCriterium": {
              "id": "buitenruimten__totaal__prive"
            }
          },
          "punten": 2.0
        },
        {
          "aantal": 71.32,
          "criterium": {
            "id": "buitenruimten__totaal__prive",
            "naam": "Totaal (privé)",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          },
          "punten": 26.96
        },
        {
          "criterium": {
            "id": "buitenruimten__maximering",
            "naam": "Maximaal 15 punten"
          },
          "punten": -11.96
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "ENE",
          "naam": "Energieprestatie"
        }
      },
      "punten": 22.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "C (Energie-index)"
          },
          "punten": 22.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "KEU",
          "naam": "Keuken"
        }
      },
      "punten": 7.0,
      "woningwaarderingen": [
        {
          "aantal": 2700.0,
          "criterium": {
            "id": "keuken__Space_108006229__lengte_aanrecht_Aanrecht_108006231",
            "naam": "Keuken: Lengte aanrecht",
            "meeteenheid": {
              "code": "MIL",
              "naam": "Millimeter"
            }
          },
          "punten": 7.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "SAN",
          "naam": "Sanitair"
        }
      },
      "punten": 15.0,
      "woningwaarderingen": [
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108014563__staand_toilet",
            "naam": "Badruimte - Staand Toilet"
          },
          "punten": 2.0
        },
        {
          "aantal": 2.0,
          "criterium": {
            "id": "sanitair__Space_108014563__wastafel",
            "naam": "Badruimte - Wastafel"
          },
          "punten": 2.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108014563__bad_en_douche",
            "naam": "Badruimte - Bad en douche"
          },
          "punten": 7.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108006223__staand_toilet",
            "naam": "Toiletruimte - Staand Toilet"
          },
          "punten": 3.0
        },
        {
          "aantal": 1.0,
          "criterium": {
            "id": "sanitair__Space_108006223__wastafel",
            "naam": "Toiletruimte - Wastafel"
          },
          "punten": 1.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GPA",
          "naam": "Gemeenschappelijke parkeerruimten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GVR",
          "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "WOZ",
          "naam": "Punten voor de WOZ-waarde"
        }
      },
      "punten": 63.0,
      "woningwaarderingen": [
        {
          "aantal": 643000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2023"
          }
        },
        {
          "aantal": 14543.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__factor_I",
            "naam": "Factor I",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_I"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__totaal__onderdeel_I",
            "naam": "Onderdeel I"
          },
          "punten": 44.21
        },
        {
          "aantal": 147.52,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__oppervlakte_vertrekken_en_overige_ruimten",
            "naam": "Oppervlakte van vertrekken en overige ruimten",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 229.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__factor_II",
            "naam": "Factor II",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II",
            "naam": "Onderdeel II"
          },
          "punten": 19.03
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BIJ",
          "naam": "Bijzondere voorzieningen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "PMN",
          "naam": "Prijsopslag monumenten en nieuwbouw"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 1820.52,
  "punten": 282.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1820.52
}
```

</details>

<details>
<summary>Voorbeeld output in tabel</summary>

```text
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Groep                             | Naam                                                                        |       Aantal | Meeteenheid         |  Punten |  Opslag |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Slaapkamer 1                                                                |        21.05 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Woonkamer                                                                   |        41.00 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Keuken                                                                      |        20.37 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Badruimte                                                                   |         7.50 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Slaapkamer 2                                                                |        15.98 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Slaapkamer 3                                                                |        19.15 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Slaapkamer 4                                                                |        15.82 | Vierkante meter, m2 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Totaal                                                                      |       140.87 | Vierkante meter, m2 |  141.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van overige ruimten   | Berging                                                                     |         6.65 | Vierkante meter, m2 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van overige ruimten   | Totaal                                                                      |         6.65 | Vierkante meter, m2 |    5.25 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Verwarmde vertrekken                                                        |              |                     |   14.00 |         |
| Verkoeling en verwarming          |  - Slaapkamer 1                                                             |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Woonkamer                                                                |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Keuken                                                                   |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Badruimte                                                                |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Slaapkamer 2                                                             |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Slaapkamer 3                                                             |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Slaapkamer 4                                                             |              |                     |  [2.00] |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Totaal                                                                      |              |                     |   14.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Buitenruimten                     | Totaal (privé)                                                              |        71.32 | Vierkante meter, m2 |   26.96 |         |
| Buitenruimten                     |  - Balkon 1                                                                 |       [3.14] | Vierkante meter, m2 |  [1.10] |         |
| Buitenruimten                     |  - Balkon 2                                                                 |       [3.14] | Vierkante meter, m2 |  [1.10] |         |
| Buitenruimten                     |  - Tuin                                                                     |      [49.11] | Vierkante meter, m2 | [17.19] |         |
| Buitenruimten                     |  - Dakterras                                                                |      [15.93] | Vierkante meter, m2 |  [5.57] |         |
| Buitenruimten                     |  - Buitenruimten aanwezig                                                   |              |                     |  [2.00] |         |
| Buitenruimten                     | Maximaal 15 punten                                                          |              |                     |  -11.96 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Buitenruimten                     | Totaal                                                                      |              |                     |   15.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Energieprestatie                  | C (Energie-index)                                                           |              |                     |   22.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Keuken: Lengte aanrecht                                                     |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Totaal                                                                      |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Sanitair                          | Badruimte - Staand Toilet                                                   |         1.00 |                     |    2.00 |         |
| Sanitair                          | Badruimte - Wastafel                                                        |         2.00 |                     |    2.00 |         |
| Sanitair                          | Badruimte - Bad en douche                                                   |         1.00 |                     |    7.00 |         |
| Sanitair                          | Toiletruimte - Staand Toilet                                                |         1.00 |                     |    3.00 |         |
| Sanitair                          | Toiletruimte - Wastafel                                                     |         1.00 |                     |    1.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Sanitair                          | Totaal                                                                      |              |                     |   15.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | WOZ-waarde op waardepeildatum 01-01-2023                                    |   [643000.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel I                                                                 |              |                     |   44.21 |         |
| Punten voor de WOZ-waarde         |  - Factor I                                                                 |    [14543.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel II                                                                |              |                     |   19.03 |         |
| Punten voor de WOZ-waarde         |  - Oppervlakte van vertrekken en overige ruimten                            |     [147.52] | Vierkante meter, m2 |         |         |
| Punten voor de WOZ-waarde         |  - Factor II                                                                |      [229.0] |                     |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | Totaal                                                                      |              |                     |   63.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Zelfstandige woonruimten          | Afgerond totaal                                                             |              |                     |  282.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
|                                   | Maximale huur                                                               |      1820.52 | EUR                 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
```

</details>

#### Optie 2; via Python zelf

```python
from datetime import date

from woningwaardering import Woningwaardering
from woningwaardering.stelsels.utils import naar_tabel
from woningwaardering.vera.bvg.generated import (
    BouwkundigElementenBouwkundigElement,
    EenhedenAdresseerbaarObjectBasisregistratie,
    EenhedenEenheidbericht,
    EenhedenEenheidadres,
    EenhedenEnergieprestatie,
    EenhedenPand,
    EenhedenRuimte,
    EenhedenWoonplaats,
    EenhedenWozEenheid,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Bouwkundigelementsoort,
    Energielabel,
    Energieprestatiesoort,
    Energieprestatiestatus,
    Pandsoort,
    Ruimtedetailsoort,
    Ruimtesoort,
    Woningwaarderingstelsel,
)

wws = Woningwaardering(peildatum=date(2025, 1, 1))

eenheid = EenhedenEenheidbericht(
    id="<id>",
    bouwjaar=1924,
    woningwaarderingstelsel=Woningwaarderingstelsel.zelfstandige_woonruimten,
    adres=EenhedenEenheidadres(
        straatnaam="<straatnaam>",
        huisnummer="<huisnummer>",
        huisnummer_toevoeging="",
        postcode="<postcode>",
        woonplaats=EenhedenWoonplaats(naam="ROTTERDAM"),
    ),
    adresseerbaar_object_basisregistratie=EenhedenAdresseerbaarObjectBasisregistratie(
        id="0599010000485697", bag_identificatie="0599010000485697"
    ),
    panden=[
        EenhedenPand(
            soort=Pandsoort.eengezinswoning,
        )
    ],
    woz_eenheden=[
        EenhedenWozEenheid(
            waardepeildatum=date(2022, 1, 1), vastgestelde_waarde=618000
        ),
        EenhedenWozEenheid(
            waardepeildatum=date(2023, 1, 1), vastgestelde_waarde=643000
        ),
    ],
    energieprestaties=[
        EenhedenEnergieprestatie(
            soort=Energieprestatiesoort.energie_index,
            status=Energieprestatiestatus.definitief,
            begindatum=date(2019, 2, 25),
            einddatum=date(2029, 2, 25),
            registratiedatum="2019-02-26T14:51:38+01:00",
            label=Energielabel.c,
            waarde="1.58",
        )
    ],
    gebruiksoppervlakte=187,
    monumenten=[],
    ruimten=[
        EenhedenRuimte(
            id="Space_108014589",
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.slaapkamer,
            naam="Slaapkamer",
            inhoud=60.4048,
            oppervlakte=21.047,
            verwarmd=True,
        ),
        EenhedenRuimte(
            id="Space_108006229",
            soort=Ruimtesoort.vertrek,
            detail_soort=Ruimtedetailsoort.keuken,
            naam="Keuken",
            inhoud=57.4359,
            oppervlakte=20.3673,
            verwarmd=True,
            bouwkundige_elementen=[
                BouwkundigElementenBouwkundigElement(
                    id="Aanrecht_108006231",
                    naam="Aanrecht",
                    omschrijving="Aanrecht in Keuken",
                    soort=Bouwkundigelementsoort.voorziening,
                    detail_soort=Bouwkundigelementdetailsoort.aanrecht,
                    lengte=2700,
                )
            ],
        ),
    ],
)

woningwaardering_resultaat = wws.waardeer(eenheid)
print(
    woningwaardering_resultaat.model_dump_json(
        by_alias=True, indent=2, exclude_none=True
    )
)
tabel = naar_tabel(woningwaardering_resultaat)

print(tabel)
```

De output daarvan is een VERA woningwaarderingstelsel object. Dit object kan vervolgens worden omgezet naar een tabel zoals hierboven is gedaan.

<details>
<summary>Voorbeeld output in JSON</summary>

```json
{
  "groepen": [
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OVZ",
          "naam": "Oppervlakte van vertrekken"
        }
      },
      "punten": 41.0,
      "woningwaarderingen": [
        {
          "aantal": 21.05,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108014589",
            "naam": "Slaapkamer",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 20.37,
          "criterium": {
            "id": "oppervlakte_van_vertrekken__Space_108006229",
            "naam": "Keuken",
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "OOZ",
          "naam": "Oppervlakte van overige ruimten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "VKV",
          "naam": "Verkoeling en verwarming"
        }
      },
      "punten": 4.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108014589",
            "naam": "Slaapkamer",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__Space_108006229",
            "naam": "Keuken",
            "bovenliggendeCriterium": {
              "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken"
            }
          },
          "punten": 2.0
        },
        {
          "criterium": {
            "id": "verkoeling_en_verwarming__totaal__verwarmde_vertrekken",
            "naam": "Verwarmde vertrekken"
          },
          "punten": 4.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BUI",
          "naam": "Buitenruimten"
        }
      },
      "punten": -5.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "buitenruimten__geen_buitenruimten",
            "naam": "Geen buitenruimten"
          },
          "punten": -5.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "ENE",
          "naam": "Energieprestatie"
        }
      },
      "punten": 22.0,
      "woningwaarderingen": [
        {
          "criterium": {
            "id": "energieprestatie__label",
            "naam": "C (Energie-index)"
          },
          "punten": 22.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "KEU",
          "naam": "Keuken"
        }
      },
      "punten": 7.0,
      "woningwaarderingen": [
        {
          "aantal": 2700.0,
          "criterium": {
            "id": "keuken__Space_108006229__lengte_aanrecht_Aanrecht_108006231",
            "naam": "Keuken: Lengte aanrecht",
            "meeteenheid": {
              "code": "MIL",
              "naam": "Millimeter"
            }
          },
          "punten": 7.0
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "SAN",
          "naam": "Sanitair"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GPA",
          "naam": "Gemeenschappelijke parkeerruimten"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "GVR",
          "naam": "Gemeenschappelijke vertrekken, overige ruimten en voorzieningen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "WOZ",
          "naam": "Punten voor de WOZ-waarde"
        }
      },
      "punten": 112.0,
      "woningwaarderingen": [
        {
          "aantal": 643000.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__woz_waarde",
            "naam": "WOZ-waarde op waardepeildatum 01-01-2023"
          }
        },
        {
          "aantal": 14543.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__factor_I",
            "naam": "Factor I",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_I"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__totaal__onderdeel_I",
            "naam": "Onderdeel I"
          },
          "punten": 44.21
        },
        {
          "aantal": 41.42,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__oppervlakte_vertrekken_en_overige_ruimten",
            "naam": "Oppervlakte van vertrekken en overige ruimten",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II"
            },
            "meeteenheid": {
              "code": "M2",
              "naam": "Vierkante meter, m2"
            }
          }
        },
        {
          "aantal": 229.0,
          "criterium": {
            "id": "punten_voor_de_woz_waarde__factor_II",
            "naam": "Factor II",
            "bovenliggendeCriterium": {
              "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II"
            }
          }
        },
        {
          "criterium": {
            "id": "punten_voor_de_woz_waarde__totaal__onderdeel_II",
            "naam": "Onderdeel II"
          },
          "punten": 67.79
        }
      ]
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "BIJ",
          "naam": "Bijzondere voorzieningen"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": []
    },
    {
      "criteriumGroep": {
        "stelsel": {
          "code": "ZEL",
          "naam": "Zelfstandige woonruimten"
        },
        "stelselgroep": {
          "code": "PMN",
          "naam": "Prijsopslag monumenten en nieuwbouw"
        }
      },
      "punten": 0.0,
      "woningwaarderingen": [],
      "opslagpercentage": 0.0
    }
  ],
  "maximaleHuur": 1151.72,
  "punten": 181.0,
  "stelsel": {
    "code": "ZEL",
    "naam": "Zelfstandige woonruimten"
  },
  "huurprijsopslag": 0.0,
  "maximaleHuurInclusiefOpslag": 1151.72
}
```

</details>

<details>
<summary>Voorbeeld output in tabel</summary>

```text
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Groep                             | Naam                                                                        |       Aantal | Meeteenheid         |  Punten |  Opslag |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Slaapkamer                                                                  |        21.05 | Vierkante meter, m2 |         |         |
| Oppervlakte van vertrekken        | Keuken                                                                      |        20.37 | Vierkante meter, m2 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Oppervlakte van vertrekken        | Totaal                                                                      |        41.42 | Vierkante meter, m2 |   41.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Verwarmde vertrekken                                                        |              |                     |    4.00 |         |
| Verkoeling en verwarming          |  - Slaapkamer                                                               |              |                     |  [2.00] |         |
| Verkoeling en verwarming          |  - Keuken                                                                   |              |                     |  [2.00] |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Verkoeling en verwarming          | Totaal                                                                      |              |                     |    4.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Buitenruimten                     | Geen buitenruimten                                                          |              |                     |   -5.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Energieprestatie                  | C (Energie-index)                                                           |              |                     |   22.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Keuken: Lengte aanrecht                                                     |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Keuken                            | Totaal                                                                      |      2700.00 | Millimeter          |    7.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | WOZ-waarde op waardepeildatum 01-01-2023                                    |   [643000.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel I                                                                 |              |                     |   44.21 |         |
| Punten voor de WOZ-waarde         |  - Factor I                                                                 |    [14543.0] |                     |         |         |
| Punten voor de WOZ-waarde         | Onderdeel II                                                                |              |                     |   67.79 |         |
| Punten voor de WOZ-waarde         |  - Oppervlakte van vertrekken en overige ruimten                            |      [41.42] | Vierkante meter, m2 |         |         |
| Punten voor de WOZ-waarde         |  - Factor II                                                                |      [229.0] |                     |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Punten voor de WOZ-waarde         | Totaal                                                                      |              |                     |  112.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
| Zelfstandige woonruimten          | Afgerond totaal                                                             |              |                     |  181.00 |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
|                                   | Maximale huur                                                               |      1151.72 | EUR                 |         |         |
+-----------------------------------+-----------------------------------------------------------------------------+--------------+---------------------+---------+---------+
```

</details>

## 2. Datamodel uitbreidingen

Tijdens de ontwikkeling van de woningwaardering-package komt het voor dat de VERA modellen niet toereikend zijn om de punten voor een stelselgroep te berekenen. Daarom kunnen er indien nodig uitbreidingen gemaakt worden op de VERA modellen. In deze sectie onderbouwen en documenteren wij deze uitbreidingen. In de sectie Referentiedata wordt uitgelegd hoe [uitbreidingen toe te voegen](#datamodellen-uitbreiden) als contributor van dit project.

### Ruimtedetailsoort kast

Binnen het woningwaarderingsstelsel mag onder bepaalde voorwaarden de oppervlakte van vaste kasten worden opgeteld bij de ruimte waar de deur van de kast zich bevindt. Als hier bij het inmeten geen rekening mee gehouden is, kan het attribuut verbonden_ruimten gebruikt worden om de met een ruimte verbonden vaste kasten mee te laten nemen in de waardering. Hiervoor is de VERA referentiedata binnen deze repository uitgebreid met ruimtedetailsoort `Kast`, code `KAS`.

### Verbonden ruimten

Het attribuut `verbonden_ruimten` bevat de ruimten die in verbinding staan met de ruimte die het attribuut bezit. `verbonden_ruimten` wordt gebruikt bij het berekenen van de waardering van kasten en verwarming van ruimten. `verbonden_ruimten` heeft type `Optional[list[EenhedenRuimte]]` en is een uitbreiding op `EenhedenRuimte`. Voor deze uitbreiding staat een [github issue](https://github.com/Aedes-datastandaarden/vera-openapi/issues/47) open ter aanvulling op het VERA model.

### Gedeeld met aantal eenheden

Het attribuut `gedeeld_met_aantal_eenheden` geeft het aantal eenheden (één adres staat gelijk aan één eenheid) weer waarmee een bepaalde ruimte wordt gedeeld. Dit attribuut wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte met ruimtedetailsoort berging. `gedeeld_met_aantal_eenheden` heeft als type `Optional[int]`. Er staat een github issue open om dit ter discussie te stellen: https://github.com/Aedes-datastandaarden/vera-openapi/issues/44

### Gedeeld met aantal onzelfstandige woonruimten

Het attribuut `gedeeld_met_aantal_onzelfstandige_woonruimten` geeft het aantal onzelfstandige woonruimten (op zelfde adres) weer waarmee een bepaalde ruimte wordt gedeeld. `gedeeld_met_aantal_onzelfstandige_woonruimten` heeft als type `Optional[int]`. Er staat een github issue open om dit ter discussie te stellen: https://github.com/Aedes-datastandaarden/vera-openapi/issues/44

### Bouwkundige elementen

In de beleidsboeken wordt soms op basis van een bouwkundig element dat aanwezig is in een ruimte, een uitzondering of nuance op een regel besproken. Dit kan bijvoorbeeld tot gevolg hebben dat er punten in mindering worden gebracht, of punten extra gegeven worden. Bijvoorbeeld bij de berekening van de oppervlakte van een zolder als vertrek of als overige ruimte is er informatie nodig over de trap waarmee de zolder te bereiken is. Daartoe is het VERA model `EenhedenRuimte` uitgebreid met het attribuut `bouwkundige_elementen` met als type `Optional[list[BouwkundigElementenBouwkundigElement]]`. Er staat een github issue open om `bouwkundige_elementen` standaard in het VERA model toe te voegen: https://github.com/Aedes-datastandaarden/vera-openapi/issues/46

> Inmiddels is het attribuut `bouwkundige_elementen` toegevoegd aan het VERA model `EenhedenRuimte` in VERA 4.1.6. Omdat wij VERA 4.1.5 gebruiken is het technisch gezien nog een uitbreiding van ons op het VERA-model.

### Verkoeld en verwarmd

In de VERA standaard is nog geen mogelijkheid om aan te geven of een ruimte verwarmd en/of verkoeld is. Het attribuut `verwarmde_vertrekken_aantal` bestaat wel, maar dit bestaat op niveau van de eenheid en daarin bestaat geen onderscheid tussen vertrekken en overige ruimten.  
Hierom hebben wij twee boolean kenmerken toegevoegd aan `EenhedenRuimte`: `verwarmd` en `verkoeld`. Deze kenmerken geven aan of een ruimte verwarmd en/of verkoeld is.

Dit is aangekaart in deze twee issues:

- https://github.com/Aedes-datastandaarden/vera-openapi/issues/41
- https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/100

### Installaties

Installaties zouden toegevoegd moeten worden aan het VERA model `EenhedenRuimte`. Het attribuut `installaties` bestaat al in de wiki, maar nog niet in de `vera-openapi` repository versie 4.1.5: https://github.com/Aedes-datastandaarden/vera-openapi/issues/70. VERA is hierin vrij verwarrend m.b.t. bouwkundige elementen / installaties / [voorzieningen](https://www.coraveraonline.nl/index.php/Referentiedata:VOORZIENINGSOORT). Op dit moment gebruiken wij `installaties` als attribuut op ruimte met als type `Optional[list[Voorzieningsoort]]`.

### Aantal

Het attribuut `Eenhedenruimte.aantal` is als uitbreiding op het VERA-model toegevoegd. Hierdoor is het mogelijk om aan te geven hoeveel van deze specifieke ruimte er zijn. Dit attribuut wordt uitsluitend gebruikt in het berekenen van de punten voor Gemeenschappelijke Parkeerruimten. Hier door is het niet nodig om elk parkeervak van een parkeergarage of parkeerterrein mee te geven aan een eenheid.

### Parkeergelegenheden

Als uitbreiding op de referentiedata is de `Ruimtesoort.Parkeergelegenheid` toegevoegd. Daarnaast zijn er verschillende parkerruimten (`Ruimtedetailsoort`) toegevoegd. Deze uitbreidingen zijn overgenomen vanuit de github issue https://github.com/Aedes-datastandaarden/vera-referentiedata/issues/110#issuecomment-2190641829.

## 3. Contributing

### Setup

Om de woningwaardering-package en de daarbij behorende developer dependencies te installeren, run onderstaand command:

```
git clone https://github.com/woonstadrotterdam/woningwaardering.git
cd woningwaardering
pip install -e ".[dev]"
```

### Naamgeving van classes

Voor de naamgeving van de classes in de woningwaardering module volgen we de VERA referentiedata. Deze referentiedata is gedefinieerd in de referentiedata enums, te vinden onder [woningwaardering/vera/referentiedata](woningwaardering/vera/referentiedata).

#### Genereren opzet woningwaarderingstelsels en -groepen

Om alle onderstaande naamgevingen correct en consequent door te voeren, is er een task beschikbaar die de opzet van een woningwaarderingstelsel en -groep volgens deze regels voor je kan aanmaken.

Zorg er voor dat [Task](https://taskfile.dev/installation/) en de dev dependencies zijn geïnstalleerd:

```
pip install -e ".[dev]"
```

Vervolgens voer je onderstaand command uit:

```
task genereer-opzet-woningwaarderinggroep
```

Dit script stelt je een aantal vragen, waarna de code voor het stelsel en de stelselgroep aangemaakt worden.

#### Stelsels

De namen voor de stelsels zijn te vinden in de `Woningwaarderingstelsel` Enum. Bijvoorbeeld: het stelsel voor zelfstandige woonruimten wordt aangeduid als `Woningwaarderingstelsel.zelfstandige_woonruimten`. De implementatie van dit `Stelsel` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py](woningwaardering/stelsels/zelfstandige_woonruimten/zelfstandige_woonruimten.py).
De geldigheid van een stelsel wordt bepaald door de begin- en einddatum, die in de constructor van de corresponderende klasse worden vastgelegd.

#### Stelselgroepen

De namen voor de stelselgroepen zijn te vinden in de `Woningwaarderingstelselgroep` Enum. Bijvoorbeeld: de stelselgroep voor oppervlakte van vertrekken wordt aangeduid als `Woningwaarderingstelselgroep.oppervlakte_van_vertrekken`. De implementatie van deze `Stelselgroep` bevindt zich in [woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py](woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py).
De geldigheid van een stelselgroep wordt bepaald door de begin- en einddatum, die in de constructor van de corresponderende klasse worden vastgelegd.

### Releasemanagement

#### Versienummering

Voor versienummering maken we gebruik van [SemVer](https://semver.org/lang/nl/):

Bij SemVer wordt een versienummer in de vorm MAJOR.MINOR.PATCH gebruikt, waarbij elk element als volgt wordt verhoogd:

- `MAJOR` wordt verhoogd bij incompatibele API-wijzigingen,
- `MINOR` wordt verhoogd bij het toevoegen van functionaliteit die compatibel is met de vorige versie, en
- `PATCH` wordt verhoogd bij compatibele bugfixes.

Er zijn aanvullende labels beschikbaar voor pre-release en build-metadata om toe te voegen aan het `MAJOR.MINOR.PATCH`-formaat.

Bijvoorbeeld: stel dat de huidige versie `0.1.3-alpha` is.

- De suffix `-alpha` wordt gebruikt zolang de software nog niet volledig is, bijvoorbeeld zolang nog niet alle beoogde stelselgroepen geïmplementeerd zijn
- Wanneer een nieuwe release alleen compatibele bugfixes of updates van dependencies bevat, wordt de nieuwe versie `0.1.4-alpha`
- Wanneer een nieuwe release ook compatibele nieuwe functionaliteit toevoegt, bijvoorbeeld de implementatie van een nieuwe stelselgroep, dan wordt de nieuwe versie `0.2.0-alpha`.
- Wanneer alle beoogde stelselgroepen geïmplementeerd zijn, wordt de nieuwe versie `1.0.0-beta`. De publieke api mag vanaf dan enkel nog backwards-compatible wijzigen.
- Wanneer de software volledig is en in productie genomen wordt, wordt de nieuwe versie `1.0.0`
- Wanneer er een incompatible wijziging is in de VERA modellen, wordt de nieuwe versie `2.0.0`, eventueel met het `-alpha` of `-beta` label, afhankelijk van de implementatiestatus.

#### Releaseproces

Om een nieuwe release te starten, moet er een Git tag aangemaak worden volgens het format `v<versienummer>`. De prefix `v` geeft aan dat de tag een versiepunt markeert.

Bijvoorbeeld:

```cli
$ git tag v0.2.3-alpha
$ git push --tags
```

Hiermee start het releaseproces, gedefinieerd in een GitHub workflow: [.github/workflows/publish-to-pypi.ymls](.github/workflows/publish-to-pypi.yml)

In dit proces wordt een package aangemaakt met een [Python versienummer](https://packaging.python.org/en/latest/discussions/versioning/), afgeleid van het SemVer nummer in de tag. Bijvoorbeeld: `0.2.3-alpha` wordt `0.2.3a0`

De package wordt eerst gepubliceerd op [TestPyPi](https://test.pypi.org/project/woningwaardering/). Na goedkeuring wordt de package naar [PyPi](https://pypi.org/project/woningwaardering/) gepubliceerd. Daarna wordt er een release aangemaakt in GitHub, met een changelog met de titel en link naar alle pull requests die deel uitmaken van deze release.

### Testing

Voor het testen van code wordt het [pytest framework](https://docs.pytest.org/en/8.0.x/index.html) gebruikt. Meer informatie is te vinden over het framework.
Passende tests worden altijd met de nieuw geschreven code opgeleverd.
Er zijn verschillende "test-scopes" te bedenken, zoals het testen van details en specifieke functies.
Daarnaast is het testen van een hele keten of stelselgroep-object ook vereist.
Bij het opleveren van nieuwe code moet aan beide test-scopes gedacht worden.

#### Test coverage rapport

Na het uitvoeren van `pytest` wordt er een code coverage report getoond. Hierin is per file te zien welk percentage van de code in de files getest is.
Daarnaast wordt de code coverage ook naar een file `lcov.info` geschreven. Die kan gebruikt worden in VSCode om de coverage weer te geven met een plugin zoals "Coverage Gutters".

#### Conventies voor tests

Tests worden toegevoegd aan de `tests`-folder in de root van de repository.
Voor de structuur in de `tests`-folder wordt dezelfde structuur aangehouden als die in de `woningwaardering`-folder.
De naam van het bestand waarin de tests staan geschreven is `test_<file_name>.py`.
Elke testfunctie begint met `test_`, gevolgd door de naam van de functie of class die getest wordt, bijvoorbeeld `def test_<functie_naam>()` of `def test_<ClassNaam>()`.
Hierin wordt de naam de van de functie of class exact gevolgd.
Voor pytest is `test_` een indicator om de functie te herkennen als een testfunctie.

Stel dat de functionaliteiten van `woningwaardering/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/oppervlakte_van_vertrekken.py` getest moeten worden, dan is het pad naar het bijbehorende testbestand `tests/stelsels/zelfstandige_woonruimten/oppervlakte_van_vertrekken/test_oppervlakte_van_vertrekken.py`.
In `test_oppervlakte_van_vertrekken.py` worden testfuncties geschreven met bijbehorende naamconventies.
Hieronder is de functienaamconventie en python code weergegeven voor het testen van een losse functie (`def losse_functie`):

```python
def test_losse_functie() -> None:
    assert losse_functie() == True
```

Als er een class getest wordt, bijvoorbeeld `OppervlakteVanVertrekken`, dan is de testfunctie opzet als volgt:

```python

def test_OppervlakteVanVertrekken():
    opp_v_v = OppervlakteVanVertrekken()
    assert self.opp_v_v.functie_een() == 1
    assert self.opp_v_v.functie_twee() == 2
```

#### Test modellen

Om de woningwaardering-package zo nauwkeurig mogelijk te testen, zijn er eenheidmodellen (in .json format) toegevoegd in `tests/data/...`. De modellen volgen de VERA standaard en dienen als een testinput voor de geschreven tests. De resulterende outputs zijn met de hand nagerekend om de kwaliteit van de tests te waarborgen.

Om heel specifieke regelgeving uit het beleidsboek te testen, kunnen er handmatig test modellen gemaakt worden. Deze test modellen worden opgeslagen in de test folder van een stelselgroep waarvoor de specifieke regelgeving die getest wordt. Zie bijvoorbeeld `tests/data/zelfstandige_woonruimten/stelselgroepen/oppervlakte_van_vertrekken/input/gedeelde_berging.json`: hier is een gedeelde berging gedefinieerd om een specifieke set van regels in oppervlakte_van_vertrekken te testen.

### Logger Guidelines

In de woningwaardering package wordt de logger van `loguru` gebruikt voor logging.
Voor het developen in de woningwaardering package worden de logging levels `DEBUG`, `INFO`, `WARNING` en `ERROR` gebruikt.
De verschillende levels worden gebruikt voor de verschillende types van logging, zoals beschreven in de [python 3.11 documentatie](https://docs.python.org/3.11/library/logging.html#logging-levels).
Hieronder is de tabel van de python documentatie gekopieerd waarin de verschillende logging levels staan beschreven.
De tabel is aangevuld met de kolom "Gebruik Woningwaardering Package", waarin wordt aangegeven met voorbeelden welke soort logging gedaan wordt op de verschillende logging levels.

| Level    | Numerieke waarde | Wat het betekent / Wanneer te gebruiken                                                                                                                                                                                                                                                   | Gebruik Woningwaardering Package                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------- | ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| NOTSET   | 0                | Wanneer ingesteld op een logger, geeft dit aan dat bovenliggende loggers geraadpleegd moeten worden om het effectieve niveau te bepalen. Als dit nog steeds NOTSET oplevert, worden alle gebeurtenissen gelogd. Wanneer ingesteld op een handler, worden alle gebeurtenissen afgehandeld. | Wordt niet gebruikt in de woningwaardering package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| DEBUG    | 10               | Gedetailleerde informatie, meestal alleen van belang voor een ontwikkelaar die een probleem probeert te diagnosticeren.                                                                                                                                                                   | Wordt alleen gebruikt om details weer the geven aan een developer. bijvoorbeeld: wat een functie terug geeft of welke type een variabele heeft.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| INFO     | 20               | Bevestiging dat alles werkt zoals verwacht.                                                                                                                                                                                                                                               | Bevat beschrijvingen van de werking van de code. Bijvoorbeeld: Het berekende resultaat voor een stelselgroep of welke code op basis van de input data wordt gerund.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| WARNING  | 30               | Een indicatie dat er iets onverwachts is gebeurd, of dat er in de nabije toekomst een probleem kan optreden (bijv. 'schijfruimte bijna vol'). De software werkt nog steeds zoals verwacht.                                                                                                | Een warning wordt gelogd wanneer er bijvoorbeeld iets mist in de input data of een functie deprecated is. Dit kan er toe leiden dat bepaalde code niet uitgevoerd kan worden. Voor warnings aan de package gebruiker, wordt altijd `warnings.warn()` gebruikt. Zie het kopje [warnings](#warnings) voor meer informatie over het geven van warnings voor gebruikers en hoe hier mee omgegaan wordt.                                                                                                                                                                                                                                                                         |
| ERROR    | 40               | Vanwege een ernstiger probleem heeft de software een bepaalde functie niet kunnen uitvoeren.                                                                                                                                                                                              | Een error wordt in de woningwaardering package gelogd wanneer het gedrag verwacht is en de error een extra toelichting nodig heeft. Wanneer een error kritiek is voor het functioneren van de package wordt deze error geraisd. Ook kan het voorkomen dat de verwachte error toegestaan is. Dit kan bijvoorbeeld in een `try`/`except` patroon. Er kan dan gekozen worden om de error te loggen maar niet te raisen. Hierdoor kan het programma wel doorgaan en is het wel duidelijk dat er een `exception` heeft plaatsgevonden. Zoals een error geraisd kan worden en het programma kan laten stoppen, zo kunnen warnings ook geraisd worden om het progromma te stoppen. |
| CRITICAL | 50               | Een ernstige fout, die aangeeft dat het programma zelf mogelijk niet meer kan blijven draaien.                                                                                                                                                                                            | Wordt niet gebruikt in de woningwaardering package.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

### Datamodellen

De datamodellen in de `woningwaardering` package zijn gebaseerd op de OpenAPI-specificatie van het [VERA BVG domein](https://aedes-datastandaarden.github.io/vera-openapi/Ketenprocessen/BVG.html).

Wanneer je deze modellen wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) en de dev dependencies zijn geïnstalleerd:

```
pip install -e ".[dev]"
```

Vervolgens kan je met dit commando de modellen in deze repository bijwerken:

```
task genereer-vera-bvg-modellen
```

De classes voor deze modellen worden gegeneerd in `woningwaardering/vera/bvg/generated.py`

#### Datamodellen uitbreiden

Wanneer de VERA modellen niet toereikend zijn om de woningwaardering te berekenen, kan het VERA model uitgebreid worden.

Maak hiervoor altijd eerst een issue aan in de [VERA OpenApi repository](https://github.com/Aedes-datastandaarden/vera-openapi).

Maak vervolgens in de map [woningwaardering/vera/bvg/model_uitbreidingen](woningwaardering/vera/bvg/model_uitbreidingen) een class aan met de missende attributen. De naamgeving voor deze classes is: `_{classNaam}`.

Zet in de class bij het toegevoegde attribuut een comment met een link naar het issue in de VERA OpenApi repository zodat duidelijk is waar de toevoeging voor dient, en we kunnen volgen of de aanpassing is doorgevoerd in de VERA modellen.

Daarnaast neem je in de class een docstring op met uitleg over het gebruik en doel van de uitbreiding.

Bijvoorbeeld: voor het uitbreiden van de class `EenhedenRuimte` maak je een class `_EenhedenRuimte` aan:

```python
from typing import Optional

from pydantic import BaseModel, Field


class _EenhedenRuimte(BaseModel):
    # https://github.com/Aedes-datastandaarden/vera-openapi/issues/44
    gedeeld_met_aantal_eenheden: Optional[int] = Field(
        default=None, alias="gedeeldMetAantalEenheden"
    )
    """
    Het aantal eenheden waarmee deze ruimte wordt gedeeld. Deze waarde wordt gebruikt bij het berekenen van de waardering van een gedeelde ruimte met ruimtedetailsoort berging.
    """
```

De task `genereer-vera-bvg-modellen` zal de body van deze classes samenvoegen met de gelijknamige VERA class en zo de toegevoegde attributen beschikbaar maken.

### Referentiedata

We maken gebruik van de [VERA Referentiedata](https://github.com/Aedes-datastandaarden/vera-referentiedata).

Wanneer je de referentiedata wilt bijwerken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd

Vervolgens kan je met dit commando de referentiedata in deze repository bijwerken:

```
task genereer-vera-referentiedata
```

De referentiedata wordt gegenereerd in `woningwaardering/vera/referentiedata`

### Woonplaatsen en COROP-gebieden

Om te bepalen in welk COROP-gebied een woonplaats ligt, maken we gebruik van de CBS datasets "Woonplaatsen in Nederland" en "Gebieden in Nederland".
Het CBS publiceert eens per jaar nieuwe datasets, daarom hebben we een script gemaakt dat een extract van deze data als resource in de package opslaat in `woningwaardering/data/corop/corop.generated.csv`.

Wanneer je deze data bij wilt werken, zorg er dan voor dat [Task](https://taskfile.dev/installation/) is geïnstalleerd.

Vervolgens kan je met dit commando de woonplaatsen en COROP-gebieden in deze repository bijwerken:

```
task genereer-corop-data
```

### Gemiddelde WOZ-waarden per vierkante meter per COROP-gebied

Bij het beleidsboek wordt een bijlage gepubliceerd met de gemiddelde WOZ-waarden per vierkante meter per COROP-gebied. Na publicatie van een nieuwe bijlage dient het bestand `woningwaardering/stelsels/onzelfstandige_woonruimten/punten_voor_de_woz_waarde/lookup_tabellen/corop_gebied_gemiddelde_woz_waarde_per_m2.csv` bijgewerkt te worden, door een kolom toe te voegen met als kolomnaam het jaar van de waardepeildatum waarvoor de nieuwe gemiddelde waarden gelden.

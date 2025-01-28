from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class MonitorwaardesoortReferentiedata(Referentiedata):
    pass


class Monitorwaardesoort(Referentiedatasoort):
    elektriciteitnetgebruikhoog = MonitorwaardesoortReferentiedata(
        code="ENH",
        naam="ElektriciteitNetgebruikHoog",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door slimme meter.
    kWh (cumulatief).
    """

    elektriciteitnetgebruiklaag = MonitorwaardesoortReferentiedata(
        code="ENL",
        naam="ElektriciteitNetgebruikLaag",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door slimme meter.
    kWh (cumulatief).
    """

    elektriciteitsgebruikboilervat = MonitorwaardesoortReferentiedata(
        code="EBV",
        naam="ElektriciteitsgebruikBoilervat",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door Gateway of
    via Portal. kWh (cumulatief). Spiraal zit in boilervat.
    """

    elektriciteitsgebruikbooster = MonitorwaardesoortReferentiedata(
        code="EGB",
        naam="ElektriciteitsgebruikBooster",
    )
    """
    Gegevens zijn in resolutie van 5 minuten. Aangeleverd door Gateway of via Portal.
    kWh (cumulatief) Booster zit in de warmtepomp.
    """

    elektriciteitsgebruikhuishoudelijk = MonitorwaardesoortReferentiedata(
        code="EGH",
        naam="ElektriciteitsgebruikHuishoudelijk",
    )
    """
    Dit wordt berekend en is de resultante van totaal gebruik - gebouwgebonden gebruik.
    En gebouwgebonden gebruik is warmtepomp + boiler + booster + WTW. Resolutie
    volgt resolutie van brondata.
    """

    elektriciteitsgebruikwarmtepomp = MonitorwaardesoortReferentiedata(
        code="EGW",
        naam="ElektriciteitsgebruikWarmtepomp",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door Gateway of
    via Portal. kWh (cumulatief).
    """

    elektriciteitsgebruikwtw = MonitorwaardesoortReferentiedata(
        code="EWT",
        naam="ElektriciteitsgebruikWTW",
    )
    """
    Gegevens zijn meestal in resolutie van 1 uur. Aangeleverd door Gateway of via
    Portal. kWh (cumulatief).
    """

    elektriciteitterugleveringhoog = MonitorwaardesoortReferentiedata(
        code="ETH",
        naam="ElektriciteitTerugleveringHoog",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door slimme meter.
    kWh (cumulatief).
    """

    elektriciteitterugleveringlaag = MonitorwaardesoortReferentiedata(
        code="ETL",
        naam="ElektriciteitTerugleveringLaag",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door slimme meter.
    kWh (cumulatief).
    """

    elektriciteitvermogen = MonitorwaardesoortReferentiedata(
        code="EVE",
        naam="ElektriciteitVermogen",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door slimme meter.
    W (momentaan).
    """

    gasgebruik = MonitorwaardesoortReferentiedata(
        code="GAS",
        naam="Gasgebruik",
    )
    """
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door slimme meter.
    M3 (cumulatief).
    """

    luchtvochtigheid = MonitorwaardesoortReferentiedata(
        code="LUV",
        naam="Luchtvochtigheid",
    )
    """
    Relatieve luchtvochtigheid is een maat voor de hoeveelheid waterdamp die in de lucht
    aanwezig is, uitgedrukt als een percentage van de maximale hoeveelheid waterdamp
    die de lucht bij een bepaalde temperatuur kan bevatten. Bij een relatieve
    luchtvochtigheid van 100% is de lucht volledig verzadigd met waterdamp en kan er
    geen extra vocht meer worden opgenomen, wat kan leiden tot condensatie. Een
    relatieve luchtvochtigheid van 50% betekent dat de lucht de helft van de
    maximale hoeveelheid waterdamp bevat die het bij die temperatuur kan bevatten.
    De relatieve luchtvochtigheid is belangrijk voor comfort en gezondheid, en wordt
    vaak gemeten met een hygrometer. Gegevens zijn in de beschikbare resolutie van
    de monittoring partij. Aangeleverd door Gateway of via Portal. % relatieve
    luchtvochtigheid (momentaan).
    """

    temperatuursetpointwoonkamer = MonitorwaardesoortReferentiedata(
        code="TSW",
        naam="TemperatuurSetpointWoonkamer",
    )
    """
    De ingestelde temperatuur die je wilt bereiken en handhaven in de woonkamer. Dit
    wordt ingesteld via een thermostaat en bepaalt wanneer het verwarmingssysteem
    moet inschakelen om de gewenste temperatuur te bereiken en te behouden.
    Bijvoorbeeld, als je het temperatuursetpoint op 21°C instelt, zal de thermostaat
    de verwarming inschakelen wanneer de temperatuur in de woonkamer onder de 21°C
    daalt en uitschakelen wanneer deze temperatuur is bereikt. De meest slimme
    thermostaten houden rekening met weersverwachtingen en energieprijzen om te
    bepalen wanneer en hoe hard ze de verwarmingsinstallatie aan het werk zetten.
    Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd door Gateway
    of via Portal. Graden C (momentaan).
    """

    temperatuurwarmtapwater = MonitorwaardesoortReferentiedata(
        code="TWT",
        naam="TemperatuurWarmTapwater",
    )
    """
    Gegevens zijn in resolutie van 5 minuten. Aangeleverd door Gateway of via Portal.
    Graden C (momentaan).
    """

    temperatuurwoonkamer = MonitorwaardesoortReferentiedata(
        code="TWO",
        naam="TemperatuurWoonkamer",
    )
    """
    De huidige temperatuur in de woonkamer. Dit kan worden gemeten met een thermometer
    of worden afgelezen van een thermostaat. De ideale temperatuur in de woonkamer
    ligt meestal tussen de 19 en 21 graden Celsius, afhankelijk van persoonlijke
    voorkeur en comfort. Het handhaven van een comfortabele temperatuur in de
    woonkamer is belangrijk voor het welzijn en de productiviteit van de bewoners.
    Te hoge of te lage temperaturen kunnen invloed hebben op het comfort en de
    gezondheid. Gegevens zijn in resolutie van 5, 15 of meer minuten. Aangeleverd
    door Gateway of via Portal. Graden C (momentaan).
    """

    ventilatiedebiet = MonitorwaardesoortReferentiedata(
        code="VED",
        naam="Ventilatiedebiet",
    )
    """
    Een ventilatiedebiet is de hoeveelheid lucht die per tijdseenheid wordt verplaatst
    door een ventilatiesysteem. Dit kan zowel de toevoer van verse lucht als de
    afvoer van vervuilde lucht omvatten. Het ventilatiedebiet wordt meestal
    uitgedrukt in kubieke meters per uur (m³/h) en is essentieel voor het waarborgen
    van een goede luchtkwaliteit in gebouwen. Het meten van het ventilatiedebiet is
    belangrijk om ervoor te zorgen dat een ventilatiesysteem effectief werkt en de
    juiste hoeveelheid lucht verplaatst om een gezond binnenklimaat te behouden. Bij
    ventilatie type C gaat het om afvoer. Bij type D is afvoer en toevoer per
    definitie  gelijk. Resolutie is afhankelijk van monitoringpartij.Aangeleverd
    door Gateway of via Portal. m3/uur (momentaan).
    """

    warmteproductiewarmtepomp = MonitorwaardesoortReferentiedata(
        code="WAW",
        naam="WarmteproductieWarmtepomp",
    )
    """
    Het gebruik van warm water voor huishoudelijke doeleinden, zoals douchen, baden,
    afwassen en schoonmaken. Dit wordt vaak gemeten om inzicht te krijgen in het
    energieverbruik en de efficiëntie van warmwatersystemen, zoals boilers of
    warmtepompen. Het meten van het watergebruik voor warm tapwater is belangrijk
    voor het optimaliseren van energieverbruik en het verminderen van kosten. Het
    kan ook helpen bij het identificeren van mogelijkheden voor waterbesparing en
    het verbeteren van de duurzaamheid van huishouden. Gegevens zijn in resolutie
    van 5 minuten. Aangeleverd door Gateway of via Portal. GJ (cumulatief).
    """

    watergebruikwarmtapwater = MonitorwaardesoortReferentiedata(
        code="WWT",
        naam="WatergebruikWarmTapwater",
    )
    """
    Het gebruik van warm water voor huishoudelijke doeleinden, zoals douchen, baden,
    afwassen en schoonmaken. Dit gaat om het aantal liters warm tapwater dat het
    boilervat verlaat. Hiermee kan worden bepaald hoeveel van de geproduceerde
    warmte naar tapwater gaat (en dus ook hoeveel naar ruimteverwarming).  Dit wordt
    vaak gemeten om inzicht te krijgen in het energieverbruik en de efficiëntie van
    warmwatersystemen, zoals boilers of warmtepompen. Het meten van het watergebruik
    voor warm tapwater is belangrijk voor het optimaliseren van energieverbruik en
    het verminderen van kosten. Het kan ook helpen bij het identificeren van
    mogelijkheden voor waterbesparing en het verbeteren van de duurzaamheid van
    huishoudens. Gegevens zijn in resolutie van 5 minuten. Aangeleverd door Gateway
    of via Portal. Liter (cumulatief).
    """

    zon_opwekmomentaan = MonitorwaardesoortReferentiedata(
        code="ZOM",
        naam="Zon-opwekMomentaan",
    )
    """
    De momentane opwekking van zonne-energie, oftewel de hoeveelheid energie die op een
    specifiek moment door zonnepanelen wordt geproduceerd. Vooral van toepassing bij
    zonneweides of hele grote dakoppervlakten. Dit wordt vaak gemeten in kilowatt
    (kW) of megawatt (MW) en kan variëren afhankelijk van factoren zoals de
    intensiteit van het zonlicht, de hoek van de zonnepanelen, en de efficiëntie van
    het systeem. Het monitoren van de momentane opwekking is belangrijk voor het
    optimaliseren van de prestaties van zonne-energiesystemen en voor het beheren
    van de energievoorziening in real-time. Gegevens zijn in resolutie van 5
    minuten. Aangeleverd door Gateway of via Portal. kW (momentaan).
    """

    zon_opwektotaal = MonitorwaardesoortReferentiedata(
        code="WTO",
        naam="Zon-opwekTotaal",
    )
    """
    De totale hoeveelheid energie die door alle zonnepanelen wordt opgewekt die zijn
    gekoppeld aan de meterkast van een eenheid. Dit kan betrekking hebben op de
    totale productie van een enkel zonnepaneel, een groep zonnepanelen, of zelfs de
    totale zonne-energieproductie. Het meten van de totale zonne-energieopwekking is
    belangrijk voor het evalueren van de efficiëntie van zonne-energiesystemen en
    voor het plannen van energievoorziening en duurzaamheid. Gegevens zijn in
    resolutie van 5, 15 of meer minuten. Aangeleverd door Gateway of via Portal. kWh
    (cumulatief).
    """

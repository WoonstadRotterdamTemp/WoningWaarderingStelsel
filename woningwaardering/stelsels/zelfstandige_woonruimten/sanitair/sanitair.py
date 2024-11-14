import warnings
from collections import Counter
from datetime import date
from decimal import Decimal
from typing import Iterator

from loguru import logger

from woningwaardering.stelsels import utils
from woningwaardering.stelsels._dev_utils import bereken
from woningwaardering.stelsels.stelselgroep import Stelselgroep
from woningwaardering.vera.bvg.generated import (
    EenhedenEenheid,
    EenhedenRuimte,
    WoningwaarderingResultatenWoningwaardering,
    WoningwaarderingResultatenWoningwaarderingCriterium,
    WoningwaarderingResultatenWoningwaarderingCriteriumGroep,
    WoningwaarderingResultatenWoningwaarderingGroep,
    WoningwaarderingResultatenWoningwaarderingResultaat,
)
from woningwaardering.vera.referentiedata import (
    Bouwkundigelementdetailsoort,
    Ruimtedetailsoort,
    Voorzieningsoort,
    Woningwaarderingstelsel,
    Woningwaarderingstelselgroep,
)
from woningwaardering.vera.utils import (
    get_bouwkundige_elementen,
)


class Sanitair(Stelselgroep):
    def __init__(
        self,
        peildatum: date = date.today(),
    ) -> None:
        super().__init__(
            begindatum=date(2024, 7, 1),
            einddatum=date.max,
            peildatum=peildatum,
        )
        self.stelsel = Woningwaarderingstelsel.zelfstandige_woonruimten
        self.stelselgroep = Woningwaarderingstelselgroep.sanitair

    def bereken(
        self,
        eenheid: EenhedenEenheid,
        woningwaardering_resultaat: (
            WoningwaarderingResultatenWoningwaarderingResultaat | None
        ) = None,
    ) -> WoningwaarderingResultatenWoningwaarderingGroep:
        woningwaardering_groep = WoningwaarderingResultatenWoningwaarderingGroep(
            criteriumGroep=WoningwaarderingResultatenWoningwaarderingCriteriumGroep(
                stelsel=self.stelsel.value,
                stelselgroep=self.stelselgroep.value,
            )
        )
        woningwaardering_groep.woningwaarderingen = []

        ruimten = [
            ruimte
            for ruimte in eenheid.ruimten or []
            if not utils.gedeeld_met_eenheden(ruimte)
        ]

        for ruimte in ruimten:
            woningwaardering_groep.woningwaarderingen.extend(
                Sanitair.genereer_woningwaarderingen(ruimte, self.stelselgroep)
            )

        totaal_punten = utils.rond_af_op_kwart(
            sum(
                Decimal(str(woningwaardering.punten))
                for woningwaardering in woningwaardering_groep.woningwaarderingen or []
                if woningwaardering.punten is not None
            ),
        )
        woningwaardering_groep.punten = float(totaal_punten)

        logger.info(
            f"Eenheid ({eenheid.id}) krijgt {woningwaardering_groep.punten} punten voor {self.stelselgroep.naam}"
        )

        return woningwaardering_groep

    @staticmethod
    def genereer_woningwaarderingen(
        ruimte: EenhedenRuimte,
        stelselgroep: Woningwaarderingstelselgroep,
        stelsel: Woningwaarderingstelsel = Woningwaarderingstelsel.zelfstandige_woonruimten,
    ) -> Iterator[WoningwaarderingResultatenWoningwaardering]:
        if ruimte.detail_soort is None:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft geen detailsoort."
            )
            return

        ruimte.installaties = ruimte.installaties or []
        zelfstandige_woonruimte = (
            stelsel == Woningwaarderingstelsel.zelfstandige_woonruimten
        )
        # Backwards compatibiliteit voor bouwkundige elementen
        for mapping in {
            Bouwkundigelementdetailsoort.wastafel: Voorzieningsoort.wastafel,
            Bouwkundigelementdetailsoort.douche: Voorzieningsoort.douche,
            Bouwkundigelementdetailsoort.bad: Voorzieningsoort.bad,
            Bouwkundigelementdetailsoort.kast: Voorzieningsoort.kastruimte,
            Bouwkundigelementdetailsoort.closetcombinatie: Voorzieningsoort.staand_toilet,
        }.items():
            bouwkundige_elementen = list(get_bouwkundige_elementen(ruimte, mapping[0]))
            if bouwkundige_elementen:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}) heeft een {mapping[0].naam} als bouwkundig element. Voor een correcte waardering dient dit als installatie in de ruimte gespecificeerd te worden."
                )
                logger.info(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): {mapping[0].naam} wordt als {mapping[1].naam} toegevoegd aan installaties"
                )
                ruimte.installaties.extend(
                    [mapping[1].value for _ in bouwkundige_elementen]
                )

        installaties = Counter([installatie for installatie in ruimte.installaties])

        mapping_toilet = {
            Ruimtedetailsoort.toiletruimte.value: {
                Voorzieningsoort.hangend_toilet.value: 3.75,
                Voorzieningsoort.staand_toilet.value: 3.0,
            },
            Ruimtedetailsoort.badkamer.value: {
                Voorzieningsoort.hangend_toilet.value: 2.75,
                Voorzieningsoort.staand_toilet.value: 2.0,
            },
            Ruimtedetailsoort.badkamer_met_toilet.value: {
                Voorzieningsoort.hangend_toilet.value: 2.75,
                Voorzieningsoort.staand_toilet.value: 2.0,
            },
        }

        # Toiletten buiten toiletruimten en badkamers komen niet in aanmerking voor waardering.
        if ruimte.detail_soort in [
            Ruimtedetailsoort.toiletruimte.value,
            Ruimtedetailsoort.badkamer.value,
            Ruimtedetailsoort.badkamer_met_toilet.value,
            Ruimtedetailsoort.doucheruimte.value,
        ]:
            for toiletsoort in [
                Voorzieningsoort.hangend_toilet.value,
                Voorzieningsoort.staand_toilet.value,
            ]:
                aantal_toiletten = installaties[toiletsoort]

                if aantal_toiletten > 0:
                    yield (
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam} - {toiletsoort.naam}",
                            ),
                            punten=float(
                                utils.rond_af(
                                    mapping_toilet[ruimte.detail_soort][toiletsoort]
                                    * aantal_toiletten,
                                    decimalen=2,
                                )
                            ),
                            aantal=aantal_toiletten,
                        )
                    )

        punten_sanitair = {
            Voorzieningsoort.wastafel.value: 1.0,
            Voorzieningsoort.meerpersoonswastafel.value: 1.5,
            Voorzieningsoort.douche.value: 4.0 if zelfstandige_woonruimte else 3.0,
            Voorzieningsoort.bad.value: 6.0 if zelfstandige_woonruimte else 5.0,
            Voorzieningsoort.bad_en_douche.value: 7.0
            if zelfstandige_woonruimte
            else 6.0,
        }

        totaal_aantal_wastafels = 0

        for wastafelsoort in [
            Voorzieningsoort.wastafel,
            Voorzieningsoort.meerpersoonswastafel,
        ]:
            aantal_wastafels = installaties[wastafelsoort.value]

            # Een aanrecht met spoelbak, waarvan de lengte minder bedraagt dan 1 m,
            # voldoet dus niet aan de eis van 1 m en wordt daarom niet als aanrecht gewaardeerd,
            # maar als wastafel.
            aantal_spoelbakken = 0
            if (
                wastafelsoort == Voorzieningsoort.wastafel
                and ruimte.detail_soort.code
                in [
                    Ruimtedetailsoort.keuken.code,
                    Ruimtedetailsoort.woonkamer_en_of_keuken.code,
                    Ruimtedetailsoort.woonkamer.code,
                    Ruimtedetailsoort.woon_en_of_slaapkamer.code,
                    Ruimtedetailsoort.slaapkamer.code,
                ]
            ):
                for element in ruimte.bouwkundige_elementen or []:
                    if (
                        element.detail_soort
                        and element.detail_soort.code
                        == Bouwkundigelementdetailsoort.aanrecht.code
                    ):
                        if element.lengte is not None and element.lengte < 1000:
                            logger.info(
                                f"Ruimte '{ruimte.naam}' ({ruimte.id}): aanrecht < 1m wordt als wastafel gewaardeerd."
                            )
                            yield WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam} - {wastafelsoort.naam} (spoelbak in aanrecht < 1m)"
                                ),
                                punten=float(punten_sanitair[wastafelsoort.value]),
                                aantal=1,
                            )
                            aantal_spoelbakken += 1

            totaal_aantal_wastafels += aantal_wastafels

            punten_per_wastafel = Decimal(str(punten_sanitair[wastafelsoort.value]))

            punten_voor_wastafels = utils.rond_af(
                (aantal_wastafels + aantal_spoelbakken) * punten_per_wastafel,
                decimalen=2,
            )

            if aantal_wastafels > 0:
                yield (
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{ruimte.naam} - {wastafelsoort.naam}"
                        ),
                        punten=float(
                            utils.rond_af(
                                aantal_wastafels * punten_per_wastafel,
                                decimalen=2,
                            )
                        ),
                        aantal=aantal_wastafels,
                    )
                )

                # Wastafels worden gewaardeerd tot een maximum van 1 punt,
                # meerpersoonswastafels tot een maximum van 1,5 punt,
                # per vertrek of overige ruimte, m.u.v. de badkamer.
                if (
                    punten_voor_wastafels > punten_per_wastafel
                    and ruimte.detail_soort
                    not in [
                        Ruimtedetailsoort.badkamer.value,
                        Ruimtedetailsoort.badkamer_met_toilet.value,
                        Ruimtedetailsoort.doucheruimte.value,
                    ]
                    # Op een adres met minimaal acht of meer onzelfstandige woonruimten geldt dit maximum niet voor maximaal één ruimte.
                    # Dat betekent dat er voor adressen met acht of meer onzelfstandige woonruimten maximaal één ruimte mag zijn,
                    # naast de badkamer, met meer dan één wastafel die voor waardering in aanmerking komt.
                    # Voor woonruimten met >= 8 onzelfstandige woonruimten passen we hier geen maximering toe,
                    # dit doen we in de Sanitair class voor onzelfstandige woonruimten
                    and (
                        ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten is None
                        or (
                            ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten
                            is not None
                            and ruimte.gedeeld_met_aantal_onzelfstandige_woonruimten < 8
                        )
                    )
                ):
                    logger.info(
                        f"Ruimte '{ruimte.naam}' ({ruimte.id}): {punten_voor_wastafels} punten voor {wastafelsoort.naam} in {ruimte.detail_soort.naam}. Correctie wordt toegepast ivm maximaal {punten_per_wastafel} punt."
                    )
                    yield (
                        WoningwaarderingResultatenWoningwaardering(
                            criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                naam=f"{ruimte.naam} - Max {punten_per_wastafel} punt voor {wastafelsoort.naam}",
                            ),
                            punten=utils.rond_af(
                                punten_per_wastafel - punten_voor_wastafels,
                                decimalen=2,
                            ),
                        )
                    )

        # Waarschuw indien er minder wastafels zijn dan ingebouwde kasten met wastafel
        # want een wastafel moet apart worden meegegeven
        aantal_ingebouwde_kasten = installaties[
            Voorzieningsoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel.value
        ]
        if totaal_aantal_wastafels < aantal_ingebouwde_kasten:
            warnings.warn(
                f"Ruimte '{ruimte.naam}' ({ruimte.id}): {totaal_aantal_wastafels} wastafel(s) zijn minder dan het aantal ingebouwde kasten met wastafel ({aantal_ingebouwde_kasten})."
                f" Een wastafel in een {Voorzieningsoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel.naam} moet apart worden meegegeven."
            )

        totaal_punten_bad_en_douche = Decimal("0")

        aantal_douches = installaties[Voorzieningsoort.douche.value]
        aantal_baden = installaties[Voorzieningsoort.bad.value]

        aantal_bad_en_douches = min(aantal_douches, aantal_baden)

        if aantal_bad_en_douches > 0:
            punten = utils.rond_af(
                aantal_bad_en_douches
                * punten_sanitair[Voorzieningsoort.bad_en_douche.value],
                decimalen=2,
            )

            totaal_punten_bad_en_douche += punten

            yield (
                WoningwaarderingResultatenWoningwaardering(
                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                        naam=f"{ruimte.naam} - {Voorzieningsoort.bad_en_douche.naam}"
                    ),
                    punten=float(punten),
                    aantal=aantal_bad_en_douches,
                )
            )

        for voorzieningsoort in [
            Voorzieningsoort.bad,
            Voorzieningsoort.douche,
        ]:
            aantal = installaties[voorzieningsoort.value] - aantal_bad_en_douches
            if aantal > 0:
                punten = utils.rond_af(
                    aantal * punten_sanitair[voorzieningsoort.value], 2
                )

                totaal_punten_bad_en_douche += punten

                yield (
                    WoningwaarderingResultatenWoningwaardering(
                        criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                            naam=f"{ruimte.naam} - {voorzieningsoort.naam}"
                        ),
                        punten=float(punten),
                        aantal=aantal,
                    )
                )

        punten_voorzieningen = {
            Voorzieningsoort.bubbelfunctie_van_het_bad.value: 1.5,
            Voorzieningsoort.douchewand.value: 1.25,
            Voorzieningsoort.handdoekenradiator.value: 0.75,
            Voorzieningsoort.ingebouwd_kastje_met_in_of_opgebouwde_wastafel.value: 1,
            Voorzieningsoort.kastruimte.value: 0.75,
            Voorzieningsoort.stopcontact_bij_wastafel.value: 0.25,
            Voorzieningsoort.eenhandsmengkraan.value: 0.25,
            Voorzieningsoort.thermostatische_mengkraan.value: 0.5,
        }

        totaal_punten_voorzieningen = Decimal("0")

        if ruimte.detail_soort in [
            Ruimtedetailsoort.badkamer.value,
            Ruimtedetailsoort.badkamer_met_toilet.value,
            Ruimtedetailsoort.doucheruimte.value,
        ]:
            # Geen waardering voor extra voorzieningen indien er geen wastafel in de ruimte is
            if totaal_aantal_wastafels == 0:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen wastafel aanwezig in {ruimte.detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
                )
            # Geen waardering voor extra voorzieningen indien er geen douche of bad in de ruimte is
            elif totaal_punten_bad_en_douche == 0:
                warnings.warn(
                    f"Ruimte '{ruimte.naam}' ({ruimte.id}): geen bad of douche aanwezig in {ruimte.detail_soort.naam}, extra voorzieningen worden niet gewaardeerd."
                )
            elif totaal_aantal_wastafels > 0 and totaal_punten_bad_en_douche > 0:
                for installatie, aantal in installaties.items():
                    if installatie not in (
                        punten_voorzieningen
                        | punten_sanitair
                        | mapping_toilet[Ruimtedetailsoort.toiletruimte.value]
                    ):
                        logger.info(
                            f"Installatie {installatie.naam} komt niet in aanmerking voor waardering"
                        )
                        continue

                    if installatie in punten_voorzieningen:
                        punten = utils.rond_af(
                            aantal * punten_voorzieningen[installatie], decimalen=2
                        )

                        totaal_punten_voorzieningen += punten

                        yield (
                            WoningwaarderingResultatenWoningwaardering(
                                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                    naam=f"{ruimte.naam} - Voorzieningen: {installatie.naam}",
                                ),
                                punten=float(punten),
                                aantal=aantal,
                            )
                        )

                        if installatie == Voorzieningsoort.kastruimte.value:
                            maximum = Decimal("0.75")
                            correctie = min(maximum - punten, Decimal("0"))
                            if correctie < 0:
                                totaal_punten_voorzieningen += correctie

                                yield WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Voorzieningen: Max {maximum} punten voor {installatie.naam}"
                                    ),
                                    punten=float(correctie),
                                )

                        if (
                            installatie
                            == Voorzieningsoort.stopcontact_bij_wastafel.value
                        ):
                            correctie_aantal = (
                                totaal_aantal_wastafels * Decimal("2") - aantal
                            )
                            correctie = min(
                                correctie_aantal
                                * Decimal(punten_voorzieningen[installatie]),
                                Decimal("0"),
                            )
                            if correctie < 0:
                                totaal_punten_voorzieningen += correctie

                                yield WoningwaarderingResultatenWoningwaardering(
                                    criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                                        naam=f"{ruimte.naam} - Voorzieningen: Max 2 stopcontacten per wastafel"
                                    ),
                                    punten=float(correctie),
                                )

        maximering = min(
            utils.rond_af(totaal_punten_bad_en_douche - totaal_punten_voorzieningen, 2),
            Decimal("0"),
        )

        if maximering < 0:
            yield WoningwaarderingResultatenWoningwaardering(
                criterium=WoningwaarderingResultatenWoningwaarderingCriterium(
                    naam=f"{ruimte.naam} - Voorzieningen: Max verdubbeling punten bad en douche"
                ),
                punten=maximering,
            )


if __name__ == "__main__":  # pragma: no cover
    bereken(
        class_=Sanitair(),
        eenheid_input="tests/data/generiek/input/37101000032.json",
        strict=False,  # False is log warnings, True is raise warnings
        log_level="DEBUG",  # DEBUG, INFO, WARNING, ERROR
    )

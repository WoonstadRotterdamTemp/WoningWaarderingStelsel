from woningwaardering.vera.bvg.generated import Referentiedata
from woningwaardering.vera.referentiedatasoort import Referentiedatasoort


class RechtvanopstalReferentiedata(Referentiedata):
    pass


class Rechtvanopstal(Referentiedatasoort):
    zelfstandig_recht_van_opstal = RechtvanopstalReferentiedata(
        code="ZRO",
        naam="Zelfstandig recht van opstal",
    )
    """
    Dit recht staat op zichzelf en is niet afhankelijk van een ander gebruiksrecht op de
    onroerende zaak. Het geeft de opstalhouder het recht om gebouwen, werken of
    beplantingen op, in of boven de grond van een ander te hebben zonder dat deze
    eigendom worden van de grondeigenaar.
    """

    afhankelijk_recht_van_opstal = RechtvanopstalReferentiedata(
        code="ARO",
        naam="Afhankelijk recht van opstal",
    )
    """
    Dit recht is gekoppeld aan een ander gebruiksrecht, zoals erfpacht, huur of pacht.
    Als het onderliggende gebruiksrecht eindigt, eindigt ook het recht van opstal.
    """

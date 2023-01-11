from kardiasclean import phonetics
import logging


log = logging.getLogger(__name__)


def test_soundex():

    a = phonetics.soundex_en("Pfizer")
    b = phonetics.soundex_es("ordoñez")
    log.debug(a)
    log.debug(b)
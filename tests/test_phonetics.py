from kardiasclean import phonetics
import logging


log = logging.getLogger(__name__)


def test_soundex():

    a = phonetics.soundex("Hi")
    b = phonetics.spanish_soundex("ordoñez")
    log.debug(a)
    log.debug(b)

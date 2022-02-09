from kps import KPS
from tekoaly_parannettu import TekoalyParannettu

class KPSParempiTekoaly(KPS):

    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = TekoalyParannettu(10)

        tokan_siirto = tekoaly.anna_siirto()

        self.io.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
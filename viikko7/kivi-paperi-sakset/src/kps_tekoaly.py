from kps import KPS
from tekoaly import Tekoaly

class KPSTekoaly(KPS):

    def _toisen_siirto(self, ensimmaisen_siirto):
        tekoaly = Tekoaly()
    
        tokan_siirto = tekoaly.anna_siirto()

        self.io.kirjoita(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto

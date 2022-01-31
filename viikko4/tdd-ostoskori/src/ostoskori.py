from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.korin_sisalto = []

    def tavaroita_korissa(self):
        tavaroiden_lukumaara = 0

        if self.korin_sisalto:
            for ostos in self.korin_sisalto:
               tavaroiden_lukumaara += ostos.lukumaara()
  
        return tavaroiden_lukumaara

    def hinta(self):
        korin_hinta = 0
        
        if self.korin_sisalto:
            for ostos in self.korin_sisalto:
                korin_hinta += ostos.hinta()
        
        return korin_hinta

    def lisaa_tuote(self, lisattava: Tuote):
        if any(ostos.tuotteen_nimi() == lisattava.nimi() for ostos in self.korin_sisalto):
            for ostos in self.korin_sisalto:
                if ostos.tuotteen_nimi() == lisattava.nimi():
                    ostos.muuta_lukumaaraa(1)
        else:
            self.korin_sisalto.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        paivitetty_korin_sisalto = []
        
        for ostos in self.korin_sisalto:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() > 0:
                    paivitetty_korin_sisalto.append(ostos)
            else:
                paivitetty_korin_sisalto.append(ostos)

        self.korin_sisalto = paivitetty_korin_sisalto

    def tyhjenna(self):
        self.korin_sisalto = []

    def ostokset(self):
        return self.korin_sisalto

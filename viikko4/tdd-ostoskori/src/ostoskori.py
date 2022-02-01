from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoskori = []
        self.maara = 0
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return self.maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.ostoskori:
            summa += ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        self.maara += 1

        ostos = Ostos(lisattava)

        for tavara in self.ostoskori:
            if ostos.tuotteen_nimi() == tavara.tuotteen_nimi():
                tavara.muuta_lukumaaraa(1)
                return
                
        self.ostoskori.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostoskori:
            if poistettava.nimi() == ostos.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.ostoskori.remove(ostos)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoskori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

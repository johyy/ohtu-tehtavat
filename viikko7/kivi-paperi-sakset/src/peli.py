from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class Peli:

    def __init__(self, io):
        self.io = io

    def suorita(self):    
        while True:
            self.io.kirjoita("Valitse pelataanko"
                "\n (a) Ihmistä vastaan"
                "\n (b) Tekoälyä vastaan"
                "\n (c) Parannettua tekoälyä vastaan"
                "\nMuilla valinnoilla lopetetaan"
                )

            vastaus = self.io.lue("")
            self.io.kirjoita("Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s")
            
            if vastaus.endswith("a"):
                KPSPelaajaVsPelaaja(self.io).pelaa()
            elif vastaus.endswith("b"):
                KPSTekoaly(self.io).pelaa()
            elif vastaus.endswith("c"):
                KPSParempiTekoaly(self.io).pelaa()
            else:
                break
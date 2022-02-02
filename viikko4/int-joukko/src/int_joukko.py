class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        self.kapasiteetti = kapasiteetti
        self.kasvatuskoko = kasvatuskoko
        self.kapasiteetti = 5
        self.kasvatuskoko = 5

        self.joukko = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0

    def kuuluu_joukkoon(self, n):

        for i in range(0, self.alkioiden_lkm):
            if n == self.joukko[i]:
                return True

        return False

    def lisaa(self, n):

        if self.alkioiden_lkm == 0:
            self.joukko[0] = n
            self.alkioiden_lkm += 1
            return True

        else:
            if self.kuuluu_joukkoon(n):
                return True
        
        self.joukko[self.alkioiden_lkm] = n
        self.alkioiden_lkm += 1

        taulukko_old = self.joukko

        self.joukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(taulukko_old, self.joukko)
        
        return True

    def poista_alkio(self, n):
        
        if n in self.joukko:
            self.joukko.remove(n)
            self.alkioiden_lkm = self.alkioiden_lkm - 1
            return True
        
        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def alkioiden_maara(self):
        return self.alkioiden_lkm

    def palauta_taulukko(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.joukko[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.palauta_taulukko()
        b_taulu = b.palauta_taulukko()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x

    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.palauta_taulukko()
        b_taulu = b.palauta_taulukko()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y

    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.palauta_taulukko()
        b_taulu = b.palauta_taulukko()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista_alkio(b_taulu[i])

        return z

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm <= 1:
            return "{" + str(self.joukko[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.joukko[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.joukko[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos

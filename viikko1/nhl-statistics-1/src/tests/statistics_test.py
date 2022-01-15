import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_etsi_pelaaja_virheellinen(self):
        self.assertIsNone(self.statistics.search("Selanne"))
    
    def test_etsi_pelaaja(self):
        etsitty = self.statistics.search("Kurri")

        self.assertEqual(self.statistics.search("Kurri"), etsitty)
    
    def test_etsi_joukkuuen_pelaajat(self):
        etsitty = self.statistics.search("Lemieux")

        self.assertEqual(self.statistics.team("PIT"), [etsitty])
    
    def test_parhaat_pisteilijat(self):
        etsitty = []
        
        etsitty.append(self.statistics.search("Gretzky"))

        lista = self.statistics.top_scorers(1)

        self.assertAlmostEqual(lista[0], etsitty[0])
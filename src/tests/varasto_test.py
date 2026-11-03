import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollaa_tilavuuden(self):
        self.varasto = Varasto(-5)

        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_alku_saldo_nollaa_saldon(self):
        self.varasto = Varasto(10, -5)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_alku_saldo_suurempi_kuin_tilavuus_rajoittaa_saldon(self):
        self.varasto = Varasto(10, 20)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_negatiivinen_lisays_varastoon_ei_lisaa_varastoon(self):
        ennen_lisaysta = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, ennen_lisaysta)

    def test_lisaa_varastoon_yli_sallittu_maara(self):
        self.varasto.lisaa_varastoon(50)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ota_varastosta_negatiivinen_maara(self):
        ennen_lisaysta = self.varasto.saldo
        self.varasto.ota_varastosta(1)

        self.assertAlmostEqual(self.varasto.saldo, ennen_lisaysta)

    def test_ota_varastosta_enemman_kuin_saldoa(self):
        self.varasto.ota_varastosta(20)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_saldo_merkkijonona(self):
        self.varasto = Varasto(10, 6.5)
        self.assertAlmostEqual(self.varasto.__str__(), "saldo = 6.5, vielä tilaa 3.5")

    

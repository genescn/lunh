import unittest
import lunh

class TestCalcDigIMEI(unittest.TestCase):

    def test_lunh_calc_digito_imei(self):
        self.assertEqual(lunh.calc_dig_imei('35780502398494'), 2)

    def test_lunh_soma_digito(self):
        self.assertEqual(lunh.soma_digitos('18'), 9)


if __name__ == '__main__':
    unittest.main()
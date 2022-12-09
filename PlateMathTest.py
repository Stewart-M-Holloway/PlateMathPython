import unittest

import PlateMath


# TODO: Complete Unit Testing for Plate Math

class PlateMathTestCase(unittest.TestCase):

    def setUp(self):
        self.plateMath_lb = PlateMath.PlateMath(unit='lb')
        self.plateMath_lb_modify = PlateMath.PlateMath(unit='lb')
        self.plateMath_kg = PlateMath.PlateMath(unit='kg')

    def test_unit_validation(self):
        self.assertRaises(ValueError, PlateMath.PlateMath, 'a',
                          'unit lb | kg not being validated')

    def test_default_bar(self):
        self.assertEqual(self.plateMath_lb.bar_weight, 45,
                         'incorrect default bar weight - lb')
        self.assertEqual(self.plateMath_kg.bar_weight, 20,
                         'incorrect default bar weight - kg')

    def test_bar_override(self):

        self.assertEqual(35, PlateMath.PlateMath('lb',bar_weight=35).bar_weight,
                         'bar_weight argument override failed')

    def test_calculateMaxWeight(self):
        self.assertEqual(1270, self.plateMath_lb.max_weight)
        self.assertEqual(555, self.plateMath_kg.max_weight)


    def test_calculatePlates(self):

        # Test lb
        self.assertEqual({45: 1}, self.plateMath_lb.calculatePlates(135))
        self.assertEqual({45: 2}, self.plateMath_lb.calculatePlates(225))
        self.assertEqual(self.plateMath_lb.plates,
                         self.plateMath_lb.calculatePlates(1820))
        self.assertEqual(0, self.plateMath_lb.calculatePlates(45))
        self.assertEqual({},
                         self.plateMath_lb.calculatePlates(220))

if __name__ == '__main__':
    unittest.main()

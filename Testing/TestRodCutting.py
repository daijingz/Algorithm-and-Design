# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Rod Cutting Problem
import unittest
import RodCutting


class MyTestCase(unittest.TestCase):
    def test_empty_object(self):
        Rod1 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        Rod1.empty_object()
        self.assertEqual(0, Rod1.get_length())
        self.assertEqual([], Rod1.get_price())

        Rod2 = RodCutting.Rod(5, [1, 3, 6, 10, 15])
        Rod2.empty_object()
        self.assertEqual(0, Rod2.get_length())
        self.assertEqual([], Rod2.get_price())

        Rod3 = RodCutting.Rod(3, [1, 3, 6])
        Rod3.empty_object()
        self.assertEqual(0, Rod3.get_length())
        self.assertEqual([], Rod3.get_price())

        Rod4 = RodCutting.Rod(7, [1, 2, 3, 5, 7, 9, 10])
        Rod4.empty_object()
        self.assertEqual(0, Rod4.get_length())
        self.assertEqual([], Rod4.get_price())

        Rod5 = RodCutting.Rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        Rod5.empty_object()
        self.assertEqual(0, Rod5.get_length())
        self.assertEqual([], Rod5.get_price())

    def test_set_rod(self):
        Rod1 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        Rod1.empty_object()
        Rod1.set_rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        self.assertEqual(10, Rod1.get_length())
        self.assertEqual([1, 3, 5, 6, 8, 10, 11, 15, 18, 20], Rod1.get_price())

        Rod2 = RodCutting.Rod(5, [1, 3, 6, 10, 15])
        Rod2.empty_object()
        Rod2.set_rod(5, [1, 3, 6, 10, 15])
        self.assertEqual(5, Rod2.get_length())
        self.assertEqual([1, 3, 6, 10, 15], Rod2.get_price())

        Rod3 = RodCutting.Rod(3, [1, 3, 6])
        Rod3.empty_object()
        Rod3.set_rod(3, [1, 3, 6])
        self.assertEqual(3, Rod3.get_length())
        self.assertEqual([1, 3, 6], Rod3.get_price())

        Rod4 = RodCutting.Rod(7, [1, 2, 3, 5, 7, 9, 10])
        Rod4.empty_object()
        Rod4.set_rod(7, [1, 2, 3, 5, 7, 9, 10])
        self.assertEqual(7, Rod4.get_length())
        self.assertEqual([1, 2, 3, 5, 7, 9, 10], Rod4.get_price())

        Rod5 = RodCutting.Rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        Rod5.empty_object()
        Rod5.set_rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(8, Rod5.get_length())
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8], Rod5.get_price())

    def test_eq(self):
        Rod1 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        Rod2 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        self.assertEqual(True, Rod1 == Rod2)

        Rod3 = RodCutting.Rod(5, [1, 3, 6, 10, 15])
        Rod4 = RodCutting.Rod(5, [1, 3, 6, 10, 15])
        self.assertEqual(True, Rod3 == Rod4)

        Rod5 = RodCutting.Rod(3, [1, 3, 6])
        Rod6 = RodCutting.Rod(3, [1, 3, 6])
        self.assertEqual(True, Rod5 == Rod6)

        Rod7 = RodCutting.Rod(7, [1, 2, 3, 5, 7, 9, 10])
        Rod8 = RodCutting.Rod(7, [1, 2, 3, 5, 7, 9, 10])
        self.assertEqual(True, Rod7 == Rod8)

        Rod9 = RodCutting.Rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        Rod10 = RodCutting.Rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(True, Rod9 == Rod10)

    def test_Cut_Rod(self):
        Rod1 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        self.assertEqual(10, Rod1.Cut_Rod())
# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Rod Cutting Problem
import unittest
import RodCutting


class MyTestCase(unittest.TestCase):
    def test_empty_object(self):
        """! Testing of empty_object method """
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
        """! Testing of set_rod method """
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
        """! Testing of __eq__ method """
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
        """! Testing of Cut_Rod method """
        Rod1 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        self.assertEqual(20, Rod1.Cut_Rod())

        Rod2 = RodCutting.Rod(5, [1, 3, 6, 10, 15])
        self.assertEqual(15, Rod2.Cut_Rod())

        Rod3 = RodCutting.Rod(3, [1, 3, 6])
        self.assertEqual(6, Rod3.Cut_Rod())

        Rod4 = RodCutting.Rod(7, [1, 2, 3, 5, 7, 9, 10])
        self.assertEqual(10, Rod4.Cut_Rod())

        Rod5 = RodCutting.Rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(8, Rod5.Cut_Rod())

        Rod6 = RodCutting.Rod(10, [1, 3, 4, 18, 19, 20, 21, 22, 23, 24])
        self.assertEqual(39, Rod6.Cut_Rod())

        Rod7 = RodCutting.Rod(7, [7, 8, 10, 11, 12, 13, 14])
        self.assertEqual(49, Rod7.Cut_Rod())

        Rod8 = RodCutting.Rod(8, [10, 11, 12, 13, 20, 21, 22, 23])
        self.assertEqual(80, Rod8.Cut_Rod())

        Rod9 = RodCutting.Rod(10, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(89, Rod9.Cut_Rod())

        Rod10 = RodCutting.Rod(5, [1, 4, 9, 16, 25])
        self.assertEqual(25, Rod10.Cut_Rod())

    def test_Mem_Cut_Rod(self):
        """! Testing of Mem_Cut_Rod method """
        Rod1 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        self.assertEqual(20, Rod1.Mem_Cut_Rod())

        Rod2 = RodCutting.Rod(5, [1, 3, 6, 10, 15])
        self.assertEqual(15, Rod2.Mem_Cut_Rod())

        Rod3 = RodCutting.Rod(3, [1, 3, 6])
        self.assertEqual(6, Rod3.Mem_Cut_Rod())

        Rod4 = RodCutting.Rod(7, [1, 2, 3, 5, 7, 9, 10])
        self.assertEqual(10, Rod4.Mem_Cut_Rod())

        Rod5 = RodCutting.Rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(8, Rod5.Mem_Cut_Rod())

        Rod6 = RodCutting.Rod(10, [1, 3, 4, 18, 19, 20, 21, 22, 23, 24])
        self.assertEqual(39, Rod6.Mem_Cut_Rod())

        Rod7 = RodCutting.Rod(7, [7, 8, 10, 11, 12, 13, 14])
        self.assertEqual(49, Rod7.Mem_Cut_Rod())

        Rod8 = RodCutting.Rod(8, [10, 11, 12, 13, 20, 21, 22, 23])
        self.assertEqual(80, Rod8.Mem_Cut_Rod())

        Rod9 = RodCutting.Rod(10, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(89, Rod9.Mem_Cut_Rod())

        Rod10 = RodCutting.Rod(5, [1, 4, 9, 16, 25])
        self.assertEqual(25, Rod10.Mem_Cut_Rod())

    def test_analysis(self):
        """! Testing of analysis method """
        Rod1 = RodCutting.Rod(10, [1, 3, 5, 6, 8, 10, 11, 15, 18, 20])
        self.assertEqual(1.0, Rod1.analysis()[0])

        Rod2 = RodCutting.Rod(5, [1, 3, 6, 10, 15])
        self.assertEqual(1.5, Rod2.analysis()[1])

        Rod3 = RodCutting.Rod(3, [1, 3, 6])
        self.assertEqual(2.0, Rod3.analysis()[2])

        Rod4 = RodCutting.Rod(7, [1, 2, 3, 5, 7, 9, 10])
        self.assertEqual(1.25, Rod4.analysis()[3])

        Rod5 = RodCutting.Rod(8, [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(1.0, Rod5.analysis()[4])

        Rod6 = RodCutting.Rod(10, [1, 3, 4, 18, 19, 20, 21, 22, 23, 24])
        self.assertEqual(1.0, Rod6.analysis()[0])

        Rod7 = RodCutting.Rod(7, [7, 8, 10, 11, 12, 13, 14])
        self.assertEqual(2.1666666666666665, Rod7.analysis()[1])

        Rod8 = RodCutting.Rod(8, [10, 11, 12, 13, 20, 21, 22, 23])
        self.assertEqual(3.25, Rod8.analysis()[2])

        Rod9 = RodCutting.Rod(10, [1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(1.25, Rod9.analysis()[3])

        Rod10 = RodCutting.Rod(5, [1, 4, 9, 16, 25])
        self.assertEqual(5.0, Rod10.analysis()[4])
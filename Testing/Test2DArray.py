# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Test cases (Unit tests)
import unittest
import twoD_array


class MyTestCase(unittest.TestCase):
    def test_init(self):
        """! Testing of __init__ Method """
        array1 = twoD_array.twoD_array(1, 1)
        self.assertEqual(array1.get_body(), [[0]])

        array2 = twoD_array.twoD_array(2, 5)
        self.assertEqual(array2.get_body()[0][4], 0)
        self.assertEqual(array2.get_body()[1][4], 0)
        self.assertEqual(array2.get_body()[0][0], 0)
        self.assertEqual(array2.get_body()[1][0], 0)

        array3 = twoD_array.twoD_array(20, 20)
        self.assertEqual(array3.get_body()[0][0], 0)
        self.assertEqual(array3.get_body()[0][19], 0)
        self.assertEqual(array3.get_body()[19][0], 0)
        self.assertEqual(array3.get_body()[19][19], 0)

        array4 = twoD_array.twoD_array(10, 10)
        self.assertEqual(array4.get_body()[0][0], 0)
        self.assertEqual(array4.get_body()[0][9], 0)
        self.assertEqual(array4.get_body()[9][0], 0)
        self.assertEqual(array4.get_body()[9][9], 0)

        array5 = twoD_array.twoD_array(5, 5)
        self.assertEqual(array5.get_body()[0][0], 0)
        self.assertEqual(array5.get_body()[0][4], 0)
        self.assertEqual(array5.get_body()[4][0], 0)
        self.assertEqual(array5.get_body()[4][4], 0)

    def test_set_x(self):
        """! Testing of set_x Method """
        array1 = twoD_array.twoD_array(1, 1)
        array1.set_x(3)
        self.assertEqual(array1.get_x(), 3)
        array1.set_x(6)
        self.assertEqual(array1.get_x(), 6)
        array1.set_x(10)
        self.assertEqual(array1.get_x(), 10)

        array2 = twoD_array.twoD_array(7, 5)
        array2.set_x(4)
        self.assertEqual(array2.get_x(), 4)
        array2.set_x(2)
        self.assertEqual(array2.get_x(), 2)
        array2.set_x(8)
        self.assertEqual(array2.get_x(), 8)
        array2.set_x(13)
        self.assertEqual(array2.get_x(), 13)

        array3 = twoD_array.twoD_array(20, 20)
        array3.set_x(1)
        self.assertEqual(array3.get_x(), 1)
        array3.set_x(20)
        self.assertEqual(array3.get_x(), 20)
        array3.set_x(1)
        self.assertEqual(array3.get_x(), 1)
        array3.set_x(20)
        self.assertEqual(array3.get_x(), 20)

    def test_set_y(self):
        """! Testing of set_y Method """
        array1 = twoD_array.twoD_array(1, 1)
        array1.set_y(3)
        self.assertEqual(array1.get_y(), 3)
        array1.set_y(6)
        self.assertEqual(array1.get_y(), 6)
        array1.set_y(10)
        self.assertEqual(array1.get_y(), 10)

        array2 = twoD_array.twoD_array(7, 5)
        array2.set_y(4)
        self.assertEqual(array2.get_y(), 4)
        array2.set_y(2)
        self.assertEqual(array2.get_y(), 2)
        array2.set_y(8)
        self.assertEqual(array2.get_y(), 8)
        array2.set_y(13)
        self.assertEqual(array2.get_y(), 13)

        array3 = twoD_array.twoD_array(20, 20)
        array3.set_y(1)
        self.assertEqual(array3.get_y(), 1)
        array3.set_y(20)
        self.assertEqual(array3.get_y(), 20)
        array3.set_y(1)
        self.assertEqual(array3.get_y(), 1)
        array3.set_y(20)
        self.assertEqual(array3.get_y(), 20)

    def test_set_point(self):
        """! Testing of set_point Method """
        array6 = twoD_array.twoD_array(10, 10)
        array6.set_point(9, 9, 2)
        self.assertEqual(array6.get_body()[8][8], 2)
        array6.set_point(8, 4, 16)
        self.assertEqual(array6.get_body()[7][3], 16)
        array6.set_point(7, 1, 9)
        self.assertEqual(array6.get_body()[6][0], 9)

        array7 = twoD_array.twoD_array(5, 5)
        array7.set_point(4, 4, 6)
        self.assertEqual(array7.get_body()[3][3], 6)
        array7.set_point(4, 4, 19)
        self.assertEqual(array7.get_body()[3][3], 19)

        array8 = twoD_array.twoD_array(8, 8)
        array8.set_point(1, 1, 7)
        self.assertEqual(array8.get_body()[0][0], 7)

    def test_empty(self):
        """! Testing of empty Method """
        array6 = twoD_array.twoD_array(10, 10)
        array6.set_point(9, 9, 2)
        self.assertEqual(array6.get_body()[8][8], 2)
        array6.set_point(8, 4, 16)
        self.assertEqual(array6.get_body()[7][3], 16)
        array6.set_point(7, 1, 9)
        self.assertEqual(array6.get_body()[6][0], 9)

        array6.empty()
        self.assertEqual(array6.get_body()[8][8], 0)
        self.assertEqual(array6.get_body()[7][3], 0)
        self.assertEqual(array6.get_body()[6][0], 0)

        array7 = twoD_array.twoD_array(5, 5)
        array7.set_point(4, 4, 6)
        self.assertEqual(array7.get_body()[3][3], 6)
        array7.set_point(4, 4, 19)
        self.assertEqual(array7.get_body()[3][3], 19)

        array7.empty()
        self.assertEqual(array7.get_body()[3][3], 0)
        self.assertEqual(array7.get_body()[3][3], 0)

        array8 = twoD_array.twoD_array(8, 8)
        array8.set_point(1, 1, 7)
        self.assertEqual(array8.get_body()[0][0], 7)

        array8.empty()
        self.assertEqual(array8.get_body()[0][0], 0)
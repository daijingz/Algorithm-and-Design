# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Test cases (Unit tests)
import unittest
import Sort2


class MyTestCase(unittest.TestCase):
    def test_checkAvailable(self):
        """! Testing of checkAvailable method """
        tst1 = [1, 2, 3, 4, 5, 6, 4]
        self.assertEqual(False, Sort2.checkAvailable(tst1))

        tst2 = [0, 2, 3, 4, 5, 6, 1]
        self.assertEqual(False, Sort2.checkAvailable(tst2))

        tst3 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(True, Sort2.checkAvailable(tst3))

        tst4 = [-10, -8, -6, -7]
        self.assertEqual(True, Sort2.checkAvailable(tst4))

        tst5 = [1.0, 2.0, 1.5, 3, 5, 6, 4]
        self.assertEqual(True, Sort2.checkAvailable(tst5))

    def test_heapSort(self):
        """! Testing of selection sort method """
        tst1 = [1, 2, 3, 7, 5, 6, 4]
        true_tst1 = [1, 2, 3, 4, 5, 6, 7]
        Sort2.heapSort(tst1)
        self.assertEqual(true_tst1, tst1)

        tst2 = [-1, -2, -3, -7, -5, -6, -4]
        true_tst2 = [-7, -6, -5, -4, -3, -2, -1]
        Sort2.heapSort(tst2)
        self.assertEqual(true_tst2, tst2)

        tst3 = [10, -2, 3, -7, 5, 6, -4]
        true_tst3 = [-7, -4, -2, 3, 5, 6, 10]
        Sort2.heapSort(tst3)
        self.assertEqual(true_tst3, tst3)

        tst4 = [5.0, 4.0, 3.0, 2.0, 1.0]
        true_tst4 = [1.0, 2.0, 3.0, 4.0, 5.0]
        Sort2.heapSort(tst4)
        self.assertEqual(true_tst4, tst4)

        tst5 = []
        true_tst5 = []
        Sort2.heapSort(tst5)
        self.assertEqual(true_tst5, tst5)

    def test_radixSort(self):
        """! Testing of radix sort method """
        tst1 = [1, 2, 3, 7, 5, 6, 4]
        true_tst1 = [1, 2, 3, 4, 5, 6, 7]
        Sort2.radixSort(tst1)
        self.assertEqual(true_tst1, tst1)

        tst2 = [1, 2, 3, 7, 8, 9, 4]
        true_tst2 = [1, 2, 3, 4, 7, 8, 9]
        Sort2.radixSort(tst2)
        self.assertEqual(true_tst2, tst2)

        tst8 = [2, 3, 7, 5, 6, 4]
        true_tst8 = [2, 3, 4, 5, 6, 7]
        Sort2.radixSort(tst8)
        self.assertEqual(true_tst8, tst8)

        tst9 = [5, 4, 3, 2, 1]
        true_tst9 = [1, 2, 3, 4, 5]
        Sort2.radixSort(tst9)
        self.assertEqual(true_tst9, tst9)

        tst10 = []
        true_tst10 = []
        Sort2.radixSort(tst10)
        self.assertEqual(true_tst10, tst10)

    def test_bucketSort(self):
        """! Testing of bucket sort method """
        tst11 = [0.1, 0.2, 0.3, 0.7, 0.5, 0.6, 0.4]
        true_tst11 = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
        Sort2.bucketSort(tst11)
        self.assertEqual(true_tst11, tst11)

        tst12 = [1, 2, 3, 7, 8, 9, 4]
        true_tst12 = [1, 2, 3, 4, 7, 8, 9]
        Sort2.radixSort(tst12)
        self.assertEqual(true_tst12, tst12)

        tst13 = [2, 3, 7, 5, 6, 4]
        true_tst13 = [2, 3, 4, 5, 6, 7]
        Sort2.radixSort(tst13)
        self.assertEqual(true_tst13, tst13)

        tst14 = [5, 4, 3, 2, 1]
        true_tst14 = [1, 2, 3, 4, 5]
        Sort2.radixSort(tst14)
        self.assertEqual(true_tst14, tst14)

        tst15 = []
        true_tst15 = []
        Sort2.radixSort(tst15)
        self.assertEqual(true_tst15, tst15)
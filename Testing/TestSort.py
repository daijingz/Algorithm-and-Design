# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import unittest
import Sort


class MyTestCase(unittest.TestCase):
    def test_checkAvailable(self):
        """! Testing of checkAvailable method """
        tst1 = [1, 2, 3, 4, 5, 6, 4]
        self.assertEqual(False, Sort.checkAvailable(tst1))

        tst2 = [0, 2, 3, 4, 5, 6, 1]
        self.assertEqual(False, Sort.checkAvailable(tst2))

        tst3 = [1, 2, 3, 4, 5, 6]
        self.assertEqual(True, Sort.checkAvailable(tst3))

        tst4 = [-10, -8, -6, -7]
        self.assertEqual(True, Sort.checkAvailable(tst4))

        tst5 = [1.0, 2.0, 1.5, 3, 5, 6, 4]
        self.assertEqual(True, Sort.checkAvailable(tst5))

    def test_SelectionSort(self):
        """! Testing of selection sort method """
        tst6 = [1, 2, 3, 7, 5, 6, 4]
        true_tst6 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(true_tst6, Sort.SelectionSort(tst6))

        tst7 = [-1, -2, -3, -7, -5, -6, -4]
        true_tst7 = [-7, -6, -5, -4, -3, -2, -1]
        self.assertEqual(true_tst7, Sort.SelectionSort(tst7))

        tst8 = [10, -2, 3, -7, 5, 6, -4]
        true_tst8 = [-7, -4, -2, 3, 5, 6, 10]
        self.assertEqual(true_tst8, Sort.SelectionSort(tst8))

        tst9 = [5.0, 4.0, 3.0, 2.0, 1.0]
        true_tst9 = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(true_tst9, Sort.SelectionSort(tst9))

        tst10 = []
        true_tst10 = []
        self.assertEqual(true_tst10, Sort.SelectionSort(tst10))

    def test_InsertionSort(self):
        """! Testing of insertion sort method """
        tst11 = [1, 2, 3, 7, 5, 6, 4]
        true_tst11 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(true_tst11, Sort.InsertionSort(tst11))

        tst12 = [-1, -2, -3, -7, -5, -6, -4]
        true_tst12 = [-7, -6, -5, -4, -3, -2, -1]
        self.assertEqual(true_tst12, Sort.InsertionSort(tst12))

        tst13 = [10, -2, 3, -7, 5, 6, -4]
        true_tst13 = [-7, -4, -2, 3, 5, 6, 10]
        self.assertEqual(true_tst13, Sort.InsertionSort(tst13))

        tst14 = [5.0, 4.0, 3.0, 2.0, 1.0]
        true_tst14 = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(true_tst14, Sort.InsertionSort(tst14))

        tst15 = []
        true_tst15 = []
        self.assertEqual(true_tst15, Sort.InsertionSort(tst15))

    def test_MergeSort(self):
        """! Testing of merge sort method """
        tst16 = [1, 2, 3, 7, 5, 6, 4]
        true_tst16 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(true_tst16, Sort.MergeSort(tst16))

        tst17 = [-1, -2, -3, -7, -5, -6, -4]
        true_tst17 = [-7, -6, -5, -4, -3, -2, -1]
        self.assertEqual(true_tst17, Sort.MergeSort(tst17))

        tst18 = [10, -2, 3, -7, 5, 6, -4]
        true_tst18 = [-7, -4, -2, 3, 5, 6, 10]
        self.assertEqual(true_tst18, Sort.MergeSort(tst18))

        tst19 = [5.0, 4.0, 3.0, 2.0, 1.0]
        true_tst19 = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(true_tst19, Sort.MergeSort(tst19))

        tst20 = []
        true_tst20 = []
        self.assertEqual(true_tst20, Sort.MergeSort(tst20))

    def test_ShellSort(self):
        """! Testing of shell sort method """
        tst21 = [1, 2, 3, 7, 5, 6, 4]
        true_tst21 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(true_tst21, Sort.ShellSort(tst21))

        tst22 = [-1, -2, -3, -7, -5, -6, -4]
        true_tst22 = [-7, -6, -5, -4, -3, -2, -1]
        self.assertEqual(true_tst22, Sort.ShellSort(tst22))

        tst23 = [10, -2, 3, -7, 5, 6, -4]
        true_tst23 = [-7, -4, -2, 3, 5, 6, 10]
        self.assertEqual(true_tst23, Sort.ShellSort(tst23))

        tst24 = [5.0, 4.0, 3.0, 2.0, 1.0]
        true_tst24 = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(true_tst24, Sort.ShellSort(tst24))

        tst25 = []
        true_tst25 = []
        self.assertEqual(true_tst25, Sort.ShellSort(tst25))

    def test_QuickSort(self):
        """! Testing of quick sort method """
        tst26 = [1, 2, 3, 7, 5, 6, 4]
        true_tst26 = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(true_tst26, Sort.QuickSort(tst26))

        tst27 = [-1, -2, -3, -7, -5, -6, -4]
        true_tst27 = [-7, -6, -5, -4, -3, -2, -1]
        self.assertEqual(true_tst27, Sort.QuickSort(tst27))

        tst28 = [10, -2, 3, -7, 5, 6, -4]
        true_tst28 = [-7, -4, -2, 3, 5, 6, 10]
        self.assertEqual(true_tst28, Sort.QuickSort(tst28))

        tst29 = [5.0, 4.0, 3.0, 2.0, 1.0]
        true_tst29 = [1.0, 2.0, 3.0, 4.0, 5.0]
        self.assertEqual(true_tst29, Sort.QuickSort(tst29))

        tst30 = []
        true_tst30 = []
        self.assertEqual(true_tst30, Sort.ShellSort(tst30))


if __name__ == '__main__':
    unittest.main()

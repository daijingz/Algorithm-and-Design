# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Test cases (Unit tests)
import unittest
import MaximumSubarray


class MyTestCase(unittest.TestCase):
    def test_eq(self):
        MS1 = MaximumSubarray.MaximumSubarray([100, 95, 185, 120, 110], 100)
        MS2 = MaximumSubarray.MaximumSubarray([100, 95, 185, 120, 110], 100)
        self.assertEqual(True, MS1 == MS2)

        MS3 = MaximumSubarray.MaximumSubarray([150, 200, 2000, 20000, 1500, 9000], 150)
        MS4 = MaximumSubarray.MaximumSubarray([150, 200, 2000, 20000, 1500, 9000], 150)
        self.assertEqual(True, MS3 == MS4)

        MS5 = MaximumSubarray.MaximumSubarray([80, 90, 100, 200, 150, 120], 80)
        MS6 = MaximumSubarray.MaximumSubarray([80, 90, 100, 200, 150, 120], 80)
        self.assertEqual(True, MS5 == MS6)

        MS7 = MaximumSubarray.MaximumSubarray([10, 20, 15, 21, 32, 17, 19, 25], 10)
        MS8 = MaximumSubarray.MaximumSubarray([10, 20, 15, 21, 32, 17, 19, 25], 10)
        self.assertEqual(True, MS7 == MS8)

        MS9 = MaximumSubarray.MaximumSubarray([100, 110, 120, 110, 100], 100)
        MS10 = MaximumSubarray.MaximumSubarray([100, 110, 120, 110, 100], 100)
        self.assertEqual(True, MS9 == MS10)

    def test_setStartPrice(self):
        MS1 = MaximumSubarray.MaximumSubarray([100, 95, 185, 120, 110], 100)
        MS1.setStartPrice(80)
        self.assertEqual(80, MS1.getStartPrice())

        MS2 = MaximumSubarray.MaximumSubarray([150, 200, 2000, 20000, 1500, 9000], 150)
        MS2.setStartPrice(180)
        self.assertEqual(180, MS2.getStartPrice())

        MS3 = MaximumSubarray.MaximumSubarray([80, 90, 100, 200, 150, 120], 80)
        MS3.setStartPrice(200)
        self.assertEqual(200, MS3.getStartPrice())

        MS4 = MaximumSubarray.MaximumSubarray([10, 20, 15, 21, 32, 17, 19, 25], 10)
        MS4.setStartPrice(20)
        self.assertEqual(20, MS4.getStartPrice())
        
        MS5 = MaximumSubarray.MaximumSubarray([100, 110, 120, 110, 100], 100)
        MS5.setStartPrice(120)
        self.assertEqual(120, MS5.getStartPrice())

    def test_emptyDailyPrice(self):
        MS1 = MaximumSubarray.MaximumSubarray([100, 95, 185, 120, 110], 100)
        MS1.emptyDailyPrice()
        self.assertEqual([], MS1.getDailyPrice())

        MS2 = MaximumSubarray.MaximumSubarray([150, 200, 2000, 20000, 1500, 9000], 150)
        MS2.emptyDailyPrice()
        self.assertEqual([], MS2.getDailyPrice())

        MS3 = MaximumSubarray.MaximumSubarray([80, 90, 100, 200, 150, 120], 80)
        MS3.emptyDailyPrice()
        self.assertEqual([], MS3.getDailyPrice())

        MS4 = MaximumSubarray.MaximumSubarray([10, 20, 15, 21, 32, 17, 19, 25], 10)
        MS4.emptyDailyPrice()
        self.assertEqual([], MS4.getDailyPrice())

        MS5 = MaximumSubarray.MaximumSubarray([100, 110, 120, 110, 100], 100)
        MS5.emptyDailyPrice()
        self.assertEqual([], MS5.getDailyPrice())

    def test_addDailyPrice(self):
        MS1 = MaximumSubarray.MaximumSubarray([100, 95, 185, 120, 110], 100)
        MS1.addDailyPrice(130)
        self.assertEqual(130, MS1.getDailyPrice()[5])
        MS1.addDailyPrice(150)
        self.assertEqual(150, MS1.getDailyPrice()[6])
        MS1.addDailyPrice(115)
        self.assertEqual(115, MS1.getDailyPrice()[7])

        MS2 = MaximumSubarray.MaximumSubarray([150, 200, 2000, 20000, 1500, 9000], 150)
        MS2.addDailyPrice(3000)
        self.assertEqual(3000, MS2.getDailyPrice()[6])
        MS2.addDailyPrice(1500)
        self.assertEqual(1500, MS2.getDailyPrice()[7])
        MS2.addDailyPrice(1150)
        self.assertEqual(1150, MS2.getDailyPrice()[8])

        MS3 = MaximumSubarray.MaximumSubarray([80, 90, 100, 200, 150, 120], 80)
        MS3.addDailyPrice(80)
        self.assertEqual(80, MS3.getDailyPrice()[6])
        MS3.addDailyPrice(90)
        self.assertEqual(90, MS3.getDailyPrice()[7])
        MS3.addDailyPrice(100)
        self.assertEqual(100, MS3.getDailyPrice()[8])

        MS4 = MaximumSubarray.MaximumSubarray([10, 20, 15, 21, 32, 17, 19, 25], 10)
        MS4.addDailyPrice(10)
        self.assertEqual(10, MS4.getDailyPrice()[8])
        MS4.addDailyPrice(19)
        self.assertEqual(19, MS4.getDailyPrice()[9])
        MS4.addDailyPrice(21)
        self.assertEqual(21, MS4.getDailyPrice()[10])
        MS4.addDailyPrice(23)
        self.assertEqual(23, MS4.getDailyPrice()[11])
        MS4.addDailyPrice(25)
        self.assertEqual(25, MS4.getDailyPrice()[12])

    def test_emptyNet(self):
        MS1 = MaximumSubarray.MaximumSubarray([100, 95, 185, 120, 110], 100)
        MS1.emptyNet()
        self.assertEqual([], MS1.getNet())

        MS2 = MaximumSubarray.MaximumSubarray([150, 200, 2000, 20000, 1500, 9000], 150)
        MS2.emptyNet()
        self.assertEqual([], MS2.getNet())

        MS3 = MaximumSubarray.MaximumSubarray([80, 90, 100, 200, 150, 120], 80)
        MS3.emptyNet()
        self.assertEqual([], MS3.getNet())

        MS4 = MaximumSubarray.MaximumSubarray([10, 20, 15, 21, 32, 17, 19, 25], 10)
        MS4.emptyNet()
        self.assertEqual([], MS4.getNet())

        MS5 = MaximumSubarray.MaximumSubarray([100, 110, 120, 110, 100], 100)
        MS5.emptyNet()
        self.assertEqual([], MS5.getNet())
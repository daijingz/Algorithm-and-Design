# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Test cases (Unit tests)
import unittest
import QuickFind


class MyTestCase(unittest.TestCase):
    def test_get_length(self):
        QF1 = QuickFind.QuickFind()
        self.assertEqual(10, QF1.get_length())

        QF2 = QuickFind.QuickFind(1)
        self.assertEqual(1, QF2.get_length())

        QF3 = QuickFind.QuickFind(0)
        self.assertEqual(10, QF3.get_length())

        QF4 = QuickFind.QuickFind(-1)
        self.assertEqual(10, QF4.get_length())

        QF5 = QuickFind.QuickFind(-25)
        self.assertEqual(10, QF5.get_length())

        QF6 = QuickFind.QuickFind(25)
        self.assertEqual(25, QF6.get_length())
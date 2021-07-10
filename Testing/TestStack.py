# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import unittest
import Stack


class MyTestCase(unittest.TestCase):
    def test_isEmpty(self):
        Stack1 = Stack.Stack()
        self.assertEqual(True, Stack1.isEmpty())
        Stack1.appendBody([1])
        self.assertEqual(False, Stack1.isEmpty())

        Stack2 = Stack.Stack()
        self.assertEqual(True, Stack2.isEmpty())
        Stack2.appendBody([2])
        self.assertEqual(False, Stack2.isEmpty())
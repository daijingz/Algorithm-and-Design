# Author: Jingze Dai
# Date: 16/02/2021
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
import unittest
import Stack


class MyTestCase(unittest.TestCase):
    def test_isEmpty(self):
        Stack1 = Stack.Stack()
        self.assertEqual(True, Stack1.isEmpty())
        Stack1.setBody([1])
        self.assertEqual(False, Stack1.isEmpty())

        Stack2 = Stack.Stack()
        self.assertEqual(True, Stack2.isEmpty())
        Stack2.setBody([2])
        self.assertEqual(False, Stack2.isEmpty())

        Stack3 = Stack.Stack()
        self.assertEqual(True, Stack3.isEmpty())
        Stack3.setBody([3])
        self.assertEqual(False, Stack3.isEmpty())

        Stack4 = Stack.Stack()
        self.assertEqual(True, Stack4.isEmpty())
        Stack4.setBody([4])
        self.assertEqual(False, Stack4.isEmpty())

        Stack5 = Stack.Stack()
        self.assertEqual(True, Stack5.isEmpty())
        Stack5.setBody([5])
        self.assertEqual(False, Stack5.isEmpty())

    def test_makeEmpty(self):
        Stack1 = Stack.Stack()
        Stack1.setBody([1])
        Stack1.setBody([2])
        Stack1.setBody([3])
        Stack1.setBody([4])
        Stack1.setBody([5])
        Stack1.makeEmpty()
        self.assertEqual(True, Stack1.isEmpty())

        Stack2 = Stack.Stack()
        Stack1.makeEmpty()
        self.assertEqual(True, Stack2.isEmpty())

        Stack3 = Stack.Stack()
        Stack3.setBody([1])
        Stack3.setBody([2])
        Stack3.setBody([3])
        Stack3.makeEmpty()
        self.assertEqual(True, Stack3.isEmpty())

        Stack4 = Stack.Stack()
        Stack4.setBody([1])
        Stack4.setBody([2])
        Stack4.setBody([3])
        Stack4.setBody([4])
        Stack4.setBody([5])
        Stack4.setBody([6])
        Stack4.setBody([7])
        Stack4.makeEmpty()
        self.assertEqual(True, Stack4.isEmpty())

        Stack5 = Stack.Stack()
        Stack5.setBody([1])
        Stack5.setBody([2])
        Stack5.setBody([3])
        Stack5.setBody([4])
        Stack5.setBody([5])
        Stack5.setBody([6])
        Stack5.setBody([7])
        Stack5.setBody([8])
        Stack5.setBody([9])
        Stack5.setBody([10])
        Stack5.makeEmpty()
        self.assertEqual(True, Stack5.isEmpty())

    def test_size_len(self):
        Stack1 = Stack.Stack()
        Stack1.setBody([1])
        Stack1.setBody([2])
        Stack1.setBody([3])
        Stack1.setBody([4])
        Stack1.setBody([5])
        self.assertEqual(5, Stack1.size())
        self.assertEqual(5, len(Stack1))

        Stack2 = Stack.Stack()
        self.assertEqual(0, Stack2.size())
        self.assertEqual(0, len(Stack2))

        Stack3 = Stack.Stack()
        Stack3.setBody([1])
        Stack3.setBody([2])
        Stack3.setBody([3])
        self.assertEqual(3, Stack3.size())
        self.assertEqual(3, len(Stack3))

        Stack4 = Stack.Stack()
        Stack4.setBody([1])
        Stack4.setBody([2])
        Stack4.setBody([3])
        Stack4.setBody([4])
        Stack4.setBody([5])
        Stack4.setBody([6])
        Stack4.setBody([7])
        self.assertEqual(7, Stack4.size())
        self.assertEqual(7, len(Stack4))

        Stack5 = Stack.Stack()
        Stack5.setBody([1])
        Stack5.setBody([2])
        Stack5.setBody([3])
        Stack5.setBody([4])
        Stack5.setBody([5])
        Stack5.setBody([6])
        Stack5.setBody([7])
        Stack5.setBody([8])
        Stack5.setBody([9])
        Stack5.setBody([10])
        self.assertEqual(10, Stack5.size())
        self.assertEqual(10, len(Stack5))
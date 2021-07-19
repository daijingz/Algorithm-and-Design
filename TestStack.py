# Author: Jingze Dai
# Email Address: daij24@mcmaster.ca or david1147062956@163.com
# Github: https://github.com/daijingz
# Linkedin: https://www.linkedin.com/in/jingze-dai/
# Description: Test cases (Unit tests)
import unittest
import Stack


class MyTestCase(unittest.TestCase):
    def test_isEmpty(self):
        """! Testing of isEmpty method """
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
        """! Testing of makeEmpty method """
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
        """! Testing of size and len method """
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

    def test_push(self):
        """! Testing of push method """
        Stack1 = Stack.Stack()
        Stack1.push(1)
        Stack1.push(2)
        Stack1.push(3)
        self.assertEqual(1, Stack1.getBody()[0])
        self.assertEqual(2, Stack1.getBody()[1])
        self.assertEqual(3, Stack1.getBody()[2])

        Stack2 = Stack.Stack()
        Stack2.push("1")
        Stack2.push("2")
        Stack2.push("3")
        Stack2.push("4")
        Stack2.push("5")
        self.assertEqual("1", Stack2.getBody()[0])
        self.assertEqual("2", Stack2.getBody()[1])
        self.assertEqual("3", Stack2.getBody()[2])
        self.assertEqual("4", Stack2.getBody()[3])
        self.assertEqual("5", Stack2.getBody()[4])

        Stack3 = Stack.Stack()
        Stack3.push(1.86)
        Stack3.push(2.15)
        Stack3.push(2.34)
        Stack3.push(5.76)
        Stack3.push(9.81)
        self.assertEqual(1.86, Stack3.getBody()[0])
        self.assertEqual(2.15, Stack3.getBody()[1])
        self.assertEqual(2.34, Stack3.getBody()[2])
        self.assertEqual(5.76, Stack3.getBody()[3])
        self.assertEqual(9.81, Stack3.getBody()[4])

    def test_pop(self):
        """! Testing of pop method """
        Stack1 = Stack.Stack()
        Stack1.push(1)
        Stack1.push(2)
        Stack1.push(3)
        Stack1.pop()
        self.assertEqual(2, Stack1.size())
        self.assertEqual(1, Stack1.getBody()[0])
        self.assertEqual(2, Stack1.getBody()[1])

        Stack2 = Stack.Stack()
        Stack2.push("1")
        Stack2.push("2")
        Stack2.push("3")
        Stack2.push("4")
        Stack2.push("5")
        Stack2.pop()
        Stack2.pop()
        Stack2.pop()
        self.assertEqual(2, Stack2.size())
        self.assertEqual("1", Stack2.getBody()[0])
        self.assertEqual("2", Stack2.getBody()[1])

        Stack3 = Stack.Stack()
        Stack3.push(1.86)
        Stack3.push(2.15)
        Stack3.push(2.34)
        Stack3.push(5.76)
        Stack3.push(9.81)
        Stack3.pop()
        self.assertEqual(4, Stack3.size())
        self.assertEqual(1.86, Stack3.getBody()[0])
        self.assertEqual(2.15, Stack3.getBody()[1])
        self.assertEqual(2.34, Stack3.getBody()[2])
        self.assertEqual(5.76, Stack3.getBody()[3])

    def test_delete(self):
        """! Testing of delete method """
        Stack1 = Stack.Stack()
        Stack1.push(1)
        Stack1.push(2)
        Stack1.push(3)
        Stack1.pop()
        self.assertEqual(2, Stack1.size())
        self.assertEqual(1, Stack1.getBody()[0])
        self.assertEqual(2, Stack1.getBody()[1])

        Stack2 = Stack.Stack()
        Stack2.push("1")
        Stack2.push("2")
        Stack2.push("3")
        Stack2.push("4")
        Stack2.push("5")
        Stack2.pop()
        Stack2.pop()
        Stack2.pop()
        self.assertEqual(2, Stack2.size())
        self.assertEqual("1", Stack2.getBody()[0])
        self.assertEqual("2", Stack2.getBody()[1])

        Stack3 = Stack.Stack()
        Stack3.push(1.86)
        Stack3.push(2.15)
        Stack3.push(2.34)
        Stack3.push(5.76)
        Stack3.push(9.81)
        Stack3.pop()
        self.assertEqual(4, Stack3.size())
        self.assertEqual(1.86, Stack3.getBody()[0])
        self.assertEqual(2.15, Stack3.getBody()[1])
        self.assertEqual(2.34, Stack3.getBody()[2])
        self.assertEqual(5.76, Stack3.getBody()[3])
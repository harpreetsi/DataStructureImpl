from StackImplUsingLinkedList import Stack
import unittest

class StackImplUsingLinkedListTest(unittest.TestCase):

	def test_push(self):
		myStack = Stack()
		myStack.push(5)
		self.assertEqual(myStack.topElement(), 5)
		# print(myStack.topElement())		

	def test_topElement(self):
		myStack = Stack()
		myStack.push(10)
		self.assertEqual(myStack.topElement(), 10)

	def test_topElement_stackEmpty(self):
		myStack = Stack()
		self.assertEqual(myStack.topElement(), "Stack empty")

	def test_pop(self):
		myStack = Stack()
		myStack.push(10)
		self.assertEqual(myStack.pop().data, 10)
		# print(myStack.pop().data)

	def test_stackUnderflow(self):
		myStack = Stack()
		self.assertEqual(myStack.pop(), "Stack empty")

	def test_isEmpty(self):
		myStack = Stack()
		self.assertTrue(myStack.isEmpty())

	def test_isNotEmpty(self):
		myStack = Stack()
		myStack.push(10)
		self.assertFalse(myStack.isEmpty())



if __name__ == '__main__':
	unittest.main()
from StackImplUsingLinkedList import StackImplUsingLinkedList
import unittest

class StackImplUsingLinkedListTest(unittest.TestCase):

	def test_push(self):
		myStack = StackImplUsingLinkedList()
		myStack.push(5)
		self.assertEqual(myStack.topElement(), 5)
		# print(myStack.topElement())		

	def test_topElement(self):
		myStack = StackImplUsingLinkedList()
		myStack.push(10)
		self.assertEqual(myStack.topElement(), 10)

	def test_topElement_stackEmpty(self):
		myStack = StackImplUsingLinkedList()
		self.assertEqual(myStack.topElement(), "Stack empty")

	def test_pop(self):
		myStack = StackImplUsingLinkedList()
		myStack.push(10)
		self.assertEqual(myStack.pop().data, 10)
		# print(myStack.pop().data)

	def test_stackUnderflow(self):
		myStack = StackImplUsingLinkedList()
		self.assertEqual(myStack.pop(), "Stack empty")

	def test_isEmpty(self):
		myStack = StackImplUsingLinkedList()
		self.assertTrue(myStack.isEmpty())

	def test_isNotEmpty(self):
		myStack = StackImplUsingLinkedList()
		myStack.push(10)
		self.assertFalse(myStack.isEmpty())



if __name__ == '__main__':
	unittest.main()
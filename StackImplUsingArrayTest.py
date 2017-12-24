from StackImplUsingArray import StackImplUsingArray
import unittest

class TestStackImplUsingArray(unittest.TestCase):

	def test_push(self):
		myStack = StackImplUsingArray(10)
		self.assertEqual(myStack.push(5), "success")

	def test_stackOverflow(self):
		myStack = StackImplUsingArray(3) # declared a stack of size 3
		myStack.push(5)
		myStack.push(5)
		myStack.push(5)
		self.assertEqual(myStack.push(5), "Stack full")		

	def test_topElement(self):
		myStack = StackImplUsingArray(10)
		myStack.push(10)
		self.assertEqual(myStack.topElement(), 10)

	def test_topElement_stackEmpty(self):
		myStack = StackImplUsingArray(10)
		self.assertEqual(myStack.topElement(), "Stack empty")

	def test_pop(self):
		myStack = StackImplUsingArray(10)
		myStack.push(10)
		self.assertEqual(myStack.pop(), 10)

	def test_stackUnderflow(self):
		myStack = StackImplUsingArray(10)
		self.assertEqual(myStack.pop(), "Stack empty")

	def test_isEmpty(self):
		myStack = StackImplUsingArray(10)
		self.assertTrue(myStack.isEmpty())

	def test_isNotEmpty(self):
		myStack = StackImplUsingArray(10)
		myStack.push(10)
		self.assertFalse(myStack.isEmpty())

	def test_print_empty_stack(self):
		myStack = StackImplUsingArray(10)
		myStack.print()

	def test_print(self):
		myStack = StackImplUsingArray(10)
		myStack.push(10)
		myStack.push(20)
		myStack.print()


if __name__ == '__main__':
	unittest.main()

from BalancedParentheses import BalancedParentheses
import unittest

class BalancedParenthesesTest(unittest.TestCase):

	def test_AreParenthesesBalanced_positive(self):
		balancedParenthesesObject = BalancedParentheses()
		expression = "[(a+b)]"
		self.assertTrue(balancedParenthesesObject.AreParanthesesBalanced(expression))

	def test_AreParenthesesBalanced_negative(self):
		balancedParenthesesObject = BalancedParentheses()
		expression = "[(a+b)])"
		self.assertFalse(balancedParenthesesObject.AreParanthesesBalanced(expression))	

	def test_ArePair_positive(self):
		balancedParenthesesObject = BalancedParentheses()
		self.assertTrue(balancedParenthesesObject.ArePair("{","}"))

	def test_ArePair_negative(self):
		balancedParenthesesObject = BalancedParentheses()
		self.assertFalse(balancedParenthesesObject.ArePair("(","}"))
		


if __name__ == '__main__':
	unittest.main()



	
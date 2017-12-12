from PrefixEvaluation import PrefixEvaluation
import unittest

class PrefixEvaluationTest(unittest.TestCase):

	def test_evaluatePrefix(self):
		expression = "-+*23*549"
		# expression = "+23"
		prefixEvaluationObject = PrefixEvaluation()
		self.assertEqual(prefixEvaluationObject.evaluatePrefix(expression),17)
		# print(prefixEvaluationObject.evaluatePrefix(expression))

	def test_isOperand_positive(self):
		testData = '100' # this should return fasle but returning true, fix it.
		prefixEvaluationObject = PrefixEvaluation()
		self.assertTrue(prefixEvaluationObject.isOperand(testData))
		# print(prefixEvaluationObject.isOperand(testData))

	def test_isOperand_negative(self):
		testData = '100' # This should return false but returning true, fix it.
		prefixEvaluationObject = PrefixEvaluation()
		self.assertFalse(prefixEvaluationObject.isOperand(testData))

	def test_isOperator_positive(self):
		testData = '/'
		prefixEvaluationObject = PrefixEvaluation()
		self.assertTrue(prefixEvaluationObject.isOperator(testData))

	def test_isOperator_negative(self):
		testData = 3
		prefixEvaluationObject = PrefixEvaluation()
		self.assertFalse(prefixEvaluationObject.isOperator(testData))

	def test_performOperation_addition(self):
		prefixEvaluationObject = PrefixEvaluation()
		self.assertEqual(prefixEvaluationObject.performOperation('+', 3, 4), 7)

	def test_performOperation_subtraction(self):
		prefixEvaluationObject = PrefixEvaluation()
		self.assertEqual(prefixEvaluationObject.performOperation('-', 4, 3), 1)
		# print(prefixEvaluationObject.performOperation('-', 4, 3))

	def test_performOperation_multiplication(self):
		prefixEvaluationObject = PrefixEvaluation()
		self.assertEqual(prefixEvaluationObject.performOperation('*', 4, 3), 12)
		# print(prefixEvaluationObject.performOperation('*', 4, 3))

	def test_performOperation_subtraction(self):
		prefixEvaluationObject = PrefixEvaluation()
		self.assertEqual(prefixEvaluationObject.performOperation('/', 5, 2), 2.5)
		# print(prefixEvaluationObject.performOperation('/', 9, 3))



if __name__ == '__main__':
	unittest.main()
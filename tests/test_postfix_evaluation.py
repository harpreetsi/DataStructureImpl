from PostfixEvaluation import PostfixEvaluation
import unittest

class PostfixEvaluationTest(unittest.TestCase):

	def test_evaluatePostfix(self):
		expression = "23*54*+9-"
		# expression = "23+"
		postfixEvaluationObject = PostfixEvaluation()
		self.assertEqual(postfixEvaluationObject.evaluatePostfix(expression),17)
		# postfixEvaluationObject.evaluatePostfix(expression)

	def test_isOperand_positive(self):
		testData = '100' # This should return false but returning true, fix it
		postfixEvaluationObject = PostfixEvaluation()
		self.assertTrue(postfixEvaluationObject.isOperand(testData))

	def test_isOperand_negative(self):
		testData = '100' # This should return false but returning true, fix it.
		postfixEvaluationObject = PostfixEvaluation()
		self.assertFalse(postfixEvaluationObject.isOperand(testData))

	def test_isOperator_positive(self):
		testData = '/'
		postfixEvaluationObject = PostfixEvaluation()
		self.assertTrue(postfixEvaluationObject.isOperator(testData))

	def test_isOperator_negative(self):
		testData = 3
		postfixEvaluationObject = PostfixEvaluation()
		self.assertFalse(postfixEvaluationObject.isOperator(testData))

	def test_performOperation_addition(self):
		postfixEvaluationObject = PostfixEvaluation()
		self.assertEqual(postfixEvaluationObject.performOperation('+', 3, 4), 7)

	def test_performOperation_subtraction(self):
		postfixEvaluationObject = PostfixEvaluation()
		self.assertEqual(postfixEvaluationObject.performOperation('-', 4, 3), 1)
		# print(postfixEvaluationObject.performOperation('-', 4, 3))

	def test_performOperation_multiplication(self):
		postfixEvaluationObject = PostfixEvaluation()
		self.assertEqual(postfixEvaluationObject.performOperation('*', 4, 3), 12)
		# print(postfixEvaluationObject.performOperation('*', 4, 3))

	def test_performOperation_subtraction(self):
		postfixEvaluationObject = PostfixEvaluation()
		self.assertEqual(postfixEvaluationObject.performOperation('/', 5, 2), 2.5)
		# print(postfixEvaluationObject.performOperation('/', 9, 3))



if __name__ == '__main__':
	unittest.main()
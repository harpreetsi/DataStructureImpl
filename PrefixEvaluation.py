from StackImplUsingArray import Stack

class PrefixEvaluation:
	def __init__(self):
		self.myStack = Stack(100) # define stack of 100 elements

	def evaluatePrefix(self, expression):

		for c in reversed(expression):
			if(self.isOperand(c)):
				self.myStack.push(c)
			elif(self.isOperator(c)):
				oprand1 = self.myStack.pop()
				oprand2 = self.myStack.pop()
				result = self.performOperation(c, oprand1, oprand2)
				self.myStack.push(result)
			else:
				print("error!!!")

		return self.myStack.topElement()
		
	def isOperand(self, c):
		if(c >= '0' and c <= '9'):
			return True
		else:
			return False

	def isOperator(self, c):
		if(c == '+' or c == '-' or c == '*' or c == '/'):
			return True
		else:
			return False

	def performOperation(self, operator, oprand1, oprand2):
		if(operator == '+'):
			return int(oprand1) + int(oprand2)
		elif(operator == '-'):
			return int(oprand1) - int(oprand2)
		elif(operator == '*'):
			return int(oprand1) * int(oprand2)
		elif(operator == '/'):
			return int(oprand1) / int(oprand2)
		else:
			print("error!!!")

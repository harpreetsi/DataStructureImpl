from StackImplUsingArray import Stack

class BalancedParentheses:
	def __init__(self):
		self.myStack = Stack(100)

	def AreParanthesesBalanced(self, expression):
		for c in expression:
			if(c == '[' or c == '{' or c == '('):
				self.myStack.push(c)
			if(c == ']' or c == '}' or c == ')'):
				if(self.myStack.isEmpty() or not self.ArePair(self.myStack.topElement(),c)):
					return False
				else:
					self.myStack.pop()

		if(self.myStack.isEmpty()):
			return True
		else:
			return False

	def ArePair(self, opening, closing):
		if(opening == '[' and closing == ']'):
			return True
		elif(opening == '{' and closing == '}'):
			return True
		elif(opening == '(' and closing == ')'):
			return True
		else: 
			return False

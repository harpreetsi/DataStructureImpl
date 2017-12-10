class StackImplUsingArray:
	def __init__(self,size):
		self.list = [i for i in range(size)]
		self.top = -1


	def push(self, data):
		if self.top == len(self.list) - 1:
			return "Stack full"
			
		self.top = self.top + 1
		self.list[self.top] = data

	# returns top element from ther stack, returns None if stack is empty
	def topElement(self):
		if self.top == -1:
			return "Stack empty"
			
		return self.list[self.top]

	# removes the element from top of the stack and returns it, returns None if stack is empty
	def pop(self):
		if self.top == -1:
			return "Stack empty"
			
		element = self.list[self.top]
		self.top = self.top - 1
		return element

	# if stack is empty, returns 0 otherwise returns 1
	def isEmpty(self):
		if self.top == -1:
			return True
		else:
			return False

	def print(self):
		i=0
		while i <= self.top:
			print(self.list[i])
			i = i + 1

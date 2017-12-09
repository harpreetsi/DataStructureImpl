class StackImplUsingArray:
	def __init__(self):
		self.list = [i for i in range(10)]
		self.top = -1


	def push(self, data):
		if self.top == len(self.list) - 1:
			print("Stack overflow, can not push!!!")
			return
		self.top = self.top + 1
		self.list[self.top] = data

	# returns top element from ther stack, returns None if stack is empty
	def topElement(self):
		if self.top == -1:
			print("Stack is empty!!!")
			return

		return self.list[self.top]

	# removes the element from top of the stack and returns it, returns None if stack is empty
	def pop(self):
		if self.top == -1:
			print("Stack empty, nothing to pop!!!")
			return
		element = self.list[self.top]
		self.top = self.top - 1
		return element

	# if stack is empty, returns 0 otherwise returns 1
	def isEmpty(self):
		if self.top == -1:
			return 0
		else:
			return 1

	def print(self):
		i=0
		while i <= self.top:
			print(self.list[i])
			i = i + 1



myStack = StackImplUsingArray()

myStack.push(5)
myStack.push(7)
myStack.push(9)
myStack.push(11)
# print("element removed")
# print(myStack.pop())
# myStack.pop()
# myStack.pop()
# myStack.pop()

# print(myStack.topElement())

myStack.print()

# print(myStack.isEmpty())





# Node class starts here
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

	def getData(self):
		return self.data

	def setData(self, data):
		self.data = data

	def getNext(self):
		return self.next

	def setNext(self, next):
		self.next = next
# Node class ends here

# Stack class starts here
class StackImplUsingLinkedList:
	def __init__(self):
		self.top = None

	def print(self):
		if self.top is None:
			print("Stack is empty, nothing to print!!!")
			return

		current = self.top		
		while current != None:
			print(current.data)
			current = current.next

	def push(self, data):
		node = Node(data)
		node.next = self.top
		self.top = node

	def pop(self):
		if self.top is None:
			print("Stack is empty, nothing to pop!!!")
			return

		temp = self.top
		self.top = self.top.next

	def topElement(self):
		if self.top is None:
			print("Stack is empty!!!")
			return
		print(self.top.data)

	def isEmpty(self):
		if self.top is None:
			print("Stack is empty!!!")
		else:
			print("Stack is not empty!!!")

# Stack class ends here

myStack = StackImplUsingLinkedList()

myStack.push(10)
myStack.push(20)
myStack.push(30)

# myStack.pop()
# myStack.pop()
# myStack.pop()
# myStack.pop()

# 
# myStack.topElement()
#
myStack.isEmpty()


myStack.print()







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
class Stack:
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
			return "Stack empty"

		element = self.top
		self.top = self.top.next
		return element

	def topElement(self):
		if self.top is None:
			return "Stack empty"
			
		return self.top.data

	def isEmpty(self):
		if self.top is None:
			return True
		else:
			return False


class Queue:

	def __init__(self, size):
		self.list = [i for i in range(size)]
		self.front = -1
		self.rear = -1


	def enqueue(self, data):
		if self.rear == len(self.list) - 1:
			return "queue full"
		elif self.front == -1 and self.rear == -1:
			self.front = self.rear = 0
		else:
			self.rear = self.rear + 1
		
		self.list[self.rear] = data
		return "success"


	def dequeue(self):
		if self.isEmpty():
			return "queue empty"
		elif self.front == self.rear:
			temp = self.list[self.front]
			self.front = -1
			self.rear = -1
		else:
			temp = self.list[self.front]	
			self.front = self.front + 1
		
		return temp


	def frontQ(self):
		if self.isEmpty():
			return "queue empty"

		return self.list[self.front]


	def isEmpty(self):
		if self.front == -1 and self.rear == -1:
			return True
		else:
			return False


	def print(self):
		if self.isEmpty():
			print("queue empty, nothing to print")
		else:
			i=0
			while i <= self.rear:
				print(self.list[i])
				i = i + 1


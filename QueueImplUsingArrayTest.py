from QueueImplUsingArray import Queue
import unittest

class QueueTest(unittest.TestCase):

	def test_enqueue(self):
		queue = Queue(3)
		queue.enqueue(12)
		queue.enqueue(13)		
		self.assertEqual(queue.enqueue(15), "success")

	def test_enqueue_full(self):
		queue = Queue(3)
		queue.enqueue(12)
		queue.enqueue(13)
		queue.enqueue(14)
		self.assertEqual(queue.enqueue(15), "queue full")

	def test_enqueue_one_element(self):
		queue = Queue(3)
		self.assertEqual(queue.enqueue(15), "success")

	def test_dequeue(self):
		queue = Queue(3)
		queue.enqueue(12)
		queue.enqueue(13)
		queue.enqueue(14)		
		self.assertEqual(queue.dequeue(), 12)

	def test_dequeue_empty(self):
		queue = Queue(100)
		self.assertEqual(queue.dequeue(), "queue empty")

	def test_dequeue_one_element(self):
		queue = Queue(3)
		queue.enqueue(15)
		self.assertEqual(queue.dequeue(), 15)

	def test_frontQ_empty(self):
		queue = Queue(3)
		self.assertEqual(queue.frontQ(), "queue empty")

	def test_frontQ(self):
		queue = Queue(3)
		queue.enqueue(12)
		queue.enqueue(13)
		queue.enqueue(14)
		self.assertEqual(queue.frontQ(), 12)

	def test_isEmpty_true(self):
		queue = Queue(3)
		self.assertEqual(queue.isEmpty(), True)

	def test_isEmpty_false(self):
		queue = Queue(3)
		queue.enqueue(12)
		self.assertEqual(queue.isEmpty(), False)

	def test_print(self):
		queue = Queue(3)
		queue.enqueue(12)
		queue.enqueue(13)
		queue.enqueue(14)
		queue.print()

	def test_print_empty_queue(self):
		queue = Queue(3)		
		queue.print()



if __name__ == '__main__':
	unittest.main()
from QueueImplUsingLinkedList import Queue
import unittest

class QueueTest(unittest.TestCase):
	
	def test_enqueue_empty(self):
		queue = Queue()
		queue.enqueue(5)

	def test_enqueue(self):
		queue = Queue()
		queue.enqueue(5)
		queue.enqueue(10)
		queue.enqueue(15)

	def test_dequeue(self):
		queue = Queue()
		queue.enqueue(50)
		queue.enqueue(15)
		queue.enqueue(20)
		self.assertEqual(queue.dequeue(), 50)

	def test_dequeue_empty(self):
		queue = Queue()
		self.assertEqual(queue.dequeue(), "Queue empty")

	def test_isEmpty_true(self):
		queue = Queue()
		self.assertTrue(queue.isEmpty())

	def test_isEmpty_false(self):
		queue = Queue()
		queue.enqueue(20)
		self.assertFalse(queue.isEmpty())

	def test_front_empty(self):
		queue = Queue()
		self.assertEqual(queue.frontQ(), "Queue empty")

	def test_front_non_empty(self):
		queue = Queue()
		queue.enqueue(10)
		queue.enqueue(20)
		self.assertEqual(queue.frontQ(), 10)

	def test_print(self):
		queue = Queue()
		queue.enqueue(10)
		queue.enqueue(20)
		queue.enqueue(30)
		queue.enqueue(40)
		queue.print()


if __name__ == '__main__':
	unittest.main()


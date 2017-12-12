from LinkedList import LinkedList
import unittest

class LinkedListTest(unittest.TestCase):

	def test_add_at_the_begining_empty_list(self):
		mylist = LinkedList()
		mylist.add_at_the_begining(10)
		self.assertEqual(mylist.add_at_the_begining(20).data, 20)
		# print(mylist.add_at_the_begining(20).data)

	def test_add_at_the_begining_non_empty_list(self):
		mylist = LinkedList()
		mylist.add_at_the_begining(10)
		mylist.add_at_the_begining(20)
		self.assertEqual(mylist.add_at_the_begining(30).data, 30)
		# print(mylist.add_at_the_begining(30).data)
		# mylist.print()

	def test_add_at_the_end_empty_list(self):
		mylist = LinkedList()
		self.assertEqual(mylist.add_at_the_end(500).data, 500)
		# print(mylist.add_at_the_end(500).data)

	def test_add_at_the_end_non_empty_list(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		temp = mylist.head.next
		# print(temp.data)
		self.assertEqual(temp.data, 20)

	def test_add_at_nth_position_1st_position_non_empty_list(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		self.assertEqual(mylist.add_at_nth_position(5, 1).data, 5)
		# self.assertEqual(mylist.add_at_nth_position(5, 1).next.data, 10)
		# print(mylist.add_at_nth_position(5, 1).data)
		# mylist.print()

	def test_add_at_nth_position_0th_position_invalid(self):
		mylist = LinkedList()
		self.assertEqual(mylist.add_at_nth_position(5, 0), "Invalid position, it can not be less than or equal to 0")
		# print(mylist.add_at_nth_position(5, 0))

	def test_add_at_nth_position_positive(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		mylist.add_at_the_end(40)
		self.assertEqual(mylist.add_at_nth_position(25, 3).next.next.data, 25)
		# mylist.add_at_nth_position(25, 3)
		# mylist.print()

	def test_add_at_nth_position_invalid_position(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		mylist.add_at_the_end(40)
		self.assertEqual(mylist.add_at_nth_position(50, 6), "Invalid position, it exceeds the size of the linked list")
		# mylist.print()

	def test_remove_at_the_begining_empty_list(self):
		mylist = LinkedList()
		self.assertEqual(mylist.remove_at_the_begining(), "List is empty, nothing to remove")
		# mylist.remove_at_the_begining()

	def test_remove_at_the_begining_non_empty_list(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		self.assertEqual(mylist.remove_at_the_begining().data, 20)
		# print(mylist.remove_at_the_begining().data)

	def test_remove_at_the_end_empty_list(self):
		mylist = LinkedList()
		self.assertEqual(mylist.remove_at_the_end(), "List is empty, nothing to remove")

	def test_remove_at_the_end_list_has_one_element(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		self.assertEqual(mylist.remove_at_the_end(), None)
		# print(mylist.remove_at_the_end())

	def test_remove_at_the_end_list_has_more_than_one_elements(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		self.assertEqual(mylist.remove_at_the_end().next.data, 20)

	def test_remove_at_nth_position_0th_position_invalid(self):
		mylist = LinkedList()
		self.assertEqual(mylist.remove_at_nth_position(0), "Invalid position, it can not be less than or equal to 0")
		# print(mylist.remove_at_nth_position(-1))

	def test_remove_at_nth_position_1st_position(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		self.assertEqual(mylist.remove_at_nth_position(1).data, 20)
		# print(mylist.remove_at_nth_position(1).data)

	def test_remove_at_nth_position_positive(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		mylist.add_at_the_end(40)
		self.assertEqual(mylist.remove_at_nth_position(3).next.next.data, 40)
		# print(mylist.remove_at_nth_position(3))
		# mylist.print()

	def test_remove_at_nth_position_invalid_position(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		self.assertEqual(mylist.remove_at_nth_position(4), "Invalid position, it exceeds the size of the linked list")
		# print(mylist.remove_at_nth_position(4))
		# mylist.print()

	def test_reverse_empty_list(self):
		mylist = LinkedList()
		self.assertEqual(mylist.reverse(), "List is empty, nothing to reverse")

	def test_reverse_non_empty_list(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		mylist.add_at_the_end(40)
		self.assertEqual(mylist.reverse().data, 40)
		# print(mylist.reverse().data)

	def test_reverse_one_element_list(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		self.assertEqual(mylist.reverse().data, 10)
		# print(mylist.reverse().data)

	def test_reverse_using_recursion_empty_list(self):
		mylist = LinkedList()
		self.assertEqual(mylist.reverse_using_recursion(mylist.head), "List is empty, nothing to reverse")
		# print(mylist.reverse_using_recursion(mylist.head))

	def test_reverse_using_recursion_one_element_list(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		self.assertEqual(mylist.reverse_using_recursion(mylist.head).data, 10)
		# print(mylist.reverse_using_recursion(mylist.head).data)

	def test_reverse_using_recursion_non_empty_list(self):
		mylist = LinkedList()
		mylist.add_at_the_end(10)
		mylist.add_at_the_end(20)
		mylist.add_at_the_end(30)
		mylist.add_at_the_end(40)
		mylist.add_at_the_end(50)
		mylist.add_at_the_end(60)
		self.assertEqual(mylist.reverse_using_recursion(mylist.head).data, 60)
		# mylist.reverse_using_recursion(mylist.head)
		# mylist.print()


if __name__ == '__main__':
	unittest.main()

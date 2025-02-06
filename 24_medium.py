
class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


# SOLVED
class LinkedList:
	def __init__(self):
		self.head = None


def swap_pairs(head):
	node = head.head
	while node and node.next:
		node.val, node.next.val = node.next.val, node.val
		node = node.next.next

	return head

head = LinkedList()
first = Node(1)
second = Node(2)
third = Node(3)
forth = Node(4)

head.head = first
first.next = second
second.next = third
third.next = forth

print(swap_pairs(head))

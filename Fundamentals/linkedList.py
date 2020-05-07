class Node:
def __init__(self, value, next = None):
	self.value = value 
	self.next = next 

class LinkedList:
	def __init__(self):
		self.head = Node("dummy")
		self._size = 0

	def insertFromFront(self, value):
		# setting the first element of linkedlist into next  
		next = self.head.next 
		# setting the value of the first element to the new value
		self.head.next = Node(value)
		# setting the pointer for the new value to the old head  
		self.head.next.next = next 




# Definition for singly-linked list with a random pointer.
import pdb
class RandomListNode:
	def __init__(self, x):
		self.label = x
		self.next = None
		self.random = None

class Solution:
	# @param head, a RandomListNode
	# @return a RandomListNode
	def copyRandomList(self, head):
		pdb.set_trace()
		if head == None:
			return None
		t = head
		while t != None:
			newNode = RandomListNode(t.label)
			t.copyNode = newNode
			t = t.next
		t = head
		result = head.copyNode
		pdb.set_trace()
		while t != None:
			if t.next != None:
				t.copyNode.next = t.next.copyNode
			if t.random != None:
				t.copyNode.random = t.random.copyNode
			t = t.next
		t =  head
		while t != None:
			t.copyNode = None	
			del(t.copyNode)
			t = t.next
		pdb.set_trace()
		return result

test = Solution()
r1 = RandomListNode(1)
r2 = RandomListNode(2)
r3 = RandomListNode(3)

r1.next = r2
r2.next = r3
r1.random = r3
r2.random = r2

result = test.copyRandomList(r1)
import pdb
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	# @param head, a ListNode
	# @param k, an integer
	# @return a ListNode
	def lengthOfList(self, head):
		p = head
		c = 0
		while not p is None:
			p = p.next
			c = c + 1
		return c
	def reverseKGroup(self, head, k):
		length = self.lengthOfList(head)
		groupCount = length / k
		if k <= 1 or groupCount == 0:
			return head
		c = 0
		inc = 1
		gstart = head
		inp = head.next
		preTail = None
		while c < groupCount:
			preNode = gstart 
			nextNode = None
			while inc < k:
				nextNode = inp.next
				inp.next = preNode 
				preNode = inp
				inp = nextNode
				inc = inc + 1
			if c == 0:
				result = preNode
			if not preTail is None:
				preTail.next = preNode
			preTail = gstart 
			gstart = nextNode
			if not gstart is None:
				inp = gstart.next
			inc = 1
			c = c + 1
		preTail.next = nextNode
		return result 

def makelist(arr):
	result = None
	p = None
	for a in arr:
		if result is None:
			result = ListNode(a)
			p = result
		else:
			p.next = ListNode(a)
			p = p.next
	return result
def printlist(head):
	p = head
	while not p is None:
		print p.val, "->"
		p = p.next

test = Solution()
arr = [1,2,3,4]
arr = [1,2]
l = makelist(arr)
printlist(l)
print "---"
l = test.reverseKGroup(l, 1)
printlist(l)

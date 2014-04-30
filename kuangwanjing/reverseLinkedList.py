import pdb

class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None
def arrToList(arr):
	if len(arr) > 0:
		head = ListNode(arr[0])
		cur = head
		for i in range(1, len(arr)):
			cur.next = ListNode(arr[i])
			cur = cur.next
	return head
def printList(l):
	cur = l
	while cur != None:
		print cur.val , "->"
		cur = cur.next
	print "None"
class Solution:
	def reverseBetween(self, head, m, n):
		#pdb.set_trace()
		cur = head
		count = 1
		reverseHead = None
		reverseTail = None
		if m > 1:
			while cur != None:
				if count == m - 1:
					reverseHead = cur 
					reverseTail = cur.next
					break
				cur = cur.next
				count = count + 1
		else:
			reverseTail = head
		cur = reverseTail.next
		curt = reverseTail
		for i in range(0, n-m):
			np = cur.next
			cur.next = curt 
			curt = cur
			cur = np
		if reverseHead != None:
			reverseHead.next = curt
		else:
			head = curt
		reverseTail.next = cur
		return head

test = Solution()
l = arrToList([1,2,3,4,5])

result = test.reverseBetween(l, 1, 5)
printList(result)
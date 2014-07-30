# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
"""
class Solution:
	def printList(self, head, tail):
		p = head
		while p != None:
			print p.val , "->"
			if p == tail:
				break
			p = p.next
	def reorderList(self, head):
		if head is None or head.next is None or head.next.next is None:
			return 
		#find the middle ListNode
		step1 = step2 = head 
		while not step2 is None and not step2.next is None:
			step1 = step1.next
			step2 = step2.next
			if not step2 is None:
				step2 = step2.next
		step = step1
		if not step2 is None:
			step = step.next
		h = head
		while not step is None:
			temp = step.next
			step.next = h
			h = step
			step = temp
		step = h
		h = head
		#reorder the list
		while not h is step1:
			temp1 = h.next
			temp2 = step.next
			h.next = step
			step.next = temp1 
			h = temp1
			step = temp2
		step1.next = None

test = Solution()
arr = [1,2,3,4,5,6]
l = makeList(arr)
test.reorderList(l)
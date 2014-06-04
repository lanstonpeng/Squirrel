# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        h = head
        while h:
            if h.next and h.val == h.next.val:
                h.next = h.next.next
            else:
            	h = h.next
        return head

s = Solution()
h1 = ListNode(1)
h2 = ListNode(1)
h3 = ListNode(1)
h1.next = h2
h2.next = h3

b =  s.deleteDuplicates(h1)

while b:
	print b.val
	b = b.next
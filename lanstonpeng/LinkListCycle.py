import pdb
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
    	#pdb.set_trace()
        if head == None:
            return False
        node1 = head
        node2 = head
        while 1:
            node1 = node1.next
            #print node1.val
            node2 = node2.next
            if node1 == None:
                return False
            if node2:
                node2 = node2.next
                #print node2.val
            else:
                return False
            if node2 == None:
            	return False
            if node1.val == node2.val:
                return True

s = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l1.next = l2
l2.next = l1
print s.hasCycle(l1)


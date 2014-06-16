#Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

import pdb
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param num, a list of integerse
	# @return a tree node
	def buildTree(self, num, head, tail):
		if head == tail:
			return TreeNode(num[head])
		if head > tail:
			return None
		mid = (head + tail)	/ 2
		root = TreeNode(num[mid])
		left = self.buildTree(num, head, mid-1)
		right = self.buildTree(num, mid+1, tail)
		root.left = left
		root.right = right
		return root
	def sortedArrayToBST(self, num):
		return self.buildTree(num, 0, len(num)-1)

test = Solution()
inputa = [3,4,5,6,7]
result = test.sortedArrayToBST(inputa)
pdb.set_trace()
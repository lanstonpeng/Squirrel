class ClassName(val):
	def __init__(self, val):
		self.val = val 
		self.left = None
		self.right = None
		
class Solution:
	# @param root, a tree node
	# @return a boolean
	def visited(self, node):
		if node == None:
			return 0
		lh = self.visited(node.left)
		lr = self.visited(node.right)
		if lh is not None:
			return None
		if lr is not None:
			return None
		if max(lh, lr) - min(lh, lr) > 1:
			return None
		return max(lh, lr) + 1
	def isBalanced(self, root):
		if self.visited(root) is not None:
			return True
		else:
			return False
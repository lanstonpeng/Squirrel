import pdb
# Definition for a  binary tree node
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution:
	# @param root, a tree node
	# @return a list of integers
	def inorderTraversal(self, root):
		result = []
		s = []
		nodes = []
		if root != None:
			s.append(0)
			nodes.append(root)
		#pdb.set_trace()
		while len(s): 
			cur = nodes[-1]
			curs = s[-1]
			if curs == 2:
				nodes.pop()						
				s.pop()
				if len(s):
					s[-1] = s[-1] + 1
			if curs == 1:
				result.append(cur.val)
				if cur.right:
					nodes.append(cur.right)	
					s.append(0)
				else:
					s[-1] = 2
			if curs == 0:
				if cur.left:
					nodes.append(cur.left)
					s.append(0)
				else:
					s[-1] = 1
		return result

test = Solution()
root = TreeNode(3)
#root.left = TreeNode(2)
root.right = TreeNode(4)
result = test.inorderTraversal(root)
#result = test.inorderTraversal(None)
print (result)
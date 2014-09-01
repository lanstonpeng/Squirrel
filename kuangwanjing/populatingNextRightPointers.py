import pdb
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None
		self.next = None 

def buildTree(arr):
	# @param arr, a list of value of tree.
	# @return the root node of a tree.
	if len(arr) == 0:
		return None
	treeNodes = []
	for i in range(len(arr)):
		treeNodes.append(TreeNode(arr[i]))
		if i%2 == 0:
			if (i-2)/2 >= 0:
				treeNodes[(i-2)/2].right = treeNodes[i]
		else:
			if (i-1)/2 >= 0:
				treeNodes[(i-1)/2].left = treeNodes[i]
	return treeNodes[0]

def printNext(tree):
	if tree:
		if tree.next:
			print tree.val, "-->", tree.next.val
		else:
			print tree.val, "-->", None
		if tree.left:
			printNext(tree.left)
		if tree.right:
			printNext(tree.right)

class Solution:
	# @param root, a tree node
	# @return nothing
	def connect(self, root):
		if root:
			if root.left and root.right:
				root.left.next = root.right
				if root.next:
					root.right.next = root.next.left
				self.connect(root.left)
				self.connect(root.right)
		return

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
tree = buildTree(arr)
test = Solution()
test.connect(tree)
printNext(tree)

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
    def preorderTraversal(self, root):
        self.result = [];
        self.noRecur(root)
        return self.result
    def recur(self,node):
        if node != None:
            self.result.append(node.val)
            self.recur(node.left)
            self.recur(node.right)
    def noRecur(self,node):
    	stack = []
    	current = node
    	stack.append(current)
    	#pdb.set_trace()
    	while len(stack) or current:
			while current != None:
				print current.val
				self.result.append(current.val)
				if current.left != None:
					stack.append(current.left)
					current = current.left
				else:
					break
			#pdb.set_trace()
			current = current.right
			while current == None and len(stack):
				current = stack.pop()
				print current.val
				current = current.right

root = TreeNode(2)
node3 = TreeNode(3)
node1 = TreeNode(1)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)

node4.left = node5
node3.left = node1
node3.right = node4

root.left = node3
#root.right = node6

s = Solution()

print s.preorderTraversal(root)

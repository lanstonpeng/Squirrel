# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
    	return self.recur(root) >= 0;
    def recur(self,node):
    	if node == None:
    		return 0
    	left = self.recur(node.left)
    	if left<0:
    		return -1;
    	right = self.recur(node.right)
    	if right < 0 or abs(left - right) > 1:
    		return -1;
    	return max(left,right) + 1


s = Solution()

root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.right = node1
node1.right = node2
node2.right = node3
node3.right = node4

print s.isBalanced(root)
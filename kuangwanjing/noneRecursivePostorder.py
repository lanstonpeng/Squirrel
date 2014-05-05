class Solution:
	# @param root, a tree node
	# @return a list of integers
	def postOrderTraversal(self, root):
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
				result.append(cur.val) #--> postorder
				nodes.pop()						
				s.pop()
				if len(s):
					s[-1] = s[-1] + 1
			if curs == 1:
				#result.append(cur.val) #--> inorder
				if cur.right:
					nodes.append(cur.right)	
					s.append(0)
				else:
					s[-1] = 2
			if curs == 0:
				#result.append(cur.val) #--> preorder
				if cur.left:
					nodes.append(cur.left)
					s.append(0)
				else:
					s[-1] = 1
		return result	
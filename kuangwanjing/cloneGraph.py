# Definition for a undirected graph node
import pdb
class UndirectedGraphNode:
	def __init__(self, x):
		self.label = x
		self.neighbors = []

class Solution:
	# @param node, a undirected graph node
	# @return a undirected graph node
	def cloneGraph(self, node):
		if node == None:	
			return None
		visited = {}
		edges = []
		queue = [node]
		while len(queue) > 0:
			cur = queue[0]
			queue.pop(0)
			if cur.label in visited:
				continue
			visited[cur.label] = True
			for n in cur.neighbors:
				if not n.label in visited:
					queue.append(n)
				edges.append((cur.label, n.label))
		visited[node.label] = True
		
		#stand_alone point
		if len(edges) == 0:
			return UndirectedGraphNode(node.label)
		visited = {}
		for e in edges:
			if not e[0] in visited:
				n1 = UndirectedGraphNode(e[0])
				visited[e[0]] = n1 
			n1 = visited[e[0]]
			if not e[1] in visited:	
				n2 = UndirectedGraphNode(e[1])
				visited[e[1]] = n2 
			n2 = visited[e[1]]	
			n1.neighbors.append(n2)
			#if n1 != n2:
			#	n2.neighbors.append(n1)
		#pdb.set_trace()
		return visited[node.label]

test = Solution()
n0 = UndirectedGraphNode(0)
n1 = UndirectedGraphNode(1)
n2 = UndirectedGraphNode(2)
n3 = UndirectedGraphNode(3)
n4 = UndirectedGraphNode(4)
n5 = UndirectedGraphNode(5)
"""
n1.neighbors = [n2, n3]
n2.neighbors = [n1, n4]
n3.neighbors = [n1, n4]
n4.neighbors = [n2, n3]
"""
"""
n0.neighbors = [n1]
n1.neighbors = [n2]
n2.neighbors = [n2]
"""

n0.neighbors = [n0, n0, n0]

#{0,1,5#1,2,5#2,3#3,4,4#4,5,5#5}
"""
n0.neighbors = [n1,n5]
n1.neighbors = [n2,n5]
n2.neighbors = [n3]
n3.neighbors = [n4, n4]
n5.
"""
result = test.cloneGraph(n0)

pdb.set_trace()
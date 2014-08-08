import pdb
class RegNode:
	def __init__(self, char, loop = -1):
		self.char = char
		self.loop = loop 
		self.next = None

def printNFA(nfa):
	cur = nfa
	while not cur is None:
		print cur.char, cur.loop
		cur = cur.next 
class Solution:
	def isEqual(self, s1, s2):
		return s1 == s2 or s1 == '.' or s2 == '.'
	def makeNFA(self, p):
		result = None 
		cur = None
		for char in p: 
			if char != "*":
				if result is None:
					result = RegNode(char)
					cur = result
				else:
					cur.next = RegNode(char)
					cur = cur.next
			else:
				cur.loop = 0
		cur = result
		pre = None
		#pdb.set_trace()
		while cur:
			if pre and pre.char == cur.char and pre.loop == 0 and cur.loop == 0: 
				temp = cur
				pre.next = cur.next
				del(cur)
				cur = pre.next
			else:
				pre = cur
				cur = cur.next
		return result
	def checkTailLoop(self, node):
		cur = node
		while cur:
			if cur.loop != 0:
				return False
			cur = cur.next
		return True
	def isMatch(self, s, p):
		nfa = self.makeNFA(p)
		if nfa is None:
		    return s == ""
		if s == "":
			t = nfa
			while t:
				if t.loop == -1:
					return False
				t = t.next
			return True
		scount = 0 
		status = [{'node': nfa, 'index': 0}]
		#pdb.set_trace()
		while len(status) > 0:
			curStatus = status.pop(0)
			curNode = curStatus['node']
			curIdx = curStatus['index']
			if curIdx >= len(s):
				continue
			if self.isEqual(s[curIdx], curNode.char):
				if curIdx == len(s)-1:
					if self.checkTailLoop(curNode.next):
						return True
					else:
						if curNode.loop == 0 and self.isEqual(curNode.char, s[curIdx]) and curNode.next:
							status.append({'node': curNode.next, 'index': curIdx})
						continue
				if curNode.loop == -1 and curNode.next:
					status.append({'node': curNode.next, 'index': curIdx+1})
				if curNode.loop == 0:
					if curNode.next:
						status.append({'node': curNode.next, 'index': curIdx})
					status.append({'node': curNode, 'index': curIdx+1}) 
			if curNode.loop == 0 and not self.isEqual(curNode.char, s[curIdx]) and curNode.next: 
				status.append({'node': curNode.next, 'index': curIdx})
		return False 

test = Solution()
print test.isMatch("abbbcd", "ab*bbbcd")
print test.isMatch("fs", "f.*s")
print test.isMatch("aasdf", ".*aasd.*")
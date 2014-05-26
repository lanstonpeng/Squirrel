# method: recurisve
# how to improve its performance?
# record mid result.
# similar problem: 编程之美的计算字符串的编辑距离

import pdb
class Solution:
	def count(self, w, tstart, sstart):
		if tstart == len(w):
			return 1	
		if not w[tstart] in self.word:
			return 0
		l = self.word[w[tstart]]
		c = 0
		for i in range(len(l)):
			if l[i] <= sstart or len(self.s) - l[i] < len(w) - tstart - 1:
				continue
			if l[i] in self.visited and tstart+1 in self.visited[l[i]]:
				c = c + self.visited[l[i]][tstart+1]
			else:
				c = c + self.count(w, tstart+1, l[i])
		if not sstart in self.visited:
			self.visited[sstart] = {}
		self.visited[sstart][tstart] = c
		return c
	def numDistinct(self, S, T):
		self.word = {}
		self.s = S
		self.visited = {}
		for i in range(len(S)):
			if not S[i] in self.word:
				self.word[S[i]] = []
			self.word[S[i]].append(i)
		return self.count(T, 0, -1)
test = Solution()
print (test.numDistinct("aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe", "bddabdcae"))
print (test.numDistinct("racabbitt", "rabbit"))
print (test.numDistinct("eee", "eee"))
print (test.numDistinct("raabbb", "rabb"))
print (test.numDistinct("rabbbit", "rabbit"))
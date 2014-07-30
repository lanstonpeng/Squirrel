import pdb
"""
class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
"""
class Solution:
	def isPalindrome(self, s):
		h = 0
		t = len(s)-1
		while h < t:
			if s[h] != s[t]:
				return False
			h = h + 1
			t = t - 1
		return True
	def partition(self, s): 
		if len(s) == 1:
			return [[s]]
		result = []
		for i in range(len(s)-1):
			curStr = s[0:i+1]
			if self.isPalindrome(curStr):
				subResult = self.partition(s[i+1:])
				if subResult != []:
					for subArr in subResult:
						subArr.insert(0, curStr)
						result.append(subArr)
		if self.isPalindrome(s):
			result.append([s])
		return result
test = Solution()
input_str = "aab"
input_str = "ababababababababababababcbabababababababababababa"
result = test.minCut(input_str)
print (result)
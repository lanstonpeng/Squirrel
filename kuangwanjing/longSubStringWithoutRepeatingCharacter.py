class Solution:
	# @return an integer
	def lengthOfLongestSubstring(self, s):
		if len(s) == 0:
			return 0
		infoDict = {}
		maxLength = 1
		groupStart = 0
		for i in range(len(s)-1):
			if not s[i]	in infoDict:
				infoDict[s[i]] = i
			else:
				temp = infoDict[s[i]]
				if temp >= groupStart:
					maxLength = max(maxLength, i-groupStart)
					groupStart = temp + 1 
				infoDict[s[i]] = i
		lastLength = 0
		if not s[-1] in infoDict or infoDict[s[-1]] < groupStart:
			lastLength = len(s) - groupStart
		else:
			lastLength = max(len(s) - 1 -  infoDict[s[-1]], 0, len(s) - groupStart -1)
		return max(maxLength, lastLength)
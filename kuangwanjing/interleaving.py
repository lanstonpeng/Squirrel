class Solution:
	# @return a boolean
	def isInterleave(self, s1, s2, s3):
		path = []
		len1 = len(s1)
		len2 = len(s2)
		if len1 + len2 != len(s3):
		    return False
		for j in range(len1+1):
			path.append([False] * (len2+1))
		path[0][0] = True	
		for i in range(1, len2+1):
			path[0][i] = (s2[0:i] == s3[0:i])
		for i in range(1, len1+1):
			path[i][0] = (s1[0:i] == s3[0:i])
		for i in range(1, len1+1):
			for j in range(1, len2+1):
				path[i][j] = (s1[i-1] == s3[i+j-1] and path[i-1][j]) or (s2[j-1] == s3[i+j-1] and path[i][j-1])
		return path[len1][len2]
import pdb
class Solution:
	def __init__(self):
		self.factors = [1]
		for i in range(9):
			self.factors.append(self.factors[i] * (i+1))
	def getPermutation(self, n, k):
		left = k	
		pointer = n
		chosen = []
		result = []
		for i in range(n):
			chosen.append(str(i+1))
		#pdb.set_trace()
		while pointer > 0:
			if left == 0:
				index = len(chosen)
			else:
				if left <= self.factors[pointer-1]:
					index = 1
				else:
					if left % self.factors[pointer-1] == 0:
						index = left / self.factors[pointer-1] 
						left = 0
					else: 
						index = left / self.factors[pointer-1] + 1
						left = left - (index-1) * self.factors[pointer-1] 
			result.append(chosen[index-1])
			del(chosen[index-1]) 
			pointer = pointer - 1
		return ''.join(result)

test = Solution()
for i in range(1, 25):
	print (test.getPermutation(4, i))
print (test.getPermutation(1,1))
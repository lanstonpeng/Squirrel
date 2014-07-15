import pdb
class Solution:
	def sortColors(self, A):
		if len(A) == 0:
			return
		p1 = 0
		p2 = len(A)-1
		i = 0
		while p1 <= i <= p2 and p2 >= 0 and p1 < len(A) and p1 <= p2:
			if A[i] == 0:
				A[p1] = 0
				p1 = p1 + 1
			else:
				if A[i] == 2:
					temp = A[i]
					A[i] = A[p2]
					A[p2] = temp
					p2 = p2 - 1 
					i = i - 1
			i = i + 1
		for i in range(p1, p2+1):
			A[i] = 1
		print (A)
test = Solution()

A = [2,1,0,2,0,2,1,1]
test.sortColors(A)
A = [1]
test.sortColors(A)
A = [0, 0, 0]
test.sortColors(A)
A = [2, 2, 2]
test.sortColors(A)
A = [1,0]
test.sortColors(A)
A = [1,2,0]
test.sortColors(A)
A = [1,2,1]
test.sortColors(A)
A = [1,2,1, 0, 2, 1, 0, 1, 1, 2, 0, 2, 1, 0, 0]
test.sortColors(A)
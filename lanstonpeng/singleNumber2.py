class Solution:
# @param A, a list of integer
# @return an integer
	def singleNumber(self, A):
		arr = [0]*len(A)
		n = len(A)
		minusCount = 0
		symbol = 1
		for i in range(n):
			temp = A[i]
			l = 0
			while temp:
				if temp < 0:
					minusCount+=1
					temp = abs(temp)
				arr[ n - 1 - l ] += temp % 2
				temp = temp/2
				#print temp
				l+=1
		#print arr
		for k in range(len(arr)):
			if arr[k] % 3 != 0:
				arr[k] = 1
			else:
				arr[k] = 0
		for k in range(len(arr)):
			if arr[k]!=0:
				temp+=pow(2,len(arr) - 1 - k)
		print minusCount
		if minusCount % 3 == 0 and minusCount > 0 or minusCount == 0:
			symbol = 1
		else :
			symbol = -1
		return temp * symbol

s = Solution()
#print s.singleNumber([-2,-2,1,1,-3,1,-3,-3,-4,-2])
print s.singleNumber([1])
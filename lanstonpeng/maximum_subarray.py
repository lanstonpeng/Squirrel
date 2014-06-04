class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
    	result = 0
    	for i in range(len(A)):
    		temp = 0
    		for k in range(i,len(A)):
    			temp += A[k];
    			if temp > result:
    				result = temp
    	return result

s = Solution()
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
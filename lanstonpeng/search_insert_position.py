class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
    	for i in range(len(A)):
    		if A[i] >= target:
    			return i
    	return len(A)

A = [1,3,5,6]
A2 = [1,3,5,6]
A3 = [1,3,5,6]
target = 0
target2 = 7
target3 = 2
s = Solution()
print s.searchInsert(A3,target3)
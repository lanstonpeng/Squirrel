class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        result = 0
        for i in range(len(A)):
            temp = 0
            for k in range(i,0,-1):
                temp += A[k]
                if temp > result:
                    result = temp
        return result
    def maxSubArrSum(self,A):
        arr = [0] * len(A)
        arr[0] = A[0]
        result = arr[0]
        for i in range(1,len(A)):
            arr[i] = max(arr[i-1] + A[i],A[i])
            result = max(arr[i],result)
        return result


s = Solution()
print s.maxSubArrSum([-2,1,-3,4,-1,2,1,-5,4])
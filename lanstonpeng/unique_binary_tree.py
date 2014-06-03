class Solution:
    # @return an integer
    def numTrees(self, n):
        print self.dp(n)
        print self.recur(n)
    def recur(self,n):
    	temp = 0
    	if n == 0 or n == 1 :
    		return 1
    	else:
    		for i in range(1,n+1):
    			temp = temp + self.recur(i-1) * self.recur(n - i)
    	return temp
    def dp(self,n):
    	arr = [0] * (n+1)
        arr[0] = 1
        arr[1] = 1
    	for i in range(2,n + 1):
            for k in range(1,i + 1):
                arr[i] += arr[k-1] * arr[i-k]
    	return arr[n]

s = Solution()
print s.numTrees(3)

class Solution:
    # @return an integer
    def numTrees(self, n):
        return self.dp(n)
    def recur(self,n):
    	temp = 0
    	if n == 0 or n == 1 :
    		return 1
    	else:
    		for i in range(1,n+1):
    			temp = temp + self.recur(i-1) * self.recur(n - i)
    		return temp
    def dp(self,n):
    	arr = [0] * n
    	for i in range(0,n+1):
    		if i == 0 or i == 1:
    			arr[i] = 1
    		else:
    			for k in range(1,n):
    				arr[i] += arr[k-1] * arr[n-k]
    	return arr[n-1] 

s = Solution()
print s.numTrees(2)

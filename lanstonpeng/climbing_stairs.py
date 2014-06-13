class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
    	self.arr = [0]* (n+1)
    	self.arr[0] = 1
    	self.arr[1] = 1
    	return self.recur(n)
    def recur(self,n):
    	if self.arr[n]!=0:
    		return self.arr[n]
    	else:
    		self.arr[n] = self.recur(n-1) + self.recur(n-2)
    		return self.arr[n]
s = Solution()
'''
3 
1+2
2+1
1+1+1
'''
print s.climbStairs(35)
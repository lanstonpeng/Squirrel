class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
    	if len(prices) == 0:
    		return 0
    	low = 0
    	high = 1
    	result = 0
        while high < len(prices):
        	if prices[high] < prices[low]:
        		low = high
        		high = high + 1
        	else:
        		temp = prices[high] - prices[low]
        		if temp > result:
        			result = temp
        		high = high + 1
        return result




s = Solution()
print s.maxProfit([2,6,1,5,1])
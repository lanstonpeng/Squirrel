import pdb
class Solution:
	# @param prices, a list of integer
	# @return an integer
	def maxProfit(self, prices):
		if len(prices) == 0:
			return 0
		maxPrice = prices[-1] 
		profit = 0
		length = len(prices)
		for i in range(length):
			maxPrice = max(prices[length-i-1], maxPrice)
			profit = max(maxPrice-prices[length-i-1], profit)
		return profit

test = Solution()
input = []
print (test.maxProfit(input))
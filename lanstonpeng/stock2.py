import pdb
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        low = 0
        high = 1
        result = 0
        tempSum = 0
        #pdb.set_trace()
        while high < len(prices):
            if prices[high] < prices[low]:
                low = high
                high = high + 1
                result = result + tempSum
                temp = 0
                tempSum = 0
            else:
                temp = prices[high] - prices[low]
                if temp > tempSum:
                    tempSum = temp
                else:
                    low = high
                    result = result + tempSum
                    temp = 0
                    tempSum = 0
                high = high + 1

        return result + tempSum

s = Solution()
#print s.maxProfit([6,1,3,2,4,7])
print s.maxProfit([2,3,1,5,6])

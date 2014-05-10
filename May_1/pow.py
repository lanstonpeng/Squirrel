class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        if n == 0:
            return 1;
        return x * self.pow(x, abs(n) - 1) * n/abs(n)

s = Solution()
#print s.pow(8.88023, 3)
#print s.pow(34.00515, -3)
print s.pow(1.00001, 123)

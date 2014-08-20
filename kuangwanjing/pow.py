class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        negative = False
        if n < 0:
            negative = True
            n = -n
        y = 1
        while True:
            t = n % 2
            n = n / 2
            if t == 1:
                y = y * x
            if n == 0:
                break
            x = x * x
        if negative:
            return 1/float(y)
        else:
            return y

test = Solution()
print (test.pow(21.32, -3))
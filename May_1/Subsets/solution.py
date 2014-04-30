class Solution:
    def subsets(self, S):
        self.S = S
        self.S.sort()
        self.sLen = len(S)
        self.temp = []
        self.result = []
        self.dfs(0)
        print self.result
    def dfs(self,step):
        if step == self.sLen:
            self.result.append(list(self.temp))
            return
        self.dfs(step+1)
        self.temp.append(self.S[step])
        self.dfs(step+1)
        self.temp.pop()


s = Solution()
#s.subsets([1,2,3])
#s.subsets([0])
s.subsets([4,1,0])

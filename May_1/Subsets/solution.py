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
    def noneRecur(self,S):
        stack = [0] * len(S)
        self.result = []
        self.temp = []
        for i in range(len(stack)):
            stack[i] = 1 - stack[i]
            for idx in range(i + 1,len(stack)):
                stack[idx] = 1 - stack[idx]
                print stack
                for k in range(len(stack)):
                    if stack[k] == 1:
                        self.temp.append(S[k])
                self.result.append(list(self.temp))
                self.temp = []
        print self.result



s = Solution()
#s.subsets([1,2,3])
#s.subsets([0])
#s.subsets([4,1,1])
s.noneRecur([1,4,5])

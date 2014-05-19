'''
Status

Time Spending
'''
import pdb
class Solution:
    def letterCombinations(self, digits):
        self.dList = list(digits)
        self.dListLen = len(self.dList)
        self.temp = []
        self.result = []
        self.keyIndex = 0
        self.dfs()
        print self.result
    def dfs(self):
        #pdb.set_trace()
        if len(self.temp) == self.dListLen:
            self.result.append(list(self.temp))
            return
        if self.keyIndex < self.dListLen:
            key = self.dList[self.keyIndex]
        else:
            return
        for item in self.getAlphabets(key):
            self.temp.append(item)
            self.keyIndex +=1
            self.dfs()
            self.keyIndex -=1
            self.temp.pop()
    def iteration(self):
        self.visited = [0]*self.dListLen

    def getAlphabets(self,number):
        return {
                '1':[''],
                '2':['a','b','c'],
                '3':['d','e','f'],
                '4':['g','h','i'],
                '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z'],
                '0':['']
                }.get(number,'')

s = Solution()
s. letterCombinations("23")

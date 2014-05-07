'''
s = "LeetCode"
dic = ["leet","code"]
return True
'''
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dic):
        for i in range(len(dic)): #n
            l = len(dic[i])
            idx = s.find(dic[i])  #n*m(if implementing by myself)
            if idx > -1:
                s = s[:idx] + s[idx+l:]
            else:
                return False
        if(len(s) == 0):
            return True
        pass

s = Solution()
print s.wordBreak("leetcodeyouku",["youku","leet","code"])

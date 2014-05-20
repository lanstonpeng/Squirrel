'''
s = "LeetCode"
dic = ["leet","code"]
return True
'''
import pprint
import pdb

class TreeNode:
 def __init__(self, x):
     self.val = x
     self.left = None
     self.right = None

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dic):
        for i in range(len(dic)): #n
            dic = list(dic)
            l = len(dic[i])
            idx = s.find(dic[i])  #n*m(if implementing by myself)
            if idx > -1:
                s = s[:idx] + s[idx+l:]
            else:
                return False
        if(len(s) == 0):
            return True
        else:
            return False
    def wordBreak2(self,s,arr):
        root = {}
        for word in arr:
            node = root
            for idx in range(len(word)):
                char = word[idx]
                if char in node:
                    node = node[char]
                    if idx == len(word) -1:
                        node["#"] = 1
                else:
                    node[char] = {}
                    node = node[char]
                    if idx == len(word) -1:
                        node["#"] = 1
        node = root
        ii = 0
        #pdb.set_trace()
        while 1:
            index = ii
            item = s[index]
            node = root
            while 1:
                if item in node:
                    if index == len(s) and "#" in node:
                        return True
                    node = node[item]
                    # see if the word is cut
                    ii = ii + 1
                    index = ii
                    if index > len(s):
                        return False
                    if "#" in node:
                        break
                    #item = s[index]
                else:
                    if item in root:
                        #if "#" not in node:
                        #    return False
                        break;
                    else:
                        return False
        #pp = pprint.PrettyPrinter(indent=4)
        #pp.pprint(root)



s = Solution()
print s.wordBreak2("leetcodeyouku",["youku","leet","code"])
print s.wordBreak2("bb",["a","b","bbb"])
print s.wordBreak2("cars", ["car","ca","rs"])
print s.wordBreak2("aaaaaaa", ["aaaa","aa"])
print s.wordBreak2("a",["a"])

'''
bad case
---------
Input:	"bb", ["a","b","bbb","bbbb"]
Output:	false
Expected:	true
'''

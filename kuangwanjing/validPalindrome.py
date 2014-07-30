"""
class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
"""
class Solution:
    def isLetterAndNumber(self, c):
        return "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9"
    def findNext(self, s, p):
        while p <= len(s)-1 and not self.isLetterAndNumber(s[p]):
            p = p + 1
        return p
    def findPrev(self, s, p):
        while p >= 0 and not self.isLetterAndNumber(s[p]):
            p = p - 1
        return p
    def isEqual(self, c1, c2):
        return c1.lower() == c2.lower() 
    def isPalindrome(self, s):
        head = self.findNext(s, 0)
        tail = self.findPrev(s, len(s)-1)
        while head <= tail:
            if not self.isEqual(s[head], s[tail]):
                return False
            head = head + 1
            tail = tail - 1
            head = self.findNext(s, head)
            tail = self.findPrev(s, tail)
        return True
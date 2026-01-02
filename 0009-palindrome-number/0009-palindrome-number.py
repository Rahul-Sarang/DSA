 
class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        rev = ""
        
        for i in range(len(s) - 1, -1, -1):
            rev += s[i]
        
        return s == rev

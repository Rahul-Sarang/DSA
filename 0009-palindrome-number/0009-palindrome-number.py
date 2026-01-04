class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        realX = x
        rev = 0
        while x > 0:
            num = x % 10
            rev = rev * 10 + num
            x = x // 10
        
        return realX == rev
obj = Solution()
print(obj.isPalindrome(121))  
print(obj.isPalindrome(123))   
print(obj.isPalindrome(-121)) 
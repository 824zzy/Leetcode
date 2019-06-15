""" Just write a helper function to check palindrome
basiclly type is two pointer.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1
        
        while i<j:
            if s[i] != s[j]:
                return self.check(s, i+1, j) or self.check(s, i, j-1)
            i += 1
            j -= 1
        return True
    
    def check(self, s: str, i: int, j: int) -> bool:
        while i<j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
        
""" Here a better solution
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s[i] != s[-i-1]
                r = len(s) - i
            return s[i+1:r] == s[i+1:r][::-1] or s[i:r-1] == s[i:r-1][::-1]
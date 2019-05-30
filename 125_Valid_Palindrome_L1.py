""" usage of build-in string methodd
1. str.split()
2. str.lower()/upper()
3. str.isalpha()/isnumeric()
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = ''.join(s.split()).lower()
        words = [w for w in words if w.isalpha() or w.isnumeric()]
        
        for i, j in zip(words, reversed(words)):
            if i != j:
                return False
        return True
        
        
        
""" Facebook
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ''.join(s.split()).lower()
        words = [c for c in sentence if c.isalpha() or c.isnumeric()]
        return words==words[::-1]
    
    
from string import punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ', '')
        for p in punctuation:
            s = s.replace(p, '')
        return s==s[::-1]
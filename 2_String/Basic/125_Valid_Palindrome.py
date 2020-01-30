""" Facebook
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = ''.join(s.split()).lower()
        words = [c for c in sentence if c.isalpha() or c.isnumeric()]
        return words==words[::-1]
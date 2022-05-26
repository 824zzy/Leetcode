""" L0: https://leetcode.com/problems/reverse-prefix-of-word/
find the character
"""
class Solution:
    def reversePrefix(self, word: str, c: str) -> str:
        word = list(word)
        for i, w in enumerate(word):
            if w==c: return "".join(word[:i+1][::-1]+word[i+1:])
        return "".join(word)
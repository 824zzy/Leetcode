""" https://leetcode.com/problems/reverse-prefix-of-word/
string simulation
"""


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        i = word.index(ch)
        return word[:i+1][::-1] + word[i+1:]

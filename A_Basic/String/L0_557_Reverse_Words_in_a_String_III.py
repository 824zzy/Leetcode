""" https://leetcode.com/problems/reverse-words-in-a-string-iii/
split string and reverse each substring
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split()])

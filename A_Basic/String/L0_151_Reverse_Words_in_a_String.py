""" https://leetcode.com/problems/reverse-prefix-of-word/submissions/
split and reverse the string
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])

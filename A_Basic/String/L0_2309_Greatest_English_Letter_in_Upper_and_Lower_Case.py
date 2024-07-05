""" https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/
check uppercase from a to z
"""


class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        for i in reversed(range(26)):
            c = chr(97 + i)
            if c.upper() in s and c.lower() in s:
                return c.upper()
        return ""

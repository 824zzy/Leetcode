""" https://leetcode.com/problems/determine-if-string-halves-are-alike/description/
simulation
"""


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a, b = 0, 0
        for i in range(len(s) // 2):
            a += s[i] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
            b += s[~i] in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
        return a == b

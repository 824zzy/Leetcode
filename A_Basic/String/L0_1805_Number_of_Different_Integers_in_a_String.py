""" https://leetcode.com/problems/number-of-different-integers-in-a-string/
check if character is digit by `if c.isdigit():`
"""


class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        word = "".join([c if c.isdigit() else " " for c in word])
        return len(set(map(int, word.split())))

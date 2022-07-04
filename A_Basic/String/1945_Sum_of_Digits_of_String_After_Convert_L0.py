""" https://leetcode.com/problems/sum-of-digits-of-string-after-convert/
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.
"""
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        A = "".join([str(ord(c)-ord('a')+1) for c in s])
        for _ in range(k):
            A = str(sum(map(int, list(A))))
        return int(A)
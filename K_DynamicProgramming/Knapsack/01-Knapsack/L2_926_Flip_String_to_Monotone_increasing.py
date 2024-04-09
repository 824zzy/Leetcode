""" https://leetcode.com/problems/flip-string-to-monotone-increasing/
Interesting knap sack probem:

In order to keep monotonic property, we have to record whether we flip 0 to 1 in i-th position.
So there are four conditions:
1. if we have flipped 0 to 1:
    if s[i]==1, we do nothing
    if s[i]==0, we flip 0 to 1
2. if we haven't flipped 0 to 1:
    if s[i]==0, we can flip it and set flipped0to1, or do nothing
    if s[i]==1, we have to flip 1 to 0
"""
from header import *


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @cache
        def dp(i, flipped0to1):
            if i == len(s):
                return 0
            if flipped0to1:
                if s[i] == '1':
                    return dp(i + 1, flipped0to1)
                elif s[i] == '0':
                    return 1 + dp(i + 1, flipped0to1)
            else:
                if s[i] == '0':
                    return min(1 + dp(i + 1, True), dp(i + 1, False))
                elif s[i] == '1':
                    return min(1 + dp(i + 1, False), dp(i + 1, True))

        return dp(0, False)

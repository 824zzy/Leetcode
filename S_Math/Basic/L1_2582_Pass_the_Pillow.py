""" https://leetcode.com/problems/pass-the-pillow/
observation: each pass contains n-1 steps
"""
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        x, i = divmod(time, n-1)
        if x&1:
            return n-i
        else:
            return i+1
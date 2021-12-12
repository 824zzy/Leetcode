""" https://leetcode.com/problems/rings-and-rods/
use bitmask to represent RGB and "or" operation to find out how many different rings in a rod
"""
class Solution:
    def countPoints(self, A: str) -> int:
        mp = dict(zip("RBG", [1,2,4]))
        cnt = [0]*10
        for i in range(0, len(A), 2):
            cnt[int(A[i+1])] |= mp[A[i]]
        return sum(x==7 for x in cnt)
""" https://leetcode.com/problems/longest-consecutive-sequence/
1. find left and right end-points to compute the sequence length
2. update end-points in the hash table
"""
class Solution:
    def longestConsecutive(self, A: List[int]) -> int:
        mp = {}
        ans = 0
        
        for x in A:
            if x not in mp:
                l = mp.get(x-1, 0)
                r = mp.get(x+1, 0)
                L = l+r+1
                mp[x] = mp[x-l] = mp[x+r] = L       
        return max(mp.values(), default=0)
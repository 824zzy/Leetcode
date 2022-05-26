""" https://leetcode.com/problems/longest-consecutive-sequence/
Find left and right endpoint and sequence length then update hash table
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d, ans = {}, 0
        for n in nums:
            if n not in d:
                l = d.get(n-1, 0)
                r = d.get(n+1, 0)
                lens = l + r + 1
                ans = max(ans, lens)
                d[n-l] = d[n] = d[n+r] = lens
        return ans
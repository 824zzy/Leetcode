""" https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
variance of two sum: (x+y)%60=0 => y%60=-x%60 => y=(-x%60)%60
"""
class Solution:
    def numPairsDivisibleBy60(self, A: List[int]) -> int:
        seen = defaultdict(int)
        ans = 0
        for x in A:
            ans += seen[(60-x%60)%60]
            seen[x%60] += 1
        return ans
""" https://leetcode.com/problems/count-hills-and-valleys-in-an-array/
1. only keep climax by itertools.groupby
2. find hills and valleys
"""
class Solution:
    def countHillValley(self, A: List[int]) -> int:
        # only keep climax
        A = [k for k, v in groupby(A)]
        ans = 0
        # find hills and valleys
        for i in range(1, len(A)-1):
            if A[i-1]>A[i]<A[i+1] or A[i-1]<A[i]>A[i+1]: ans += 1
        return ans
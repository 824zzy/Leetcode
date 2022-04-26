""" https://leetcode.com/problems/teemo-attacking/
find right most reachable time at each index
"""
class Solution:
    def findPoisonedDuration(self, A: List[int], d: int) -> int:
        ans = 0
        for i in range(len(A)-1):
            ans += min(d, A[i+1]-A[i])
        return ans+d
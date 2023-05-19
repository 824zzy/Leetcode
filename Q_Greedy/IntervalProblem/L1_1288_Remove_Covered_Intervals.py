""" https://leetcode.com/problems/remove-covered-intervals/
"""
class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x:(x[0], -x[1]))
        ans = 0
        right = 0

        for i in range(len(A)):
            if A[i][1]>right: ans += 1
            right = max(right, A[i][1])
        return ans
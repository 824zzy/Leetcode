""" https://leetcode.com/problems/longest-turbulent-subarray/submissions/
find maximum length by recording up&down states.
"""
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        ans, up, down = 1, 1, 1
        for i in range(1, len(A)):
            if A[i]<A[i-1]: 
                up, down = 1, up+1
            elif A[i]>A[i-1]: up, down = down+1, 1
            else: up, down = 1, 1
            ans = max([ans, up, down])
        return ans
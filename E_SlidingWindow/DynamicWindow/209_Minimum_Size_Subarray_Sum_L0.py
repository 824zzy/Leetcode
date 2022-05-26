""" https://leetcode.com/problems/minimum-size-subarray-sum/
the k is given, just follow the template to solve this problem.
"""
class Solution:
    def minSubArrayLen(self, t: int, A: List[int]) -> int:
        i = 0
        ans = inf
        for j in range(len(A)):
            t -= A[j]
            while t<=0:
                ans = min(ans, j-i+1)
                t += A[i]
                i += 1
        return ans if ans!=inf else 0
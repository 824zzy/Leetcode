""" https://leetcode.com/problems/length-of-the-longest-subsequence-that-sums-to-target/
"""
from header import *


class Solution:
    def lengthOfLongestSubsequence(self, A: List[int], t: int) -> int:
        dp = [[0] * (t + 1) for _ in range(len(A) + 1)]
        for i in range(t):
            dp[-1][i] = -inf
        dp[-1][t] = 0

        for i in range(len(A) - 1, -1, -1):
            for j in range(t):
                # skip
                ans1 = dp[i + 1][j]
                # choose
                ans2 = -inf
                if j + A[i] <= t:
                    ans2 = 1 + dp[i + 1][j + A[i]]
                dp[i][j] = max(ans1, ans2)
        return dp[0][0] if dp[0][0] != -inf else -1


# top down will get memory limit exceeded
class Solution:
    def lengthOfLongestSubsequence(self, A: List[int], t: int) -> int:
        @cache
        def dp(i, sm):
            if i == len(A):
                if sm == t:
                    return 0
                else:
                    return -inf
            # skip
            ans1 = dp(i + 1, sm)
            # choose
            ans2 = -inf
            if sm + A[i] <= t:
                ans2 = 1 + dp(i + 1, sm + A[i])
            return max(ans1, ans2)
        ans = dp(0, 0)
        return ans if ans != -inf else -1


"""
[1,2,3,4,5]
9
[4,1,3,2,1,5]
7
[1,1,5,4,5]
3
[39,33,50,97,91,36,87,66,12,90,22,10,17,99,52,80,82,71,48,29,77,75,33,5,72,97,95,82,70,100,43,7,54,54,23,5,34,22,34,67,62,22,94,70,6,52,28,17,88,21,49,12,60,46,11,16,44,15,76,66,85,38,24,95,46,80,46,91]
1000
[21,20,28,56,72,81,70,77,68,51,81,32,95,41,38,16,99,92,54,87,25,82,59,72,61,91,93,33,37,1,54,74,22,94,48,76,48,6,60,27,3,16,61,54,19,72,59,79,5,100,80,99,45,94,6,22,55,36,27,4,61,8,29,42,75,57,74,68,96,52,79,59,27,74,56,87,6,62,60,90,56,81,97,51,8,24,14,66,71,57,15,51,11,85,72,91,8,32,16,71]
742
[27,29,80,37,77,60,12,54,52,45,56,33,6,59,85,49,28,15,15,17,87,50,2,8,8,13,39,88,91,75,56,52,27,66,20,5,4,55,71,99,54,71,28,61,4,67,52,44,64,86,40,100,30,86,39,29,60,23,56,7,84,52,40,85,79,68,88,47,22,9,88,34,54,85,59,67,34,29,74,78,47,59,34,49,77,91,78,96,89,90,29,69,58,61,8,27,41,92,51,89]
774
"""

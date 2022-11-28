""" https://leetcode.com/problems/arithmetic-slices-ii-subsequence/
refer to: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/1455137/Python-short-dp-explained
We have to use bottom up dp since we use hash table as states
"""
from header import *

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        ans = 0
        dp = [Counter() for i in range(len(A))]
        for i in range(len(A)):
            for j in range(i):
                dp[i][A[i]-A[j]] += dp[j][A[i]-A[j]]+1
                ans += dp[j][A[i]-A[j]]
        return ans


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        self.ans = 0
        @cache
        def dp(i):
            cnt = Counter() 
            for j in range(i+1, len(A)):
                cnt[A[i]-A[j]] += dp(j)[A[i]-A[j]]+1
                self.ans += dp(j)[A[i]-A[j]]
            return cnt

        dp(0)
        return self.ans
""" https://leetcode.com/problems/restore-the-array/
dp[i] = sum(dp[j]) for all j in [i+1, i+2, ..., i+9] if s[j:i+1] is valid
"""
from header import *


class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        @cache
        def dp(i):
            if i == len(s):
                return 1
            if s[i] == "0":
                return 0
            ans = 0
            # at most 9 steps since k<=10**9
            for j in range(i, len(s)):
                x = int(s[i : j + 1])
                if x > k:
                    break
                ans += dp(j + 1)
            return ans % (10 ** 9 + 7)

        return dp(0) % (10 ** 9 + 7)


"""
"1000"
10000
"1000"
10
"1317"
2000
"420513611027"
20
"""

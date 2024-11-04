""" https://leetcode.com/problems/delete-columns-to-make-sorted-iii/
"""

from header import *


# LIS template
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        A = list(zip(*strs))
        print(A)

        dp = [1] * len(A)
        for i in range(len(A)):
            for j in range(i):
                if all(x <= y for x, y in zip(A[j], A[i])):
                    dp[i] = max(dp[i], dp[j] + 1)
        return len(A) - max(dp)


# Knap sack
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        A = list(zip(*strs))

        @cache
        def dp(i, pre):
            if i == len(A):
                return 0
            # delete
            ans = 1 + dp(i + 1, pre)
            # keep
            if pre == None:
                ans = min(ans, dp(i + 1, A[i]))
            else:
                for a, b in zip(A[i], pre):
                    if a < b:
                        break
                else:
                    ans = min(ans, dp(i + 1, A[i]))
            return ans

        return dp(0, None)


"""
["babca","bbazb"]
["edcba"]
["ghi","def","abc"]
["aaa","aaa","aaa"]
"""

""" https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/
dp[i] denotes if A[i] can be the last element of a valid partition.

Time complexity: O(N) ~= 10^5
"""
from header import *

# bottom up


class Solution:
    def validPartition(self, A: List[int]) -> bool:
        dp = [False for _ in range(len(A) + 1)]
        dp[0] = True

        for i in range(len(A)):
            if i - 1 >= 0 and A[i] == A[i - 1]:
                dp[i + 1] |= dp[i - 1]
            if i - 2 >= 0:
                if A[i] == A[i - 1] == A[i - 2] or A[i - 2] + \
                        2 == A[i - 1] + 1 == A[i]:
                    dp[i + 1] |= dp[i - 2]
        return dp[-1]


# iterative top down solution
class Solution:
    def validPartition(self, A: List[int]) -> bool:
        dp = [False for _ in range(len(A) + 1)]
        dp[-1] = True

        for i in reversed(range(len(A))):
            if i + 1 < len(A) and A[i] == A[i + 1]:
                dp[i] |= dp[i + 2]
            if i + 2 < len(A):
                if A[i] == A[i + 1] == A[i + 2] or A[i] + \
                        2 == A[i + 1] + 1 == A[i + 2]:
                    dp[i] |= dp[i + 3]
        return dp[0]


# recursive top down solution
class Solution:
    def validPartition(self, A: List[int]) -> bool:
        @cache
        def dp(i):
            if i == len(A):
                return True
            ans = False
            if i + 1 < len(A) and A[i] == A[i + 1]:
                ans |= dp(i + 2)
            if i + 2 < len(A):
                if A[i] == A[i + 1] == A[i + 2] or A[i] + \
                        2 == A[i + 1] + 1 == A[i + 2]:
                    ans |= dp(i + 3)
            return ans

        return dp(0)


""" true false false true
[4,4,4,5,6]
[1,1,1,2]
[993335,993336,993337,993338,993339,993340,993341]
[803201,803201,803201,803201,803202,803203]
"""

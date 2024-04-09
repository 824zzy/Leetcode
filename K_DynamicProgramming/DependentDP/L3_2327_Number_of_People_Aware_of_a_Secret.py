""" https://leetcode.com/problems/number-of-people-aware-of-a-secret/
this problem is harder than the fourth problem to me.
dp(i) means the number of people who found the secret on ith day.
"""


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        @cache
        def dp(i):
            # i+delay>n means the person cannot share the secret with new
            # person
            if i + delay > n:
                return 1
            ans = 1
            # i+forget<=n means the person will forget the secret before n-th
            # day
            if i + forget <= n:
                ans = 0
            for j in range(i + delay, min(i + forget, n + 1)):
                ans += dp(j)
            return ans

        return dp(1) % (10**9 + 7)


""" 6 2 4
dp(1): dp(3)+dp(4)
dp(3): dp(5)+dp(6)
dp(4): dp(6)
"""

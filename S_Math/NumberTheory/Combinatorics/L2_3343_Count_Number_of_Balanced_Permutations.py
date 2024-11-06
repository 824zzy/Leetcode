""" https://leetcode.com/problems/count-number-of-balanced-permutations/
Permutation problem = Combination problem + calculate permutation
1. convert the problem into knapsack: select floor(n/2) numbers from A, and the sum of numbers is sum(A)/2
2. The combination of multiset of size n with i distinct numbers: 
    n!/(k1 * k2 * ... * ki), where k is the count of duplicates
3. Answer is: valid combinations * (n1!) * (n2!) / (k1 * k2 * ... * ki)
"""

from header import *


class Solution:
    def countBalancedPermutations(self, s: str) -> int:
        MOD = 10**9 + 7
        MX = 81
        fac = [0] * MX
        fac[0] = 1
        for i in range(1, MX):
            fac[i] = fac[i - 1] * i % MOD
        inv_f = [0] * MX  # inv_f[i] = i!^-1
        inv_f[-1] = pow(fac[-1], -1, MOD)
        for i in range(MX - 1, 0, -1):
            inv_f[i - 1] = inv_f[i] * i % MOD

        cnt = [0] * 10
        total = 0
        s = list(map(int, s))
        for c in map(int, s):
            cnt[c] += 1
            total += c
        if total % 2:
            return 0

        @cache
        def dp(i, left, diff):
            """
            count valid combinations
            """
            if i == len(s):
                return 1 if left == 0 and diff == 0 else 0
            x = int(s[i])
            # skip
            ans = dp(i + 1, left, diff + x)
            if left:
                # choose
                ans = (ans + dp(i + 1, left - 1, diff - x)) % MOD
            return ans

        n = len(s)
        n1, n2 = n // 2, n - n // 2
        ans = dp(0, n1, 0)
        dp.cache_clear()
        ans = ans * fac[n1] * fac[n2]
        for c in cnt:
            ans *= inv_f[c]
        return ans % MOD


"""
"123"
"112"
"12345"
"11"
"""

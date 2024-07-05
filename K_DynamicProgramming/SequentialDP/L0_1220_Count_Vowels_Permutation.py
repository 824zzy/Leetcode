""" https://leetcode.com/problems/count-vowels-permutation/
Hash table dp using a,e,i,o,u as key and cumulative sum as value.
"""
from header import *

# Time complexity: O(5*N), where N is the length of A
# Space complexity: O(5*N), where N is the length of A


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @cache
        def dp(i, prev):
            if i == n:
                return 1
            ans = 0
            if prev == "a":
                ans += dp(i + 1, "e")
            elif prev == "e":
                ans += dp(i + 1, "a") + dp(i + 1, "i")
            elif prev == "i":
                ans += dp(i + 1, "a") + dp(i + 1, "e") + dp(i + 1, "o") + dp(i + 1, "u")
            elif prev == "o":
                ans += dp(i + 1, "i") + dp(i + 1, "u")
            elif prev == "u":
                ans += dp(i + 1, "a")
            return ans % (10 ** 9 + 7)

        return sum(dp(1, c) for c in "aeiou") % (10 ** 9 + 7)


# Time complexity: O(5*N), where N is the length of A
# Space complexity: O(k), where k is 5


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        for _ in range(n - 1):
            a = dp["e"]
            e = dp["a"] + dp["i"]
            i = dp["a"] + dp["e"] + dp["o"] + dp["u"]
            o = dp["i"] + dp["u"]
            u = dp["a"]
            dp["a"], dp["e"], dp["i"], dp["o"], dp["u"] = a, e, i, o, u
        return sum(dp.values()) % (10 ** 9 + 7)

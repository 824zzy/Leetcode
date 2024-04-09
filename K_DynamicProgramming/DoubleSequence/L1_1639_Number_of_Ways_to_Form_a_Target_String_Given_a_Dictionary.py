""" https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/
hash table + dp


"""
from header import *


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        word_sets = [Counter(x) for x in list(zip(*words))]

        @cache
        def dp(i, j):
            if j == len(target):
                return 1
            if i == len(word_sets):
                return 0

            ans = dp(i + 1, j)
            if target[j] in word_sets[i]:
                ans += word_sets[i][target[j]] * dp(i + 1, j + 1)
            return ans % (10**9 + 7)

        return dp(0, 0)

""" https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/
translate the problem into: find the maximum subarray that at most contains Counter(s)-k*('a'+'b'+'b')
"""

from header import *


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        for x in "abc":
            cnt[x] -= k
            if cnt[x] < 0:
                return -1

        i = 0
        ans = 0
        for j in range(len(s)):
            cnt[s[j]] -= 1
            while cnt[s[j]] < 0:
                cnt[s[i]] += 1
                i += 1
            ans = max(ans, j - i + 1)
        return len(s) - ans


# binary search also works
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def fn(x):
            cnt = Counter(s[-x:])
            if cnt["a"] >= k and cnt["b"] >= k and cnt["c"] >= k:
                return True
            for i in range(x):
                cnt[s[i]] += 1
                cnt[s[-x + i]] -= 1
                if cnt["a"] >= k and cnt["b"] >= k and cnt["c"] >= k:
                    return True
            return False

        l, r = 0, len(s) + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l if l != len(s) + 1 else -1

""" https://leetcode.com/problems/longest-substring-of-all-vowels-in-order/
sliding window like two pointers
"""
from header import *

# use `unique` to mark the legit substring


class Solution:
    def longestBeautifulSubstring(self, A: str) -> int:
        i = 0
        ans = 0
        unique = 1
        for j in range(1, len(A)):
            if A[j - 1] > A[j]:
                i = j
                unique = 1
            elif A[j - 1] < A[j]:
                unique += 1
            if unique == 5:
                ans = max(ans, j - i + 1)
        return ans


# or use five rules to check if the substring is legit


class Solution:
    def longestBeautifulSubstring(self, A: str) -> int:
        def check(seen, cnt, k, v):
            seen.append(k)
            cnt += v
            if (
                (len(seen) == 1 and seen == ["a"])
                or (len(seen) == 2 and seen == ["a", "e"])
                or (len(seen) == 3 and seen == ["a", "e", "i"])
                or (len(seen) == 4 and seen == ["a", "e", "i", "o"])
                or (len(seen) == 5 and seen == ["a", "e", "i", "o", "u"])
            ):
                return seen, cnt
            elif k == "a":
                return ["a"], v
            else:
                return [], 0

        A = [[k, len(list(v))] for k, v in groupby(A)]
        seen = []
        ans = 0
        cnt = 0
        for k, v in A:
            seen, cnt = check(seen, cnt, k, v)
            if len(seen) == 5:
                ans = max(ans, cnt)
                seen = []
                cnt = 0
        return ans

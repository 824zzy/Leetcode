""" https://leetcode.com/problems/orderly-queue/description/
There are two cases:
1. k==1, we can only rotate the string, so the result is the minimum string
2. k>1, we can reorder the string, so the result is the original string
"""


class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k > 1:
            return "".join(sorted(s))
        cand = [s[i:] + s[:i] for i in range(len(s))]
        return min(cand)

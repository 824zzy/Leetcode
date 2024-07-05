""" https://leetcode.com/problems/calculate-digit-sum-of-a-string/
build next string by calculating digit sum
"""


class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nextS = ""
            for i in range(0, len(s), k):
                nextS += str(sum([int(x) for x in s[i : i + k]]))
            s = nextS
        return s

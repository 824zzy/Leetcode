""" https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        if n & 1:
            return ans + [0]
        else:
            return ans

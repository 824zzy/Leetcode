""" L0: https://leetcode.com/problems/count-square-sum-triples/
save time complexity by: k<=n and int(k)*int(k)==k*k
"""


class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                k = sqrt(i * i + j * j)
                if k <= n and int(k) * int(k) == k * k:
                    ans += 2
        return ans

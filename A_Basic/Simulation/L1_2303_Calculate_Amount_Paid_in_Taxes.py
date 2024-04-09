""" https://leetcode.com/problems/calculate-amount-paid-in-taxes/
"""


class Solution:
    def calculateTax(self, A: List[List[int]], income: int) -> float:
        ans = 0
        pre = 0
        for cur, p in A:
            cur = min(cur, income)
            ans += (cur - pre) * p
            pre = cur
        return ans / 100

# modify income on the fly


class Solution:
    def calculateTax(self, A: List[List[int]], income: int) -> float:
        ans = 0
        for i in range(len(A)):
            if not i:
                u, p = A[i][0], A[i][1]
            else:
                u, p = A[i][0] - A[i - 1][0], A[i][1]
            u = min(u, income)
            ans += p * u
            income -= u
            if not income:
                break
        return ans / 100

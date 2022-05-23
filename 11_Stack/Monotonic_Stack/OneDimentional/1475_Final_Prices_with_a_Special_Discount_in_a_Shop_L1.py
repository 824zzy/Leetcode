""" https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
find next smaller or equal element by monotonic increasing stack
the same as 739
"""
class Solution:
    def finalPrices(self, A: List[int]) -> List[int]:
        stk = []
        ans = A
        for i in range(len(A)):
            while stk and A[stk[-1]]>=A[i]:
                ii = stk.pop()
                ans[ii] = A[ii]-A[i]
            stk.append(i)
        return ans
""" https://leetcode.com/problems/watering-plants-ii/
need to practice this type of problem
"""
class Solution:
    def minimumRefill(self, P: List[int], A: int, B: int) -> int:
        ans = 0
        l, r = 0, len(P)-1
        cA, cB = A, B
        while l<=r:
            if l<r:
                if cA<P[l]: ans, cA = ans+1, A
                cA -= P[l]
                if cB<P[r]: ans, cB = ans+1, B
                cB -= P[r]
            elif cB<=cA<P[l] or cA<cB<P[r]: ans += 1
            l += 1
            r -= 1
        return ans
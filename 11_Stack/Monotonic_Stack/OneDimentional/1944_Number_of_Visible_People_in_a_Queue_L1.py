""" https://leetcode.com/problems/number-of-visible-people-in-a-queue/
go from right to left!
"""
class Solution:
    def canSeePersonsCount(self, A: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(A)
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]<A[i]:
                ans[i] += 1
                stk.pop()
            if stk: ans[i] += 1
            stk.append(i)
        return ans
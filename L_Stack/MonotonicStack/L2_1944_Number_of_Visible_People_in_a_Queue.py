""" https://leetcode.com/problems/number-of-visible-people-in-a-queue/
scan from right to left, find next greater element on the left by monotonic decreasing stack
"""


class Solution:
    def canSeePersonsCount(self, A: List[int]) -> List[int]:
        ans = [0] * len(A)
        stk = []  # dec
        for i in reversed(range(len(A))):
            cnt = 0
            while stk and A[stk[-1]] < A[i]:
                stk.pop()
                cnt += 1
            if stk:
                cnt += 1
            ans[i] = cnt
            stk.append(i)
        return ans

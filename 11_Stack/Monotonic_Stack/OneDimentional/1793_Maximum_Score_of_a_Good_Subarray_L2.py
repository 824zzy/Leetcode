""" https://leetcode.com/problems/maximum-score-of-a-good-subarray/
Similiar to 84, the only twist is use k to limit the left side and right side of rectangle
"""
class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        A += [0]
        stk, ans = [], 0
        for i in range(len(A)):
            while stk and A[stk[-1]]>=A[i]:
                H = A[stk.pop()]
                if not stk: W = i
                elif stk[-1]>=k: W = 0
                else: W = i-stk[-1]-1
                ans = max(ans, H*W)
            stk.append(i)
        return ans
""" https://leetcode.com/problems/largest-rectangle-in-histogram/
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/679784/Python3-mono-stack

Use a stack to store non-decreasing height. At position i, we pop from stack all heights (by index) that is higher than heights[i].

Height is obtained from the poped index.
Width is obtained by index i and last value on stack.
"""
class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        A += [0]
        stk, ans = [], 0
        for i in range(len(A)):
            while stk and A[stk[-1]]>=A[i]:
                H = A[stk.pop()]
                W = i if not stk else i-stk[-1]-1
                ans = max(ans, H*W)
            stk.append(i)
        return ans
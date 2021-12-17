""" https://leetcode.com/problems/largest-rectangle-in-histogram/
https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/679784/Python3-mono-stack

Use a stack to store non-decreasing height. At position i, we pop from stack all heights (by index) that is higher than heights[i].

Height is obtained from the poped index.
Width is obtained by index i and last value on stack.
"""
class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        s, ans = [], 0
        for i, h in enumerate(A+[0]):
            while s and h<=A[s[-1]]:
                H = A[s.pop()]
                W = i if not s else i-s[-1]-1
                ans = max(ans, H*W)
            s.append(i)
        return ans
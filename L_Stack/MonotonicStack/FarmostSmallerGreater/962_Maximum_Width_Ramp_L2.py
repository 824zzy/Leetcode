""" https://leetcode.com/problems/maximum-width-ramp/
1. create a decreasing stack
2. from right to left, while any elements larger than stack top, then pop it from the end to update answer.

Time complexity: O(n)
"""
class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = 0
        stk = []
        for i in range(len(A)): 
            if not stk or A[stk[-1]]>A[i]: stk.append(i)
        
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]<=A[i]:
                ans = max(ans, i-stk.pop())
        return ans
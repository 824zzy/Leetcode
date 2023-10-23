""" https://leetcode.com/problems/largest-rectangle-in-histogram/
Inspiration: translate the problem into finding the maximum value of "subarray minimum * subarray length"

Thus, we can
1. use monotonic increasing stack to find next smaller on both the left and right
2. let's consider A[i] as minimum, the largest rectangle should be in the range [prev_small+1, next_small-1]

"""
class Solution:
    def largestRectangleArea(self, A: List[int]) -> int:
        # next smaller on the right
        R = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>A[i]:
                R[stk.pop()] = i
            stk.append(i)
        
        # next smaller on the left
        L = [-1]*len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]>=A[i]:
                L[stk.pop()] = i
            stk.append(i)
        
        # for each A[i] as minimum, find the largest rectangle
        ans = 0
        for i, (l, r) in enumerate(zip(L, R)):
            ans = max(ans, A[i] * (r-l-1))
        return ans


# below is the popular one pass solution in Discussion, but it is not very lucid to me
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
""" https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/
Translate the problem into: given a histogram, find any rectangle whose area is greater than a threshold

easy understanding three pass solution: 
    assuming A[i] is the height of the rectangle, find the left and right boundary(next smaller elements) of the rectangle.

optimal one pass solution:
    assuming stack top is the height of the rectangle, find the left(stack pop's top) and right boundary(A[i]) of the rectangle.
"""
# easy understanding three pass solution
class Solution:
    def validSubarraySize(self, A: List[int], t: int) -> int:
        # next small on the right
        R = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>=A[i]:
                R[stk.pop()] = i
            stk.append(i)
        
        # next small on the left
        L = [-1]*len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]>=A[i]:
                L[stk.pop()] = i
            stk.append(i)
        
        for i, (l, r) in enumerate(zip(L, R)):
            if l!=-1 and r!=len(A):
                if A[i]>t/(r-l-1): return r-l-1

# optimal one pass solution
class Solution:
    def validSubarraySize(self, A: List[int], threshold: int) -> int:
        A += [0]
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>A[i]:
                h = A[stk.pop()]
                if stk: ii = stk[-1]
                else: ii = -1
                w = i-ii-1
                if h*w>threshold: 
                    return i-ii-1
            stk.append(i)
        return -1
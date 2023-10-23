""" https://leetcode.com/problems/maximum-score-of-a-good-subarray/
Similar to 84, the only twist is use k to limit the left side and right side of rectangle
"""
from header import *

class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
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
            if l<k<r:
                ans = max(ans, A[i] * (r-l-1))
        return ans
    

""" https://leetcode.com/problems/maximum-score-of-a-good-subarray/
greedily find maximum score by two pointers
"""
from header import *
class Solution:
    def maximumScore(self, A: List[int], k: int) -> int:
        ans = w = A[k]
        l = r = k
        while 0<=l-1 or r+1<len(A):
            if l==0 or r+1<len(A) and A[l-1]<A[r+1]:
                r += 1
                w = min(w, A[r])
            else:
                l -= 1
                w = min(w, A[l])
            ans = max(ans, w*(r-l+1))
        return ans
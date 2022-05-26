""" https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
use two pass monotonic stack to find:
1. left most index that ascending order is broken
2. right most index that descending order is broken

Time: O(n)
"""
class Solution:
    def findUnsortedSubarray(self, A: List[int]) -> int:
        l = inf
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>A[i]:
                l = min(l, stk.pop())
            stk.append(i)
        
        r = -inf
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]<A[i]:
                r = max(r, stk.pop())
            stk.append(i)
            
        if l!=inf and r!=-inf: return r-l+1
        else: return 0
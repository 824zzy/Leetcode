""" https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
1. maintain max and min queues and left most legit index
2. pop elements when absolute difference larger than limit, while update left most index
"""
from header import *

class Solution:
    def longestSubarray(self, A: List[int], limit: int) -> int:
        mx_q = deque() # monotonic decrease
        mn_q = deque() # monotonic increase
        i = 0
        ans = 0
        for j, x in enumerate(A):
            # in
            while mn_q and A[mn_q[-1]]>x:
                mn_q.pop()
            while mx_q and A[mx_q[-1]]<x:
                mx_q.pop()
            mx_q.append(j)
            mn_q.append(j)
            # out
            if A[mx_q[0]]-A[mn_q[0]]>limit:
                if i==mn_q[0]:
                    mn_q.popleft()
                if i==mx_q[0]:
                    mx_q.popleft()
                i += 1
            ans = max(ans, j-i+1)
        return ans
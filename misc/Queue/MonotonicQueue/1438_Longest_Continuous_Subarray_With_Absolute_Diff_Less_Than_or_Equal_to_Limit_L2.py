""" https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
1. maintain max and min queues and left most legit index
2. pop elements when absolute difference larger than limit, while update left most index
"""
class Solution:
    def longestSubarray(self, A: List[int], L: int) -> int:
        min_dq = deque()
        max_dq = deque()
        ans = 0
        i = 0
        for j, x in enumerate(A):
            while min_dq and min_dq[-1]>x: min_dq.pop()
            while max_dq and max_dq[-1]<x: max_dq.pop()
            min_dq.append(x)
            max_dq.append(x)
            
            if max_dq[0]-min_dq[0]>L:
                if A[i]==min_dq[0]: min_dq.popleft()
                if A[i]==max_dq[0]: max_dq.popleft()
                i += 1
            ans = max(ans, j-i+1)
        return ans
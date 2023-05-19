""" https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
1. maintain max and min priority queues and left most legit index
2. pop elements when absolute difference larger than limit, while update left most index
"""
class Solution:
    def longestSubarray(self, A: List[int], L: int) -> int:
        min_pq = []
        max_pq = []
        ans = 0
        left = 0
        for i, x in enumerate(A):
            heappush(min_pq, (x, i))
            heappush(max_pq, (-x, i))
            while min_pq and max_pq and abs(min_pq[0][0]+max_pq[0][0])>L:
                if min_pq[0][1]<max_pq[0][1]: 
                    _, ii = heappop(min_pq)
                    left = max(left, ii+1)
                else: 
                    _, ii = heappop(max_pq)
                    left = max(left, ii+1)
            ans = max(ans, i-left+1)
        return ans
""" https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
1. keep a seen set which window of size k and prefix sum
2. once find duplicate, then reset prefix sum and  and seen set
"""
from header import *


class Solution:
    def maximumSubarraySum(self, A: List[int], k: int) -> int:
        seen = set()
        sm = 0
        ans = 0
        for i in range(len(A)):
            if A[i] not in seen:
                sm += A[i]
                seen.add(A[i])
                if len(seen) == k:
                    ans = max(ans, sm)
                    sm -= A[i - k + 1]
                    seen.remove(A[i - k + 1])
            else:
                sm = A[i]
                seen = {A[i]}
        return ans


""" 15 0 24 12
[1,5,4,2,9,9,9]
3
[4,4,4]
3
[1,1,1,7,8,9]
3
[9,9,9,1,2,3]
3
"""

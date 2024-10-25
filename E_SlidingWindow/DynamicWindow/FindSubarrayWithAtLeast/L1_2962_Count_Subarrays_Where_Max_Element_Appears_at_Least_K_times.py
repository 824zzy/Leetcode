""" https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/
convert the problem into: find the subarrays where the maximum element of nums appears less than k times
"""
from header import *


class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        mx = max(A)
        n = len(A)
        i = 0
        cnt = 0
        ans = 0

        for j in range(len(A)):
            cnt += A[j] == mx
            while cnt == k:
                cnt -= A[i] == mx
                i += 1
            ans += j - i + 1
        return n * (n + 1) // 2 - ans


"""
[1,3,2,3,3]
2
[1,4,2,1]
3
"""

""" https://leetcode.com/problems/continuous-subarrays/
sliding window + Counter

find the number of subarray with **at most 2** distinct elements
"""

from header import *


class Solution:
    def continuousSubarrays(self, A: List[int]) -> int:
        i = 0
        ans = 0
        cnt = Counter()
        for j in range(len(A)):
            cnt[A[j]] += 1
            while max(cnt) - min(cnt) > 2:
                cnt[A[i]] -= 1
                if cnt[A[i]] == 0:
                    cnt.pop(A[i])
                i += 1
            ans += j - i + 1
        return ans

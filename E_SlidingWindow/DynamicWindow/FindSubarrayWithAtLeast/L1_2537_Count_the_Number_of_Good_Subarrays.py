""" https://leetcode.com/problems/count-the-number-of-good-subarrays/
find 
"""

from header import *


class Solution:
    def countGood(self, A: List[int], k: int) -> int:
        cnt = Counter()
        sm = 0
        i = 0
        ans = 0
        for j in range(len(A)):
            sm += cnt[A[j]]
            cnt[A[j]] += 1
            while sm >= k:
                cnt[A[i]] -= 1
                sm -= cnt[A[i]]
                i += 1
            ans += i
        return ans

""" https://leetcode.com/problems/count-complete-subarrays-in-an-array/
"""
from header import *


class Solution:
    def countCompleteSubarrays(self, A: List[int]) -> int:
        ans = 0
        t = len(set(A))

        cnt = Counter()
        left = 0
        for x in A:
            cnt[x] += 1
            while len(cnt) == t:
                x = A[left]
                cnt[x] -= 1
                if cnt[x] == 0:
                    del cnt[x]
                left += 1
            ans += left
        return ans


# brute force also works due to small input size


class Solution:
    def countCompleteSubarrays(self, A: List[int]) -> int:
        ans = 0
        t = len(set(A))
        for i in range(len(A)):
            seen = set()
            for j in range(i, len(A)):
                seen.add(A[j])
                if len(seen) == t:
                    ans += 1
        return ans

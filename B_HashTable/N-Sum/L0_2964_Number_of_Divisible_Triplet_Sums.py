""" https://leetcode.com/problems/number-of-divisible-triplet-sums/
3-sum-ish

(nums[i] + nums[j] + nums[k]) % d == 0
==>  (a + b) % d == 0
==>  a % d == -b % d

Time: O(N^2)
"""
from header import *


class Solution:
    def divisibleTripletCount(self, A: List[int], d: int) -> int:
        ans = 0
        for i in range(len(A)):
            seen = Counter()
            for j in range(i + 1, len(A)):
                ans += seen[-A[j] % d]
                seen[(A[i] + A[j]) % d] += 1
        return ans


"""
[3,3,4,7,8]
5
[3,3,3,3]
3
[3,3,3,3]
6
"""

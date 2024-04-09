""" https://leetcode.com/problems/minimum-total-cost-to-make-arrays-unequal/
Observation:
1. Equal i-th elements in both array must be changed, first sum up their index.

Case1:
x = num1[i] = nums2[i]
1: The major element of x less or equal than half:
    1.1: x's count is even ==> pair them
    1.2: x's count is odd ==> at least three types of x, and can swap with nums1[0]
2: The major element of x more than half:
    2.1: ask help from non-x element from low to high index
         find nums1[j] != nums2[j]!= major element, until major element less or equal than half
"""
from header import *


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        ans = swap_cnt = mode_cnt = mode = 0
        cnt = [0] * (len(nums1) + 1)
        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if x == y:
                ans += i
                swap_cnt += 1
                cnt[x] += 1
                if cnt[x] > mode_cnt:
                    mode_cnt, mode = cnt[x], x

        for i, (x, y) in enumerate(zip(nums1, nums2)):
            if mode_cnt * 2 <= swap_cnt:
                break
            if x != y and x != mode and y != mode:
                ans += i
                swap_cnt += 1
        return ans if mode_cnt * 2 <= swap_cnt else -1

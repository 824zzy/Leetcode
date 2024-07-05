""" L0: https://leetcode.com/problems/find-the-middle-index-in-array/
"""


class Solution:
    def findMiddleIndex(self, A: List[int]) -> int:
        pref = list(itertools.accumulate([0] + A + [0]))
        rev_pref = list(itertools.accumulate([0] + A[::-1] + [0]))[::-1]
        for i in range(1, len(pref) - 1):
            if pref[i - 1] == rev_pref[i + 1]:
                return i - 1
        return -1


# find x where 2*prefix=sum-x


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = 0
        for i, x in enumerate(nums):
            if 2 * prefix == total - x:
                return i
            prefix += x
        return -1

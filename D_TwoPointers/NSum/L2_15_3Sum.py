""" https://leetcode.com/problems/3sum/
1. nums[i] + nums[j] + nums[k] == 0  ==> nums[i] + nums[j] == -nums[k]
2. sort the array
3. for each i, use two pointers to find and update j and k

The hardest part is to remove duplicates.
"""
from header import *


class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = []
        n = len(A)
        for i in range(n):
            if i and A[i - 1] == A[i]:
                continue  # remove duplicates
            l, r = i + 1, n - 1
            while l < r:
                if A[i] + A[l] + A[r] > 0:
                    r -= 1
                elif A[i] + A[l] + A[r] < 0:
                    l += 1
                else:
                    ans.append([A[i], A[l], A[r]])
                    l += 1
                    while l < r and A[l - 1] == A[l]:  # remove duplicates
                        l += 1
        return ans

# use tuple to remove duplicates, which is not optimal


class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = set()
        n = len(A)
        for i in range(n):
            l, r = i + 1, n - 1
            while l < r:
                if A[i] + A[l] + A[r] > 0:
                    r -= 1
                elif A[i] + A[l] + A[r] < 0:
                    l += 1
                else:
                    ans.add(tuple([A[i], A[l], A[r]]))
                    l += 1
                    r -= 1
        return ans


"""
non-sort solution using hash table
"""


class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(A)):
            # remove duplicate
            if i and A[i] == A[i - 1]:
                continue
            seen = defaultdict(set)
            for j in range(i + 1, len(A)):
                if seen[-A[j]]:
                    ans.add(tuple(sorted([A[i], A[j], -A[i] - A[j]])))
                seen[A[i] + A[j]].add(A[j])
        return ans

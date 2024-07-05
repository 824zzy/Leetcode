""" https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/
translate the problems into: finding the number of 0's between a 1 and a -1 using two pointers
"""
from header import *

# O(n)


class Solution:
    def captureForts(self, A: List[int]) -> int:
        i = 0
        ans = 0
        for j, x in enumerate(A):
            if x:
                if A[i] and x != A[i]:
                    ans = max(ans, j - i - 1)
                i = j
        return ans


# brute force solution for contest: O(2*n)


class Solution:
    def captureForts(self, A: List[int]) -> int:
        def fn(i):
            l, r = i - 1, i + 1
            ans = 0
            while r < len(A) and A[r] == 0:
                r += 1
            if r != len(A) and A[r] != 1:
                ans = max(ans, r - i - 1)

            while l >= 0 and A[l] == 0:
                l -= 1

            if l != -1 and A[l] != 1:
                ans = max(ans, i - l - 1)
            return ans

        ans = 0
        for i, x in enumerate(A):
            if x == 1:
                ans = max(ans, fn(i))
        return ans

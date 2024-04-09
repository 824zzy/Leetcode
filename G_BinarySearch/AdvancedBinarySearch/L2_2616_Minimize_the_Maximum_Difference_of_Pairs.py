""" https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/
1. mini-max ==> binary search
2. greedily find the pairs:
    - compare the pairs one by one, if the pair is valid, we move to next available pair (A[i + 2], A[i + 1]).
      If not, we move to next available pair (A[i + 1], A[i]).
    - or use bisect_right to find all the available pairs.
"""
from header import *


class Solution:
    def minimizeMax(self, A: List[int], p: int) -> int:
        def fn(x):
            # given the maximum diff x ana a sorted array
            # can we find less than p pairs? ==> greedy
            cnt = 0
            i = 0
            while i < len(A):
                j = bisect_right(A, A[i] + x)
                if j - i <= 1:
                    i += 1
                a, b = divmod(j - i, 2)
                cnt += a
                i = j - b
            return cnt >= p

        def fn(x):
            # given the maximum diff x ana a sorted array
            # can we find less than p pairs? ==> greedy
            cnt = 0
            i = 0
            while i < len(A) - 1:
                if A[i + 1] - A[i] <= x:
                    cnt += 1
                    i += 1
                i += 1
            return cnt >= p

        A.sort()
        l, r = 0, A[-1] - A[0] + 1
        while l < r:
            m = (l + r) // 2
            if fn(m):
                r = m
            else:
                l = m + 1
        return l


"""
[10,1,2,7,1,3]
2
[4,2,1,2]
1
[4,0,2,1,2,5,5,3]
3
[0,5,3,4]
0
[5,6,0,5,4,0,0]
1
[1,1,0,3]
2
"""

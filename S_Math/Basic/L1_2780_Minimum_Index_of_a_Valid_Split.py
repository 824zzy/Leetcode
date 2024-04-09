""" https://leetcode.com/problems/minimum-index-of-a-valid-split/
solution1: two pass
solution2: conclude that the dominant of two subarray is the same as the original array
"""
from header import *


class Solution:
    def minimumIndex(self, A: List[int]) -> int:
        cnt = Counter([A[0]])
        dom = A[0]
        pre = [None, A[0]]
        for i in range(1, len(A)):
            cnt[A[i]] += 1
            if cnt[A[i]] > cnt[dom]:
                dom = A[i]
            if cnt[dom] * 2 > (i + 1):
                pre.append(dom)
            else:
                pre.append(None)

        cnt = Counter([A[-1]])
        dom = A[-1]
        suf = [None, A[-1]]
        for i in range(1, len(A)):
            cnt[A[~i]] += 1
            if cnt[A[~i]] > cnt[dom]:
                dom = A[~i]
            if cnt[dom] * 2 > (i + 1):
                suf.append(dom)
            else:
                suf.append(None)
        suf = suf[::-1]

        for i, (x, y) in enumerate(zip(pre, suf)):
            if x == y and x is not None and y is not None:
                return i - 1
        return -1


class Solution:
    def minimumIndex(self, A: List[int]) -> int:
        dom, freq = Counter(A).most_common(1)[0]
        cnt = 0
        for i, x in enumerate(A):
            if x == dom:
                cnt += 1
            if 2 * cnt > i + 1 and 2 * (freq - cnt) > len(A) - i - 1:
                return i
        return -1


"""
[1,2,2,2]
[2,1,3,1,1,1,7,1,2,1]
[3,3,3,3,7,2,2]
[2,2]
"""

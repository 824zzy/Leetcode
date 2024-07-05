""" https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/
merge sort
"""
from header import *


class Solution:
    def mergeArrays(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        m, n = len(A), len(B)
        while True:
            if i == m:
                ans.extend(B[j:])
                break
            if j == n:
                ans.extend(A[i:])
                break
            if A[i][0] < B[j][0]:
                ans.append(A[i])
                i += 1
            elif A[i][0] > B[j][0]:
                ans.append(B[j])
                j += 1
            else:
                A[i][1] += B[j][1]
                ans.append(A[i])
                i += 1
                j += 1
        return ans


class Solution:
    def mergeArrays(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        mp = defaultdict(int)
        for k, v in A:
            mp[k] = v
        for k, v in B:
            mp[k] += v
        return sorted(mp.items(), key=lambda x: x[0])

""" https://leetcode.com/problems/diagonal-traverse-ii/
use hashmap to store the diagonal elements, where key is the sum of indices
"""
from header import *


class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for i in reversed(range(len(A))):
            for j in range(len(A[i])):
                mp[i + j].append(A[i][j])
        mp = sorted(mp.items(), key=lambda x: x[0])
        ans = []
        for i in range(len(mp)):
            ans.extend(mp[i][1])
        return ans


class Solution:
    def findDiagonalOrder(self, A: List[List[int]]) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(A)):
            for j in range(len(A[i])):
                mp[(i + j, j, i)] = A[i][j]
        return [y for x, y in sorted(mp.items(), key=lambda x: x[0])]


"""
(1, 0), (0, 1)
(2, 0), (1, 1), (0, 2)
"""

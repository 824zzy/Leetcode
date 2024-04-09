""" https://leetcode.com/problems/find-a-good-subset-of-the-matrix/
# case 1: when k = 1, the seleted row must be all 0
# case 2: when k = 2, the selected rows X & Y == 0
"""


class Solution:
    def goodSubsetofBinaryMatrix(self, A: List[List[int]]) -> List[int]:
        mp = {}
        for i, row in enumerate(A):
            m = 0
            for j, x in enumerate(row):
                m |= x << j
            mp[m] = i
        # case 1
        if 0 in mp:
            return [mp[0]]
        # case 2
        for x, i in mp.items():
            for y, j in mp.items():
                if (x & y) == 0:
                    return sorted((i, j))
        return []

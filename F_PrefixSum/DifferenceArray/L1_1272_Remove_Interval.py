""" https://leetcode.com/problems/remove-interval/
categorization: greedily find valid intervals under three cases

time complexity: O(n)
"""
from header import *


class Solution:
    def removeInterval(self, A: List[List[int]], t: List[int]) -> List[List[int]]:
        ans = []
        L, R = t
        for l, r in A:
            """
            [ ]
                [  ]
            or
                 [  ]
            [  ]
            """
            if r <= L or l >= R:
                ans.append((l, r))
            """
            [  ]
              [  ]
            """
            if l < L < r:
                ans.append([l, L])
            """
              [   ]
            [   ]
            """
            if l <= R < r:
                ans.append([R, r])
        return ans


""" https://leetcode.com/problems/remove-interval/
sweep line template

time complexity: O(nlogn)
"""


class Solution:
    def removeInterval(self, A: List[List[int]], removed: List[int]) -> List[List[int]]:
        SL = []
        for i, j in A:
            SL.append([i, 1])
            SL.append([j, -1])
        SL.append([removed[0], -1])
        SL.append([removed[1], 1])
        SL.sort()

        ans = []
        cnt = 0
        l = inf
        for i, x in SL:
            cnt += x
            if cnt == 1:
                l = i
            elif cnt == 0 and l != inf:
                ans.append([l, i])
                l = inf
        return ans


"""
[1,1,0,1,0,1,1]
[1,0,-1,0,-1,0,1,0]
"""

""" https://leetcode.com/problems/number-of-spaces-cleaning-robot-cleaned/
matrix simulation
"""
from header import *


class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        x, y = 0, 0
        m, n = len(room), len(room[0])
        D = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i = 0
        dx, dy = D[i]
        ans = 0
        step = 1
        seen = {(0, 0)}
        seen_d = {(0, 0, i)}
        while 1:
            while 0 <= x + dx < m and 0 <= y + dy < n and room[x + dx][y + dy] != 1:
                x += dx
                y += dy
                if (x, y) not in seen:
                    step += 1
                    seen.add((x, y))
            i = (i + 1) % 4
            if (x, y, i) not in seen_d:
                seen_d.add((x, y, i))
            else:
                return ans + step
            dx, dy = D[i]
            ans += step
            step = 0


"""
[[0,0,0],[1,1,0],[0,0,0]]
[[0,1,0],[1,0,0],[0,0,0]]
[[0,0,0],[0,0,0],[0,0,0]]
[[0],[0],[0],[0],[1],[0],[0],[0]]
[[0,0,0,1],[0,1,0,1],[1,0,0,0]]
"""
"""
[[0,1,0],
 [1,0,0],
 [0,0,0]]
[[0,0,0,1],
 [0,1,0,1],
 [1,0,0,0]
]
"""

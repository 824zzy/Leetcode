""" https://leetcode.com/problems/candy-crush/
simulation on matrix:
1. check if there is any 3+ consecutive same number
2. eliminate them
"""
from header import *


class Solution:
    def candyCrush(self, B: List[List[int]]) -> List[List[int]]:
        def check(B):
            ans = set()
            for i in range(len(B)):
                for j in range(len(B[0])):
                    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                        x, y = i, j
                        tmp = {(i, j)}
                        while 0 <= x + dx < len(B) and 0 <= y + dy < len(
                                B[0]) and B[x][y] == B[x + dx][y + dy] and B[x][y] != 0:
                            tmp.add((x + dx, y + dy))
                            x += dx
                            y += dy
                        if len(tmp) >= 3:
                            ans |= tmp
            return ans

        def eliminate(B, candies):
            cols = list([list(x) for x in zip(*B)])
            for i in range(len(cols)):
                tmp = []
                for j in range(len(cols[0])):
                    if (j, i) not in candies:
                        tmp.append(cols[i][j])
                cols[i] = [0] * (len(B) - len(tmp)) + tmp
            return list([list(x) for x in zip(*cols)])

        while candies := check(B):
            B = eliminate(B, candies)
        return B

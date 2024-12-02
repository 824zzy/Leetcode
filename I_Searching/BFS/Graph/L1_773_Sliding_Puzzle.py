""" https://leetcode.com/problems/sliding-puzzle/
simulate the game by bfs
"""

from header import *


class Solution:
    def slidingPuzzle(self, A: List[List[int]]) -> int:
        s = "".join("".join(map(str, a)) for a in A)
        seen = {s}
        for i in range(len(s)):
            if s[i] == "0":
                loc = i
        Q = [(loc, s)]
        ans = 0
        while Q:
            nxtQ = []
            for l, s in Q:
                if s == "123450":
                    return ans
                x, y = l // 3, l % 3
                for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                    if 0 <= x + dx < 2 and 0 <= y + dy < 3:
                        ss = list(s)
                        ll = (x + dx) * 3 + (y + dy)
                        ss[l], ss[ll] = ss[ll], ss[l]
                        ss = "".join(map(str, ss))
                        if ss not in seen:
                            nxtQ.append((ll, ss))
                            seen.add(ss)
            ans += 1
            Q = nxtQ
        return -1

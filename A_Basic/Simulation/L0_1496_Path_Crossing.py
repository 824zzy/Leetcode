""" https://leetcode.com/problems/path-crossing/
simulation the path crossing process
"""


class Solution:
    def isPathCrossing(self, A: str) -> bool:
        x, y = 0, 0
        seen = {(0, 0)}
        for c in A:
            if c == "N":
                y += 1
            if c == "E":
                x += 1
            if c == "W":
                x -= 1
            if c == "S":
                y -= 1
            if (x, y) in seen:
                return True
            seen.add((x, y))
        return False

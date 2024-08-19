""" https://leetcode.com/problems/snake-in-matrix/
simulation
"""

from header import *


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        x, y = 0, 0
        for c in commands:
            if c == "UP":
                x -= 1
            elif c == "DOWN":
                x += 1
            elif c == "LEFT":
                y -= 1
            elif c == "RIGHT":
                y += 1
        return x * n + y

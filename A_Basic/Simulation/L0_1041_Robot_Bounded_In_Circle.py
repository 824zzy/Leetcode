""" https://leetcode.com/problems/robot-bounded-in-circle/
if the particle returns to origin or eventually it changes direction (any direction as long as not north) it can return to origin by repeatedly following the instructions.
"""


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == "L":
                dx, dy = -dy, dx
            if i == "R":
                dx, dy = dy, -dx
            if i == "G":
                x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)

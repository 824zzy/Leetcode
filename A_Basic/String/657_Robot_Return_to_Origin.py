""" Amazon
Basic simulation
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coor = [0, 0]
        for m in moves:
            if m == 'U':
                coor[0] += 1
            if m == 'D':
                coor[0] -= 1
            if m == 'L':
                coor[1] += 1
            if m == 'R':
                coor[1] -= 1
        if coor == [0, 0]:
            return True
        else:
            return False

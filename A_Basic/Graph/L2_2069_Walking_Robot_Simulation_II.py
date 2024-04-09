""" https://leetcode.com/problems/walking-robot-simulation-ii/
simulation in graph

for saving time complexity:
num %= self.perimeter
if num == 0 and self.pos == [0, 0] and self.dir == [1, 0]: self.dir = [0, -1]
"""


class Robot:

    def __init__(self, width: int, height: int):
        self.D = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.d = 0
        self.DIR = {0: 'East',
                    1: 'North',
                    2: 'West',
                    3: 'South'}
        self.pos = [0, 0]
        self.w, self.h = width, height

    def step(self, num: int) -> None:
        num %= 2 * (self.w + self.h) - 4
        if num == 0 and self.pos == [0, 0] and self.d == 0:
            self.d = 3
        while num:
            x, y = self.pos[0], self.pos[1]
            dx, dy = self.D[self.d]
            if self.d == 0:
                most = self.w - x - 1
            elif self.d == 1:
                most = self.h - y - 1
            elif self.d == 2:
                most = x
            else:
                most = y

            step = min(num, most)
            self.pos = [x + dx * step, y + dy * step]
            if num > most:
                self.d = (self.d + 1) % 4
            num -= step

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.DIR[self.d]

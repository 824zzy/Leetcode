""" https://leetcode.com/problems/generate-random-point-in-a-circle/submissions/
1. rejection sampling: check sample's radius until find one in the circle
2. sample rho and theta in polar coodinates. Note that sample rho=r*sqrt(uniform(x))
"""
# rejection sampling


class Solution:
    def __init__(self, r: float, x: float, y: float):
        self.x = x
        self.y = y
        self.r = r

    def randPoint(self) -> List[float]:
        while True:
            xx = self.x + self.r * random.uniform(-1, 1)
            yy = self.y + self.r * random.uniform(-1, 1)
            if (xx - self.x) ** 2 + (yy - self.y) ** 2 < self.r ** 2:
                return [xx, yy]


# polar coordinates solution


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        rho = self.r * sqrt(random.random())
        theta = 2 * pi * random.random()
        return [self.x + rho * cos(theta), self.y + rho * sin(theta)]

"""
sample rho and theta in polar coodinates. Note that sample rho=r*sqrt(uniform(x))
"""
class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.r = radius 
        self.x = x_center
        self.y = y_center

    def randPoint(self) -> List[float]:
        rho = self.r*sqrt(random.random())
        theta = 2*pi*random.random()
        return [self.x+rho*cos(theta), self.y+rho*sin(theta)]
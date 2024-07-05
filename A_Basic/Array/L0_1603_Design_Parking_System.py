""" https://leetcode.com/problems/design-parking-system/
easy simulation
"""


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.PS = {1: big, 2: medium, 3: small}

    def addCar(self, t: int) -> bool:
        self.PS[t] -= 1
        return self.PS[t] >= 0

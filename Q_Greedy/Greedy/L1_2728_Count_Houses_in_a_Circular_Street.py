""" https://leetcode.com/problems/count-houses-in-a-circular-street/
close all doors then open every door until find a opened door
"""
from header import *


class Solution:
    def houseCount(self, S, k: int) -> int:
        for i in range(k):
            S.closeDoor()
            S.moveRight()
        for i in range(k + 1):
            if S.isDoorOpen():
                return i
            S.openDoor()
            S.moveRight()

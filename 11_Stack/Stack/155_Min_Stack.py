""" L1: https://leetcode.com/problems/min-stack/
maintain min stack at the same time to save time
"""
class MinStack:
    def __init__(self):
        self.S = []
        self.M = []
        
    def push(self, val: int) -> None:
        if self.M: self.M.append(min(val, self.M[-1]))
        else: self.M.append(val)
        self.S.append(val)

    def pop(self) -> None:
        self.S.pop()
        self.M.pop()

    def top(self) -> int:
        return self.S[-1]

    def getMin(self) -> int:
        return self.M[-1]
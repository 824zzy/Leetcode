""" https://leetcode.com/problems/moving-average-from-data-stream/
sliding window simulation using queue
"""
from header import *

class MovingAverage:
    def __init__(self, size: int):
        self.sm = 0
        self.sw = deque()
        self.size = size

    def next(self, val: int) -> float:
        self.sw.append(val)
        if len(self.sw)>self.size:
            self.sm -= self.sw.popleft()
        self.sm += val
        return self.sm/len(self.sw)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
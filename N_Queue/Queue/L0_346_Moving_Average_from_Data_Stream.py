""" https://leetcode.com/problems/moving-average-from-data-stream/
sliding window simulation using queue
"""
class MovingAverage:
    def __init__(self, size: int):
        self.sm = 0
        self.W = []
        self.size = size

    def next(self, val: int) -> float:
        self.W.append(val)
        if len(self.W)>self.size:
            self.sm -= self.W.pop(0)
        self.sm += val
        return self.sm/(len(self.W))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
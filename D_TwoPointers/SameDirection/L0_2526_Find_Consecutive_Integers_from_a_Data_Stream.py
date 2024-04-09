""" https://leetcode.com/problems/find-consecutive-integers-from-a-data-stream/
"""


class DataStream:
    def __init__(self, v: int, k: int):
        self.v = v
        self.k = k
        self.cnt = 0

    def consec(self, n: int) -> bool:
        if n == self.v:
            self.cnt += 1
            if self.cnt >= self.k:
                return True
        else:
            self.cnt = 0
            return False


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)

""" https://leetcode.com/problems/maximum-frequency-stack/
Heap solution
maintain a maximum heap by (frequency, index, value)
"""


class FreqStack:

    def __init__(self):
        self.mfs = []
        self.freq = Counter()
        self.idx = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        heapq.heappush(self.mfs, (-self.freq[val], -self.idx, val))
        self.idx += 1

    def pop(self) -> int:
        f, i, v = heapq.heappop(self.mfs)
        self.freq[v] -= 1
        if self.freq[v] == 0:
            del self.freq[v]
        return v

""" L2
build a stack using defaultdict(list) to save frequency as key and val list as values. 
"""
from collections import defaultdict
class FreqStack:
    def __init__(self):
        self.freq = {}
        self.stacks = defaultdict(list)
        self.max_freq = 0

    def push(self, x):
        f = self.freq.get(x, 0)
        if f == 0:
            self.freq[x] = 1
        else:
            self.freq[x] += 1
        self.max_freq = max(self.max_freq, self.freq[x])
        self.stacks[self.freq[x]].append(x)

    def pop(self):
        item = self.stacks.get(self.max_freq)
        last = item.pop()
        self.freq[last] -= 1
        if len(item) == 0:
            self.max_freq = self.max_freq - 1
        return last
""" https://leetcode.com/problems/frequency-tracker/
use two counters to simulate
"""
from header import *


class FrequencyTracker:
    def __init__(self):
        self.mp = Counter()
        self.freq = Counter()

    def add(self, x: int) -> None:
        self.freq[self.mp[x]] -= 1
        self.mp[x] += 1
        self.freq[self.mp[x]] += 1

    def deleteOne(self, x: int) -> None:
        if self.mp[x] == 0:
            return
        self.freq[self.mp[x]] = self.freq[self.mp[x]] - 1
        self.mp[x] = self.mp[x] - 1
        self.freq[self.mp[x]] += 1

    def hasFrequency(self, f: int) -> bool:
        return self.freq[f] > 0

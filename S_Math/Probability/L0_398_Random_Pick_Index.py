""" https://leetcode.com/problems/random-pick-index/
"""
from header import *

class Solution:
    def __init__(self, nums: List[int]):
        self.d = defaultdict(list)
        for i, n in enumerate(nums):
            self.d[n].append(i)

    def pick(self, target: int) -> int:
        cnt, ans = 0, 0
        for i in range(len(self.d[target])):
            cnt += 1
            p = random.random()
            if p < 1/cnt:
                ans = self.d[target][i]
        return ans

# or cheating
class Solution:
    def __init__(self, A: List[int]):
        self.mp = defaultdict(list)
        for i, x in enumerate(A): self.mp[x].append(i)

    def pick(self, t: int) -> int:
        x = self.mp[t]
        return x[randint(0, len(x)-1)]
""" https://leetcode.com/problems/design-an-ordered-stream/
use a pointer to controll which part of mp to print out
"""
class OrderedStream:
    def __init__(self, n: int):
        self.mp = defaultdict()
        self.p = 1

    def insert(self, k: int, v: str) -> List[str]:
        self.mp[k] = v
        ans = []
        while self.p in self.mp:
            ans.append(self.mp[self.p])
            self.p += 1
        return ans

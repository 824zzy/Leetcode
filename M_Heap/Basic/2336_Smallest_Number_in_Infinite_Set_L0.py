""" https://leetcode.com/problems/smallest-number-in-infinite-set/
it is actually an easy problem due to 1<=num<=1000
"""
class SmallestInfiniteSet:
    def __init__(self):
        self.A = list(range(1, 1001))
        heapify(self.A)

    def popSmallest(self) -> int:
        return heappop(self.A)

    def addBack(self, num: int) -> None:
        if num not in self.A:
            heappush(self.A, num)
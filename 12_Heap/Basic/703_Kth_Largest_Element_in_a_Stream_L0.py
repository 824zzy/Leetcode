""" https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
class KthLargest:

    def __init__(self, k: int, A: List[int]):
        self.A = A
        heapq.heapify(self.A)
        self.k = k

    def add(self, v: int) -> int:
        heapq.heappush(self.A, v)
        return heapq.nlargest(self.k, self.A)[-1]
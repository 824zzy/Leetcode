""" https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
class KthLargest:
    def __init__(self, k: int, A: List[int]):
        self.A = sorted(A)
        self.k = k

    def add(self, v: int) -> int:
        bisect.insort(self.A, v)
        return self.A[-self.k]
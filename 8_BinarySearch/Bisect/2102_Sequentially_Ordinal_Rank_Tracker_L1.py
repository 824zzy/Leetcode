""" https://leetcode.com/problems/sequentially-ordinal-rank-tracker/
use binary search to insert location and k to find kth location
"""
class SORTracker:
    def __init__(self):
        self.A = []
        self.k = 0

    def add(self, name: str, score: int) -> None:
        bisect.insort(self.A, (-score, name))

    def get(self) -> str:
        self.k += 1
        return self.A[self.k-1][1]
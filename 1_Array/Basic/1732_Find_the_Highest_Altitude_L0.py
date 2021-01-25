# easy: prefix sum array
class Solution:
    def largestAltitude(self, A: List[int]) -> int:
        prefix = 0
        h = [0]
        for a in A:
            prefix += a
            h.append(prefix)
        return max(h)
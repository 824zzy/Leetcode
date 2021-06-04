""" L0
sort and find maximum gaps
"""
class Solution:
    def maxArea(self, h: int, w: int, H: List[int], W: List[int]) -> int:
        H = [0] + sorted(H) + [h]
        W = [0] + sorted(W) + [w]
        maxH = max([H[i]-H[i-1] for i in range(1, len(H))])
        maxW = max([W[i]-W[i-1] for i in range(1, len(W))])
        return maxH*maxW%(10**9+7)
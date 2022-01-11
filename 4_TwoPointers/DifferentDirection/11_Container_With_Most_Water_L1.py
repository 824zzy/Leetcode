""" key idea:
say height[L] < height[R]
area of (L, L+1), (L, L+2), ...,(L, R-1) will be smaller than (L, R).

otherwise height[L] > height[R]
area of (L, L+1), (L, L+2), ...,(L, R-1) will be bigger than (L, R).
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        L, R, res = 0, len(height)-1, 0
        while L < R:
            area = min(height[L], height[R])*(R-L)
            res = max(res, area)
            if height[L] < height[R]: L += 1
            else: R -= 1
        return res
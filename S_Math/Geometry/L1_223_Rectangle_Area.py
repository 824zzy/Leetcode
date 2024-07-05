""" https://leetcode.com/problems/rectangle-area/description/
1. The union area of two rectangles is: A+B-Intersection.
2. The endpoints of the intersection are mini-max of the two rectangles.
"""


class Solution:
    def computeArea(
        self,
        ax1: int,
        ay1: int,
        ax2: int,
        ay2: int,
        bx1: int,
        by1: int,
        bx2: int,
        by2: int,
    ) -> int:
        A = (ax2 - ax1) * (ay2 - ay1)
        B = (bx2 - bx1) * (by2 - by1)
        cy2 = min(ay2, by2)
        cx2 = min(ax2, bx2)
        cy1 = min(cy2, max(ay1, by1))
        cx1 = min(cx2, max(ax1, bx1))
        C = (cx2 - cx1) * (cy2 - cy1)
        return A + B - C

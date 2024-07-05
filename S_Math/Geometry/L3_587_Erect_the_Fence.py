""" https://leetcode.com/problems/erect-the-fence/
Monotone chain convex hull algorithm, time complexity: O(nlogn)
1. sort the points with respect to x-coordinates
2. calculate the upper and lower hulls in O(n) time
3.

https://commons.wikimedia.org/wiki/File:Animation_depicting_the_Monotone_algorithm.gif
"""
from header import *


class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        points = sorted(map(tuple, points), key=lambda x: (x[0], x[1]))

        def sign(o, a, b):
            """
            Cross product of two vectors OA and OB
            returns positive for counter clockwise
            turn and negative for clockwise turn
            """
            return (a[0] - o[0]) * (b[1] - o[1]) - (b[0] - o[0]) * (a[1] - o[1])

        def build(points):
            hull = []
            for p in points:
                while len(hull) >= 2 and sign(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull.append(p)
            return hull

        return list(set(build(points) + build(points[::-1])))

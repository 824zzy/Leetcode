""" https://leetcode.com/problems/reaching-points/
(x, x + y) or (x + y, y) ==> GCD of x, y
From target to start,
1. try to reduce target to start as much as possible
2. check if target can be reduced to start by three conditions:
    2.1 target == start
    2.2 target == start + k * x
    2.3 target == start + k * y
"""


class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        while sx < tx and sy < ty:
            tx, ty = tx % ty, ty % tx
        if sx == tx and sy == ty:
            return True
        elif sx == tx and sy < ty and (ty - sy) % sx == 0:
            return True
        elif sy == ty and sx < tx and (tx - sx) % sy == 0:
            return True
        else:
            return False

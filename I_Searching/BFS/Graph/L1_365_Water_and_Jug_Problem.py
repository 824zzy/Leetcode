""" https://leetcode.com/problems/water-and-jug-problem/
define 6 operations:
1. fill a
2. fill b
3. if a not full and b has water, b to a
4. if b not full and a has water, a to b
5. empty a
6. empty b
"""


class Solution:
    def canMeasureWater(self, a: int, b: int, t: int) -> bool:
        def op1(x, y, a, b):
            return (a, y)

        def op2(x, y, a, b):
            return (x, b)

        def op5(x, y, a, b):
            return (0, y)

        def op6(x, y, a, b):
            return (x, 0)

        def op3(x, y, a, b):
            return (a + min(a - x, y), b - min(a - x, y))

        def op4(x, y, a, b):
            return (a - min(x, b - y), b + min(x, b - y))

        Q = [(0, 0)]
        seen = set(Q)

        while Q:
            aa, bb = Q.pop(0)
            if aa == t or bb == t or (aa + bb) == t:
                return True
            for op in (op1, op2, op3, op4, op5, op6):
                _aa, _bb = op(aa, bb, a, b)
                if (_aa, _bb) not in seen:
                    seen.add((_aa, _bb))
                    Q.append((_aa, _bb))
        return False

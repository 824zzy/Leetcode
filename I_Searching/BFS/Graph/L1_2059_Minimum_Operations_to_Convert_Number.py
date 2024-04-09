""" https://leetcode.com/problems/minimum-operations-to-convert-number/
use bfs to go through all possible converted numbers
note that we only need to check numbers in [0, 1000]
"""


class Solution:
    def minimumOperations(self, A: List[int], start: int, goal: int) -> int:
        Q = [(start, 0)]
        seen = {start}
        while Q:
            i, step = Q.pop(0)
            if i == goal:
                return step
            if 0 <= i <= 1000:
                for x in A:
                    for op in (add, sub, xor):
                        if op(i, x) not in seen:
                            seen.add(op(i, x))
                            Q.append((op(i, x), step + 1))
        return -1

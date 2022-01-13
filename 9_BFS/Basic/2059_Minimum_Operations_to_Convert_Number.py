""" L1: https://leetcode.com/problems/minimum-operations-to-convert-number/
only check numbers that in [0, 1000]
"""
class Solution:
    def minimumOperations(self, A: List[int], s: int, g: int) -> int:
        seen = set([s])
        ans = 0
        Q = [s]
        while Q:
            for _ in range(len(Q)):
                v = Q.pop(0)
                if v==g: return ans
                if 0<=v<=1000:
                    for x in A:
                        for op in (add, sub, xor):
                            if op(v, x) not in seen:
                                seen.add(op(v, x))
                                Q.append(op(v, x))
            ans += 1
        return -1

""" https://leetcode.com/problems/baseball-game/
use stack for simulation
"""
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stk = []
        for op in ops:
            if op=='C': stk.pop()
            elif op=='D': stk.append(stk[-1]*2)
            elif op=='+': stk.append(stk[-1]+stk[-2])
            else: stk.append(int(op))
        return sum(stk)
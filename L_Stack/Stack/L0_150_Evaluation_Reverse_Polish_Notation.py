""" https://leetcode.com/problems/evaluate-reverse-polish-notation/
execute expressions by eval or operators
Time: O(n)
"""
from header import *


class Solution:
    def evalRPN(self, A: List[str]) -> int:
        # operators.add etc.
        ops = {"+": add, "-": sub, "*": mul, "/": truediv}
        stk = []
        for t in A:
            if t in ops:
                y = int(stk.pop())
                x = int(stk.pop())
                stk.append(ops[t](x, y))
            else:
                stk.append(t)
        return int(stk[0])


class Solution:
    def evalRPN(self, T: List[str]) -> int:
        s = []
        for t in T:
            if t not in "+-*/":
                s.append(t)
            else:
                r = s.pop()
                l = s.pop()
                s.append(str(int(eval(l + t + r))))
        return s[0]

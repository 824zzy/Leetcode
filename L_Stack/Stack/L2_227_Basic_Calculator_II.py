""" https://leetcode.com/problems/basic-calculator-ii/
1. use op and val to store the current operator and value
2. use stack to store the previous value

it is not easy due to the implementation of the stack
"""
from header import *

# another solution from others using only one stack
class Solution:
    def calculate(self, s: str) -> int:
        op, val = "+", 0 #initialized at "+0"
        stack = []
        for i, x in enumerate(s):
            if x.isdigit(): val = 10*val + int(x) #accumulating digits 
                
            if x in "+-*/" or i == len(s) - 1: #
                if   op == "+": stack.append(val)
                elif op == "-": stack.append(-val)
                elif op == "*": stack.append(stack.pop() * val)
                elif op == "/": stack.append(int(stack.pop()/val))
                op, val = x, 0 #reset 
        return sum(stack)
    

# maintain two stacks: operation stack and number stack
class Solution:
    def calculate(self, s: str) -> int:
        def compute(x, y, op):
            if op=='+': return x+y
            if op=='-': return x-y
            if op=='*': return x*y
            if op=='/': return x//y
        
        s += '+'
        n_stk = []
        op_stk = []
        n = ''
        for i, c in enumerate(s):
            if c.isdigit():
                n += c
            if c in '+-*/':
                if op_stk and op_stk[-1] in '*/':
                    y = int(n)
                    op = op_stk.pop()
                    x = n_stk.pop()
                    n_stk.append(compute(x, y, op))
                    op_stk.append(c)
                else:
                    n_stk.append(int(n))
                    if i!=len(s)-1:
                        op_stk.append(c)
                n = ''
            
        ans = n_stk.pop(0)
        while n_stk and op_stk:
            y = n_stk.pop(0)
            op = op_stk.pop(0)
            ans = compute(ans, y, op)
        return ans
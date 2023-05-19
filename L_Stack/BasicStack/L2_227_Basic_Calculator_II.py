""" https://leetcode.com/problems/basic-calculator-ii/
it is not easy due to the implementation of the stack

"""
from header import *

# maintain two stacks: operation stack and number stack
class Solution:
    def calculate(self, s: str) -> int:      
        s = s.replace(' ', '')
        i = 0
        num_stk = []
        op_stk = []
        ops = {'+': add, '-': sub, '*': mul, '/': floordiv}
        while i<len(s):
            if s[i] in '+-*/':
                op_stk.append(s[i])
                i += 1
            else:
                tmp = ''
                while i<len(s) and s[i].isnumeric():
                    tmp += s[i]
                    i += 1
                num_stk.append(tmp)
                while op_stk and op_stk[-1] in '*/':
                    y = num_stk.pop()
                    x = num_stk.pop()
                    num_stk.append(str(ops[op_stk.pop()](int(x), int(y))))
        
        
        op_stk = op_stk[::-1]
        num_stk = num_stk[::-1]
        while op_stk:
            x = num_stk.pop()
            y = num_stk.pop()
            num_stk.append(str(ops[op_stk.pop()](int(x), int(y))))
        return int(num_stk[0])


# solution from others using only one stack
class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        for sp in ['+', '-', '*', '/']:
            s = s.replace(sp, ' '+sp+' ')
        s = s.split(' ')
        s = ['+'] + s
        stk = []
        for i, c in enumerate(s):
            if c=='+':
                stk.append(int(s[i+1]))
            elif c=='-':
                stk.append(-int(s[i+1]))
            elif c=='*':
                n1 = int(stk.pop())
                n2 = int(s[i+1])
                stk.append(n1*n2)
            elif c=='/':
                n1 = int(stk.pop())
                n2 = int(s[i+1])
                stk.append(n1//n2)
        return sum(stk)
    
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
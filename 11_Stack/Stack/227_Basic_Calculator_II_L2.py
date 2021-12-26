""" https://leetcode.com/problems/basic-calculator-ii/
TODO: https://leetcode.com/problems/basic-calculator-ii/discuss/750164/Python3-one-stack-and-two-stack-approach
"""
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
                stk.append(math.trunc(n1/n2))
        return sum(stk)
    
    
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
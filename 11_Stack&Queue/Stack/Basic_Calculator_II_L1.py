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
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        while tokens:
            c = tokens.pop(0)
            if c not in ['+', '-', '*', '/']:
                stack.append(int(c))
            else:
                b, a = stack.pop(), stack.pop()
                if c=='+':
                    stack.append(a+b)
                if c=='-':
                    stack.append(a-b)
                if c=='*':
                    stack.append(a*b)
                if c=='/':
                    stack.append(int(a/b))
        return stack.pop()
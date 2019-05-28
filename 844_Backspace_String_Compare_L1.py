""" Naive stack usage to convert string
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(S):
            stack = []
            for s in S:
                if s != '#':
                    stack.append(s)
                elif stack:
                    stack.pop()
            return stack
        return build(S) == build(T)
        

""" reverse pointer trick
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        s = list(F(S))
        t = list(F(T))
        return s == t
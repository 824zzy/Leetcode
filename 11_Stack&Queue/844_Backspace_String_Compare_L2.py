""" Google
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
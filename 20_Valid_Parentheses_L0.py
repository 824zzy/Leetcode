
""" basic usage of stack: my straightforward method.
"""
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # test stack none
            if not stack:
                stack.append(c)
            elif c == ')' and stack[-1] == '(':
                stack.pop()
            elif c == ']' and stack[-1] == '[':
                stack.pop()
            elif c == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False
        
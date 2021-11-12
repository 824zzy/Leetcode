# Facebook
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
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
        return True if not stk else False

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c not in ")]}": stk.append(c)
            elif stk:
                if c==')' and stk[-1]=='(': stk.pop()
                elif c==']' and stk[-1]=='[': stk.pop()
                elif c=='}' and stk[-1]=='{': stk.pop()
                else: return False
            else: return False
        return True if not stk else False
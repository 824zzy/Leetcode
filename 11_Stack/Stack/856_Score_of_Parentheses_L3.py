# Solution from lee215
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack, cur = [], 0
        for i in S:
            if i == '(':
                stack.append(cur)
                cur = 0
            else:
                cur += stack.pop() + max(cur, 1)
        return cur
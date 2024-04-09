""" https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stk = []
        for c in s:
            if c == ')':
                tmp = []
                while stk and stk[-1] != '(':
                    tmp.extend(stk.pop()[::-1])
                stk.pop()
                stk.append(tmp)
            else:
                stk.append(c)

        ans = []
        for x in stk:
            ans.extend(x)
        return ''.join(ans)


# elegant solution
class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = [""]
        for c in s:
            if c == "(":
                stack.append("")
            elif c == ")":
                val = stack.pop()[::-1]
                stack[-1] += val
            else:
                stack[-1] += c
        return stack.pop()

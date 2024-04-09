""" https://leetcode.com/problems/remove-outermost-parentheses/
count open parentheses
"""


class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans, op, tmp = '', 0, []
        for c in s:
            tmp.append(c)
            if c == '(':
                op += 1
            else:
                op -= 1
                if not op:
                    ans += "".join(tmp[1:-1])
                    tmp = []
        return ans

# elegent solution from ye15


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        ans = []
        op = 0  # count of open parentheses
        for c in S:
            if c == "(":
                if op > 0:
                    ans.append(c)
                op += 1
            else:
                op -= 1
                if op > 0:
                    ans.append(c)
        return "".join(ans)

""" https://leetcode.com/problems/basic-calculator/
classic stack problem
"""


class Solution:
    def calculate(self, s: str) -> int:
        s = (
            s.replace("+", " + ")
            .replace("-", " - ")
            .replace("(", " ( ")
            .replace(")", " ) ")
            .split()
        )
        stk = []
        sign = 1  # punch line
        ans = 0
        for c in s:
            if c == "+":
                sign = 1
            elif c == "-":
                sign = -1
            elif c == "(":
                stk.extend([ans, sign])
                ans = 0
                sign = 1
            elif c == ")":
                ans *= stk.pop()
                ans += stk.pop()
            else:
                ans += sign * int(c)
        return ans

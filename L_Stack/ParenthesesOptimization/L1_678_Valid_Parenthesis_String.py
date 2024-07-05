""" https://leetcode.com/problems/valid-parenthesis-string/
calculate balance parenthesis by left2right and right2left pass.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        op, cl = 0, 0
        for i in range(len(s)):
            if s[i] == "*" or s[i] == "(":
                op += 1
            elif s[i] == ")":
                op -= 1

            if s[~i] == "*" or s[~i] == ")":
                cl += 1
            elif s[~i] == "(":
                cl -= 1

            if op < 0 or cl < 0:
                return False

        return True

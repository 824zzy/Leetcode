""" https://leetcode.com/problems/score-of-parentheses/
Keep track of the opened parentheses.
Note that only depth(2**(op)) matters to the score.
"""


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans, op = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                op += 1
            else:
                op -= 1
                if s[i - 1] == '(':
                    ans += 2**(op)
        return ans

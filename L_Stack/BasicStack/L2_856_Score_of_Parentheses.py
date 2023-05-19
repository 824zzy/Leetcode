""" https://leetcode.com/problems/score-of-parentheses/
use parenthese depth for computing the score, note that refresh stack when go deeper.
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        ans = 0
        dep = -1
        for i, c in enumerate(s):
            if c=='(': 
                dep += 1
                stk = [dep]
            else: 
                dep -= 1
                if stk: ans += 2**stk.pop()
        return ans
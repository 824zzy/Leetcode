""" https://leetcode.com/problems/score-of-parentheses/
Keep track of the not-closed parentheses.
The answer is 2**(op), as not-cl is the number of exterior set of parentheses.
"""
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans, op= 0, 0
        for i, c in enumerate(s):
            if c=='(': op += 1
            else: 
                op -= 1
                if s[i-1]=='(': ans += 2**(op)
        return ans
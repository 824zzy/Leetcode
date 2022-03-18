""" https://leetcode.com/problems/score-of-parentheses/
solution from god lee
"""
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack, ans = [], 0
        for i in S:
            if i == '(':
                stack.append(ans)
                ans = 0
            else:
                ans += stack.pop() + max(ans, 1)
        return ans
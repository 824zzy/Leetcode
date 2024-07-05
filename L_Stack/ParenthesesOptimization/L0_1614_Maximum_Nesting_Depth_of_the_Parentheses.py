""" https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/submissions/
count maximum count of open parentheses
"""


class Solution:
    def maxDepth(self, s: str) -> int:
        ans, op = 0, 0
        for c in s:
            if c == "(":
                op += 1
            elif c == ")":
                op -= 1
            ans = max(ans, op)
        return ans

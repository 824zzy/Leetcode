""" https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/
minimize the max depth of A&B by evenly distributed their depth
"""


class Solution:
    def maxDepthAfterSplit(self, s: str) -> List[int]:
        op = 0
        ans = []
        for c in s:
            if c == '(':
                op += 1
            ans.append(op & 1)
            if c == ')':
                op -= 1
        return ans

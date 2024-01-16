""" https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
similar to 2116
greedily find imbalanced parentheses through sum up not-opened parentheses and not-closed parentheses
"""
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        op = 0
        ans = 0
        for c in s:
            if c=='(':
                op += 1
            else:
                op -= 1
                if op<0:
                    op = 0
                    ans += 1
        return ans+op
    
    
# unoptimized version
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stk = []
        ans = 0
        for c in s:
            if c=='(':
                stk.append(c)
            else:
                if not stk:
                    ans += 1
                else:
                    stk.pop()
        return ans+len(stk)
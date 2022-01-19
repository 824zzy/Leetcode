""" https://leetcode.com/problems/longest-valid-parentheses/
steal from official solution
greedily find longest valid parentheses when not-opened equals tp not-closed
"""
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        ans = cl = op = 0
        
        for c in s:
            if c=='(': op += 1
            else: cl += 1
            
            if cl==op: ans = max(ans, 2*cl)
            elif cl>=op: cl = op = 0
            
        cl = op = 0
        for c in s[::-1]:
            if c=='(': op += 1
            else: cl += 1
            
            if cl==op: ans = max(ans, 2*op)
            elif op>=cl: cl = op = 0
            
        return ans
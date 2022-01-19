""" https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
filter string by two pass!
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans, op = '', 0
        for c in s:
            if c=='(':  ans, op = ans+c, op+1
            elif c==')' and op>0: ans, op = ans+c, op-1
            elif c not in '()': ans += c
        
        ans2, op = '', 0
        for c in ans[::-1]:
            if c==')':  ans2, op = ans2+c, op+1
            elif c=='(' and op>0: ans2, op = ans2+c, op-1
            elif c not in '()': ans2 += c
        
        return ans2[::-1]

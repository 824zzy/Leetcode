""" https://leetcode.com/problems/valid-parentheses/
"""
class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(': ')', '[': ']', '{': '}'}
        stk = []
        for c in s:
            if c in mp: stk.append(c)
            elif not stk or mp[stk.pop()]!=c: return False
        return not stk
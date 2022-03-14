""" https://leetcode.com/problems/valid-parentheses/
use stack for simulation and map for brevity
"""
class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(': ')', '[': ']', '{': '}'}
        stk = []
        for c in s:
            if c in mp: stk.append(c)
            elif not stk or mp[stk.pop()]!=c: return False
        return not stk
    

class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        for c in s:
            if c in '([{': stk.append(c)
            elif stk:
                cc = stk.pop()
                if (c==')' and cc!='(') or (c=='}' and cc!='{') or (c==']' and cc!='['):
                    return False
            else: return False
        return len(stk)==0
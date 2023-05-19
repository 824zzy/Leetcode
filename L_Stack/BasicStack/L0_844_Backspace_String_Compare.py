""" https://leetcode.com/problems/backspace-string-compare/
scan s and t while check pound sign
"""
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stk1, stk2 = [], []
        for c in s:
            if c=='#': 
                if stk1: stk1.pop()
            else: stk1.append(c)
                
        for c in t:
            if c=='#': 
                if stk2: stk2.pop()
            else: stk2.append(c)
        return stk1==stk2
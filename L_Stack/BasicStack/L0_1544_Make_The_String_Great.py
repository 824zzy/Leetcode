""" https://leetcode.com/problems/make-the-string-great/
stack simulation
"""
class Solution:
    def makeGood(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and c!=stk[-1] and c.lower()==stk[-1].lower():
                stk.pop()
            else: stk.append(c)
        return ''.join(stk)
""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
pop stack if last stack element equals to current
"""
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stk = []
        for c in s:
            if stk and stk[-1]==c:
                stk.pop()
            else:
                stk.append(c)
        return ''.join(stk)
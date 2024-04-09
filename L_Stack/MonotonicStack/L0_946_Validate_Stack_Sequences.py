""" https://leetcode.com/problems/validate-stack-sequences/
special monotonic stack compared with popped stack.
"""
#


class Solution:
    def validateStackSequences(
            self,
            pushed: List[int],
            popped: List[int]) -> bool:
        stk = []
        for p in pushed:
            stk.append(p)
            while stk and stk[-1] == popped[0]:
                popped.pop(0)
                stk.pop()
        return stk == []

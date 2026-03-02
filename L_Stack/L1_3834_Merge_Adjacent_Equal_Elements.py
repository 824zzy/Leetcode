""" https://leetcode.com/problems/merge-adjacent-equal-elements/
Use a stack. For each element, if it equals the stack top, pop and double
(merge). The while loop handles cascading merges: e.g. [2,2,4] produces
stack [2] → merge 2+2=4 → [4] → merge 4+4=8 → [8].
Each element is pushed/popped at most O(log(max_sum)) times due to doubling,
so the total work is O(n log V).
"""


class Solution:
    def mergeAdjacent(self, A: List[int]) -> List[int]:
        stk = []
        for i in range(len(A)):
            x = A[i]
            while stk and stk[-1] == x:
                x += stk[-1]
                stk.pop()
            stk.append(x)
        return stk

""" https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/

"""


class Solution:
    def mctFromLeafValues(self, A: List[int]) -> int:
        ans = 0
        stk = []
        for x in A:
            while stk and stk[-1] <= x:
                val = stk.pop()
                ans += val * min(stk[-1] if stk else inf, x)
            stk.append(x)
        return ans + sum(stk[i - 1] * stk[i] for i in range(1, len(stk)))

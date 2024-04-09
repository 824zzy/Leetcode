""" https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/
simply find the sum of cost by directions
"""


class Solution:
    def minCost(
            self,
            S: List[int],
            E: List[int],
            Rc: List[int],
            Cc: List[int]) -> int:
        ans = 0
        if S[0] < E[0]:
            ans += sum(Rc[S[0] + 1:E[0] + 1])
        elif S[0] > E[0]:
            ans += sum(Rc[E[0]:S[0]])
        if S[1] < E[1]:
            ans += sum(Cc[S[1] + 1:E[1] + 1])
        elif S[1] > E[1]:
            ans += sum(Cc[E[1]:S[1]])
        return ans

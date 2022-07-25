""" https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
sort the properties and maintain monotonic decreasing stack
"""
class Solution:
    def numberOfWeakCharacters(self, P: List[List[int]]) -> int:
        P.sort(key=lambda x: (x[0], -x[1]))
        stk = []
        ans = 0
        for i, (_, d) in enumerate(P):
            while stk and P[stk[-1]][1]<d:
                stk.pop()
                ans += 1
            stk.append(i)
        return ans
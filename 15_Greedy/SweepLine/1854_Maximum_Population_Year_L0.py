""" https://leetcode.com/problems/maximum-population-year/
sweep line to find maximum population and its year.
"""
class Solution:
    def maximumPopulation(self, A: List[List[int]]) -> int:
        A = sorted([x for i, j in A for x in [[i, 1], [j, -1]]])
        ans = cnt = ma_cnt = 0
        for x, k in A:
            cnt += k
            if cnt>ma_cnt:
                ans = x
                ma_cnt = cnt
        return ans
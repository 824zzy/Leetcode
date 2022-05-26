""" https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/
minA which precalculate the minimum element in a row is needed for pruning
"""
class Solution:
    def minimizeTheDifference(self, A: List[List[int]], t: int) -> int:
        minA = [min(a) for a in A]
        @cache
        def dfs(i, s):
            if i==len(A): return abs(s-t)
            if s>=t: return dfs(i+1, s+minA[i])
            return min([dfs(i+1, s+x) for x in A[i]])
        
        return dfs(0, 0)
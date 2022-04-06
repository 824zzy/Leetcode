""" https://leetcode.com/problems/combinations/
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        stk = []
        
        def dfs(i):
            if len(stk)==k: ans.append(stk.copy())
            for j in range(i, n+1):
                stk.append(j)
                dfs(j+1)
                stk.pop()
        
        dfs(1)
        return ans
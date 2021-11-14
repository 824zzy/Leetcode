""" L0: https://leetcode.com/problems/combination-sum/
"""
class Solution:
    def combinationSum(self, A: List[int], T: int) -> List[List[int]]:
        def dfs(i, t):
            if t==0: return ans.append(stk.copy())
            for j in range(i, len(A)):
                if t<A[j]: break
                stk.append(A[j])
                dfs(j, t-A[j])
                stk.pop()
        
        A.sort()
        ans = []
        stk = []
        dfs(0, T)
        return ans
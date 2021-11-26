""" https://leetcode.com/problems/delete-and-earn/
Create a mapping from value to points in M since we can obstain all the points of a valid value.
Then apply top down dp
"""
class Solution:
    def deleteAndEarn(self, A: List[int]) -> int:
        M = defaultdict(int)
        for x in A: M[x] += x
        
        @lru_cache(None)
        def dfs(i): 
            if i<0: return 0 
            if A[i]-1 not in M: return M[A[i]] + dfs(i-1)
            return max(M[A[i]]+dfs(i-2), dfs(i-1))
        
        A = sorted(set(A))
        return dfs(len(A)-1)
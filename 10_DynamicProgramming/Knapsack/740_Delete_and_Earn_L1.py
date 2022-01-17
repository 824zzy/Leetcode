""" https://leetcode.com/problems/delete-and-earn/
1. create a mapping from value to points in M since we can obstain all the points of a valid value
2. if A[i]-1 not in M, then we must choose A[i]
3. find maximum between choose A[i] and skip A[i]
"""
    
class Solution:
    def deleteAndEarn(self, A: List[int]) -> int:
        M = defaultdict(int)
        for x in A: M[x] += x
        
        @cache
        def dfs(i): 
            if i<0: return 0 
            if A[i]-1 not in M: return M[A[i]] + dfs(i-1)
            return max(M[A[i]]+dfs(i-2), dfs(i-1))
        
        A = sorted(set(A))
        return dfs(len(A)-1)
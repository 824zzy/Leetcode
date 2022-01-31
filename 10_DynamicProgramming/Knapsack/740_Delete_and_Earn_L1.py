""" https://leetcode.com/problems/delete-and-earn/
1. use hash table for calculating score and sorted keys as A
2. At i-th number, we can skip it or select it, if we select it then check if next number needs to be deleted.
"""
class Solution:
    def deleteAndEarn(self, A: List[int]) -> int:
        cnt = Counter(A)
        A = [k for k, v in sorted(cnt.items())]
        
        @cache
        def dfs(i):
            if i==len(A): return 0
            ans = dfs(i+1) # skip
            if i<len(A)-1 and A[i]+1==A[i+1]: # select and delete
                return max(ans, cnt[A[i]]*A[i]+dfs(i+2))
            else: # select and not delete
                return max(ans, cnt[A[i]]*A[i]+dfs(i+1))
        
        return dfs(0)
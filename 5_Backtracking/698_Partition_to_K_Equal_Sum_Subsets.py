""" L2
"""
class Solution:
    def canPartitionKSubsets(self, A: List[int], k: int) -> bool:
        t = sum(A)//k
        if sum(A)%k: return False
        A.sort(reverse=True)
        T = [t] * len(A)
        def dfs(idx):
            if idx==len(A): return True
            for i, n in enumerate(A):
                if T[i]>=A[idx]:
                    T[i] -= A[idx]
                    if dfs(idx+1): return True
                    T[i] += A[idx]
            return False

        return dfs(0)
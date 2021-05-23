class Solution:
    def findCircleNum(self, A: List[List[int]]) -> int:
        def dfs(i):
            visit[i] = True
            for j in range(len(A)):
                if A[i][j]==1 and not visit[j]:
                    dfs(j)
        
        if not A: return 0
        visit = [0] * len(A)
        ans = 0
        for i in range(len(A)):
            if not visit[i]:
                dfs(i)
                ans += 1
        return ans
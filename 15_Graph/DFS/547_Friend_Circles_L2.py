from collections import defaultdict
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        
        n = len(M)
        g = defaultdict(list)
        
        for i in range(n):
            for j in range(i+1, n):
                if M[i][j]==1:
                    g[i].append(j)
                    g[j].append(i)
                    
        visit = [0] * n
        
        def dfs(node):
            for n in g[node]:
                if not visit[n]:
                    visit[n] = 1
                    dfs(n)
        
        ans = 0
        for i in range(n):
            if not visit[i]:
                ans += 1
                visit[i] = 1
                dfs(i)
        return ans
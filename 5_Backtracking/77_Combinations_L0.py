class Solution(object):
    def combine(self, n, k):
        ans = []
        
        def dfs(remain, k, path):
            if k==0:
                ans.append(path)
                return
            for i, n in enumerate(remain):
                dfs(remain[i+1:], k-1, path+[n])
        
        dfs([i for i in range(1, n+1)], k, [])
        return ans
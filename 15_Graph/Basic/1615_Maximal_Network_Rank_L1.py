class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for r in roads:
            g[r[0]].append(str(r[0])+' '+str(r[1]))
            g[r[1]].append(str(r[0])+' '+str(r[1]))

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                ans = max(len(set(g[i]+g[j])), ans)
        return ans
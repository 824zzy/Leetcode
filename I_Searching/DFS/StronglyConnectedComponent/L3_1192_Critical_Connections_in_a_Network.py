""" https://leetcode.com/problems/critical-connections-in-a-network/
Tarjan's algorithm to find strong connected component
"""


class Solution:
    def criticalConnections(
            self, n: int, connections: List[List[int]]) -> List[List[int]]:
        G = defaultdict(list)
        for u, v in connections:
            G[u].append(v)
            G[v].append(u)

        low = [-1] * n

        def dfs(i, p, step):
            low[i] = step + 1
            for j in G[i]:
                if low[j] == -1:
                    low[i] = min(low[i], dfs(j, i, step + 1))
                elif j != p:
                    low[i] = min(low[i], low[j])

            if low[i] == step + 1 and i != 0:
                ans.append([p, i])
            return low[i]

        ans = []
        dfs(0, -1, 0)
        return ans

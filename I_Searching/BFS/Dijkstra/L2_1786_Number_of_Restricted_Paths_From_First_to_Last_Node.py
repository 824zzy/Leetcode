""" https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
dijkstra algorithm + top down dp
dijkstra algorithm to find lowest weight from current node to node n.
top down dp to calculate the number of restricted path
"""


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        e = defaultdict(dict)
        for i, j, k in edges:
            e[i][j] = k
            e[j][i] = k

        pq = [(0, n)]
        seen = {}
        while pq:
            s1, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = s1
                for j in e[i]:
                    s2 = e[i][j] + s1
                    heapq.heappush(pq, (s2, j))

        @cache
        def dp(node):
            if node == n:
                return 1
            ans = 0
            for nei in e[node]:
                if seen[nei] < seen[node]:
                    ans += dp(nei)
            return ans
        return dp(1) % (10**9 + 7)

""" https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/
refer to dba: https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/discuss/1844130/Python-3-Dijkstras-explained.
1. From s1 to x, for this we use Dijkstra
2. From s2 to x, same.
3. From x to dest, for this we use Dijkstra on the reversed graph.
4. Finally, we check all possible x.
"""


class Solution:
    def minimumWeight(self,
                      n: int,
                      edges: List[List[int]],
                      src1: int,
                      src2: int,
                      dest: int) -> int:
        G = collections.defaultdict(dict)
        reverse_G = collections.defaultdict(dict)
        for i, j, w in edges:
            G[i][j] = min(w, G[i].get(j, inf))
            reverse_G[j][i] = min(w, reverse_G[j].get(i, inf))

        def dijkstra(G, src):
            pq = [(0, src)]
            seen = {}
            while pq:
                cost, i = heapq.heappop(pq)
                if i not in seen:
                    seen[i] = cost
                    for j in G[i]:
                        heapq.heappush(pq, (cost + G[i][j], j))
            # shortest path from src to all the nodes
            return [seen.get(i, inf) for i in range(n)]

        src1_x = dijkstra(G, src1)
        src2_x = dijkstra(G, src2)
        dest_x = dijkstra(reverse_G, dest)

        ans = inf
        for i in range(n):
            ans = min(ans, src1_x[i] + src2_x[i] + dest_x[i])

        return ans if ans != inf else -1


# floyd-warshall solution below will TLE, don't do that
class Solution:
    def minimumWeight(self,
                      n: int,
                      edges: List[List[int]],
                      src1: int,
                      src2: int,
                      dest: int) -> int:
        N = n
        # floyd-warshall
        dist1 = [[inf] * N for _ in range(N)]
        dist2 = [[inf] * N for _ in range(N)]
        for i in range(n):
            dist1[i][i], dist2[i][i] = 0, 0
        for i, j, w in edges:
            dist1[i][j], dist2[j][i] = min(dist1[i][j], w), min(dist2[i][j], w)

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist1[i][j] = min(dist1[i][j], dist1[i][k] + dist1[k][j])
                    dist2[j][i] = min(dist2[j][i], dist2[j][k] + dist2[k][i])

        ans = inf
        for i in range(n):
            ans = min(ans, dist1[src1][i] + dist1[src2][i] + dist2[dest][i])
        return ans if ans != inf else -1

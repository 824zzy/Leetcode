""" L1
Use dijkstra algorithm to find the shorest path from each point to the others.
"""
# dijkstra algorithm
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], T: int) -> int:
        e = defaultdict(dict)
        for i, j, k in edges:
            e[i][j] = k
            e[j][i] = k
        
        ans = (float('inf'), float('-inf'))
        for start in range(n):
            pq = [(-T, start)]
            seen = Counter()
            while pq:
                t1, i = heapq.heappop(pq)
                if i not in seen:
                    seen[i] = 1
                    for j in e[i]:
                        t2 = t1+e[i][j]
                        if j not in seen and t2<=0:
                            heapq.heappush(pq, (t2, j))
            cnt = sum(seen.values())-1
            if (cnt==ans[0] and start>ans[1]) or (cnt<ans[0]): ans = (cnt, start)
        return ans[1]

# floyd algorithm
class Solution:
    def findTheCity(self, n, edges, maxd):
        dis = [[float('inf')] * n for _ in xrange(n)]
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
        for i in xrange(n):
            dis[i][i] = 0
        for k in xrange(n):
            for i in xrange(n):
                for j in xrange(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
        res = {sum(d <= maxd for d in dis[i]): i for i in xrange(n)}
        return res[min(res)]
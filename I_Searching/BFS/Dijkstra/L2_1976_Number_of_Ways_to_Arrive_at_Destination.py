""" https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
use ways and distances to find the number of ways to arrive at destination
"""


class Solution:
    def countPaths(self, n: int, A: List[List[int]]) -> int:
        ans = Counter()
        G = defaultdict(dict)
        for i, j, k in A:
            G[i][j] = k
            G[j][i] = k

        dists, ways = [inf] * n, [0] * n
        dists[0], ways[0] = 0, 1

        pq = [(0, 0)]
        while pq:
            t, i = heappop(pq)
            if t > dists[-1]:
                break
            if t == dists[i]:
                for j in G[i]:
                    if dists[i] + G[i][j] < dists[j]:
                        dists[j] = dists[i] + G[i][j]
                        ways[j] = ways[i]
                        heapq.heappush(pq, (dists[j], j))
                    elif dists[i] + G[i][j] == dists[j]:
                        ways[j] += ways[i]
        return ways[-1] % (10 ** 9 + 7)

""" L3:
use "seen" to get farthest reachable node in new graph.
seen[i] means that we can arrive at node i and have seen[i] moves left.
"""


class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, n: int) -> int:
        e = collections.defaultdict(dict)
        for i, j, l in edges:
            e[i][j] = e[j][i] = l
        pq = [(-M, 0)]
        seen = {}
        while pq:
            moves, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = -moves
                for j in e[i]:
                    moves2 = -moves - e[i][j] - 1
                    if j not in seen and moves2 >= 0:
                        heapq.heappush(pq, (-moves2, j))
        ans = len(seen)
        for i, j, k in edges:
            ans += min(seen.get(i, 0) + seen.get(j, 0), e[i][j])
        return ans

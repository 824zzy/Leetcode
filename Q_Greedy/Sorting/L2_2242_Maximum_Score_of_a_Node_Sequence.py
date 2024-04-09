""" https://leetcode.com/problems/maximum-score-of-a-node-sequence/
Sort greedy on graph

First notice that the "edges.length <= 5*10^4", so brute force O(|V|^4) or O(|E|^3) will TLE.
The intuition is no need to enumerate all neighbors, just need to check top 3 neighbors.
1. Pre-computation, find 3 largest neighbors for each node. O(|E|log3)
2. Enumerate all edges, for node a and node b, try to find their largest neighbors node c and node d

Time: O(E*k^2), where E is the number of edges, k is the number of neighbors(3)
"""


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append([-scores[j], j])
            G[j].append([-scores[i], i])
        for k, v in G.items():
            G[k] = sorted(v)[:3]

        ans = -1
        for i, j in edges:
            for _, ii in G[i]:
                for _, jj in G[j]:
                    if ii != jj and ii != j and jj != i:
                        ans = max(
                            ans,
                            scores[i] +
                            scores[j] +
                            scores[ii] +
                            scores[jj])
        return ans

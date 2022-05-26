""" https://leetcode.com/problems/maximum-score-of-a-node-sequence/
learn from huahua: https://www.youtube.com/watch?v=OmV6vuP6pWw
and lee: https://leetcode.com/problems/maximum-score-of-a-node-sequence/discuss/1953706/JavaPython-Keep-3-Biggest-Neighbours

First notice that the "edges.length <= 5*10^4", so brute force O(|V|^4) or O(|E|^3) will TLE.
The intuition is no need to enumerate all neighbors, just need to check top 3 neighbors.
1. Pre-computation, find 3 largest neighbors for each node. O(|E|log3)
2. Enumerate all edges, for node a and node b, try to find their largest neighbors node c and node d

Time: O(E*k^2)
"""
class Solution:
    def maximumScore(self, A: List[int], edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append([A[j], j])
            G[j].append([A[i], i])
        
        for i in range(len(A)): G[i] = nlargest(3, G[i])
        
        ans = -1
        for i, j in edges:
            for sii, ii in G[i]:
                for sjj, jj in G[j]:
                    if ii!=jj and ii!=j and jj!=i:
                        ans = max(ans, sii+A[i]+A[j]+sjj)
        return ans
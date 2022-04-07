""" L2: https://leetcode.com/problems/the-time-when-the-network-becomes-idle/
TODO: https://leetcode.com/problems/the-time-when-the-network-becomes-idle/discuss/1524183/Python3-graph
"""
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        # build graph
        G = defaultdict(list)
        for u, v in edges: 
            G[u].append(v)
            G[v].append(u)
        # distance by bfs
        seen = {0: 0}
        Q = [0]
        dist = 0
        while Q:
            dist += 2
            nextQ = []
            for u in Q: 
                for v in G[u]:
                    if v not in seen:
                        seen[v] = dist
                        nextQ.append(v)
            Q = nextQ
        # find earliest second
        ans = 0
        for i, p in enumerate(patience):
            if p:
                d = seen[i]
                k = d//p-int(d%p==0)
                ans = max(ans, d+k*p)
        return ans+1
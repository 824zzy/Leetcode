""" https://leetcode.com/problems/minimum-genetic-mutation/
the same as 127, it is medium for the sake of loose time limit.
1. create a graph by checking all possible candidates O(n*8*4) rather than double for loop O(n^2)
2. classic bfs to find minimum step
"""
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank += [start]
        m, n = len(start), len(bank)
        bank = set(bank)
        G = defaultdict(list)
        for g in bank:
            for i in range(8):
                p1, p2 = g[:i], g[i+1:]
                for j in "ACGT":
                    if p1+j+p2 in bank:
                        G[g].append(p1+j+p2)
                    
        Q = [[start, 0]]
        seen = set()
        seen.add(start)
        while Q:
            i, step = Q.pop(0)
            if i==end: return step
            for j in G[i]:
                if j not in seen:
                    Q.append([j, step+1])
                    seen.add(j)
        return -1
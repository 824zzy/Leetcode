""" https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/
1. use topological sort the traverse the graph
2. use list of sets to `update` ancestors of parents and `add` parents
"""


class Solution:
    def getAncestors(self, n: int, A: List[List[int]]) -> List[List[int]]:
        e = defaultdict(list)
        inD = [0] * n
        for i, j in A:
            e[i].append(j)
            inD[j] += 1

        Q = [i for i, d in enumerate(inD) if d == 0]
        ans = [set() for i in range(n)]
        while Q:
            i = Q.pop(0)
            for j in e[i]:
                inD[j] -= 1
                ans[j].update(ans[i])
                ans[j].add(i)
                if not inD[j]:
                    Q.append(j)
        return [sorted(list(ans[i])) for i in range(n)]

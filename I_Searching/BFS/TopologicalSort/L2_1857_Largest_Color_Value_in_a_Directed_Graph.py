""" https://leetcode.com/problems/largest-color-value-in-a-directed-graph/
topological sort and use hash table to greedily update maximal colors on the fly.
"""


class Solution:
    def largestPathValue(self, colors: str, A: List[List[int]]) -> int:
        e = defaultdict(list)
        n = len(colors)
        inD = [0] * n
        for i, j in A:
            e[i].append(j)
            inD[j] += 1

        Q = [i for i, d in enumerate(inD) if d == 0]
        cnts = [[0] * 26 for _ in range(n)]
        while Q:
            i = Q.pop(0)
            cnts[i][ord(colors[i]) - ord('a')] += 1
            for j in e[i]:
                cnts[j] = list(map(max, cnts[i], cnts[j]))
                inD[j] -= 1
                if not inD[j]:
                    Q.append(j)

        if sum(inD) > 0:
            return -1
        else:
            return max([max(node) for node in cnts])

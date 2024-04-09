""" https://leetcode.com/problems/maximum-total-importance-of-roads/
1. assign importance score based on the in degree and out degree
2. sum up the two ends' score as answer
"""


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        G = Counter()
        for i, j in roads:
            G[i] += 1
            G[j] += 1

        imp = {}
        single = n - len(G) + 1
        for i, (k, _) in enumerate(sorted(G.items(), key=lambda x: x[1])):
            imp[k] = i + single

        ans = 0
        for i, j in roads:
            ans += imp[i] + imp[j]
        return ans

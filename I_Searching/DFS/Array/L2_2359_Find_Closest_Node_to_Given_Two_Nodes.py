""" https://leetcode.com/problems/find-closest-node-to-given-two-nodes/
1. run DFS independently for node 1 and 2, memorizing the distance to each node we reach.
2. we check each node and return the one with minimum max distance.
"""
from header import *


class Solution:
    def closestMeetingNode(self, E: List[int], n1: int, n2: int) -> int:
        seen1 = [-1] * len(E)
        seen2 = [-1] * len(E)

        def dfs(node, d, seen):
            if node != -1 and seen[node] == -1:
                seen[node] = d
                dfs(E[node], d + 1, seen)

        dfs(n1, 0, seen1)
        dfs(n2, 0, seen2)

        ans = [inf, -1]
        for node, (mx, mn) in enumerate(zip(seen1, seen2)):
            if mx != -1 and mn != -1 and max(mx, mn) < ans[0]:
                ans = [max(mx, mn), node]
        return ans[1]


"""
[2,2,3,-1]
0
1
[1,2,-1]
0
2
[4,4,4,5,1,2,2]
1
1
[2,0,0]
2
0
[1,5,5,0,6,4,0]
5
0
"""

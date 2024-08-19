""" https://leetcode.com/problems/count-the-number-of-good-nodes/
dfs with parent
"""

from header import *


class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        G = [[] for _ in range(n)]
        for x, y in edges:
            G[x].append(y)
            G[y].append(x)
        ans = 0

        def dfs(node, parent):
            nonlocal ans
            if len(G[node]) == 1 and parent != None:
                ans += 1
                return 1
            children_sizes = []
            for nei in G[node]:
                if nei != parent:
                    children_size = dfs(nei, node)
                    children_sizes.append(children_size)
            if len(set(children_sizes)) == 1:
                ans += 1
            return sum(children_sizes) + 1

        dfs(0, None)
        return ans


# solution from 0x3ff
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        G = [[] for _ in range(n)]
        for x, y in edges:
            G[x].append(y)
            G[y].append(x)
        ans = 0

        def dfs(x, fa):
            nonlocal ans
            size = 1
            pre = 0
            ok = True

            for y in G[x]:
                if y == fa:
                    continue

                sz = dfs(y, x)
                if pre > 0 and sz != pre:
                    ok = False
                pre = sz
                size += sz
            ans += ok
            return size

        dfs(0, None)
        return ans


"""
[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
[[0,1],[1,2],[2,3],[3,4],[0,5],[1,6],[2,7],[3,8]]
[[0,1],[1,2],[1,3],[1,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[9,12],[10,11]]
[[6,0],[1,0],[5,1],[2,5],[3,1],[4,3]]
[[2,0],[4,2],[1,2],[3,1],[5,1]]
"""

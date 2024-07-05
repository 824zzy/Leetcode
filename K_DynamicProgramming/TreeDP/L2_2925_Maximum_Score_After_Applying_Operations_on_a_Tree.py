""" https://leetcode.com/problems/maximum-score-after-applying-operations-on-a-tree/
solution 1: knapsack on tree
solution 2 from 0x3ff: think reversely, only focus on which node to delete
"""
from header import *


class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        @cache
        def dp(i, p, has_skipped):
            # check leaf node
            if len(G[i]) == 1 and G[i] == [p]:
                if has_skipped:
                    return values[i]
                else:
                    return 0
            ans = 0
            ans1 = 0
            ans2 = 0
            # if already skipped one node, then take all the nodes in the path
            if has_skipped:
                ans = values[i]
                for j in G[i]:
                    if j != p:
                        ans += dp(j, i, True)
            else:
                # skip
                ans1 = 0
                # choose
                ans2 = values[i]
                for j in G[i]:
                    if j != p:
                        ans1 += dp(j, i, True)
                        ans2 += dp(j, i, False)
            return max(ans, ans1, ans2)

        return dp(0, -1, False)


class Solution:
    def maximumScoreAfterOperations(
        self, edges: List[List[int]], values: List[int]
    ) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        @cache
        def dp(i, p):
            # check leaf node
            if len(G[i]) == 1 and G[i] == [p]:
                return values[i]
            # delete current node
            loss = values[i]
            # keep current node
            loss2 = 0
            for j in G[i]:
                if j != p:
                    loss2 += dp(j, i)
            return min(loss, loss2)

        return sum(values) - dp(0, -1)

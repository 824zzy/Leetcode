""" https://leetcode.com/problems/sum-of-distances-in-tree/
From guan: https://github.com/wisdompeak/LeetCode/tree/master/Tree/834.Sum-of-Distances-in-Tree
Intuition: f(child) = f(parent) + a - b, where b = subtree_size(child) and a = n - b

1. pick "0" as a root
2. use dfs to get subtree_size of every node
3. use another dfs to get the distance sum from every node to root.
3. use the third dfs and the dp formula above to calculate the final answer
"""
from header import *


class Solution(object):
    def sumOfDistancesInTree(self, N, edges):
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        def count_subtree(i):
            sm = 1
            for j in G[i]:
                if not seen[j]:
                    seen[j] = 1
                    sm += count_subtree(j)
            subtree[i] = sm
            return sm

        subtree = [0] * N
        seen = [1] + [0] * (N - 1)
        count_subtree(0)

        def count_sum(i):
            sm = 0
            for j in G[i]:
                if not seen[j]:
                    seen[j] = 1
                    sm += count_sum(j)
            sm += subtree[i] - 1
            return sm

        seen = [1] + [0] * (N - 1)
        ans = [0] * N
        ans[0] = count_sum(0)

        def count_all(i, total):
            for j in G[i]:
                if not seen[j]:
                    seen[j] = 1
                    a = subtree[j]
                    b = N - subtree[j]
                    ans[j] = total + b - a
                    count_all(j, ans[j])

        seen = [1] + [0] * (N - 1)
        count_all(0, ans[0])
        return ans

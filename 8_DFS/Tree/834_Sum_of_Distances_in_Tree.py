""" LX: TODO: https://leetcode.com/problems/sum-of-distances-in-tree/discuss/130583/C%2B%2BJavaPython-Pre-order-and-Post-order-DFS-O(N)
"""
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def dfs(root, pre):
            # visit all neighbors
            for i in tree[root]:
                # except root's predecessor
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]
                    res[root] += res[i] + count[i]

        def dfs2(root, pre):
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)
        dfs(0, -1)
        dfs2(0, -1)
        return res
""" https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/
TODO: learn from ye15: https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/discuss/2198386/Python3-dfs
"""


class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def fn(u):
            score[u] = nums[u]
            child[u] = {u}
            for v in graph[u]:
                if seen[v] == 0:
                    seen[v] = 1
                    fn(v)
                    score[u] ^= score[v]
                    child[u] |= child[v]

        seen = [1] + [0] * (n - 1)
        score = [0] * n
        child = [set() for _ in range(n)]
        fn(0)

        ans = inf
        for u in range(1, n):
            for v in range(u + 1, n):
                if u in child[v]:
                    uu = score[u]
                    vv = score[v] ^ score[u]
                    xx = score[0] ^ score[v]
                elif v in child[u]:
                    uu = score[u] ^ score[v]
                    vv = score[v]
                    xx = score[0] ^ score[u]
                else:
                    uu = score[u]
                    vv = score[v]
                    xx = score[0] ^ score[u] ^ score[v]
                ans = min(ans, max(uu, vv, xx) - min(uu, vv, xx))
        return ans

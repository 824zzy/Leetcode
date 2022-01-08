""" https://leetcode.com/problems/minimum-interval-to-include-each-query/
TODO: https://leetcode.com/problems/minimum-interval-to-include-each-query/discuss/1186817/JavaC%2B%2BPython-Priority-Queue-Solution
"""
class Solution:
    def minInterval(self, A, queries):
        A = sorted(A, reverse=True)
        h = []
        res = {}
        for q in sorted(queries):
            while A and A[-1][0] <= q:
                i, j = A.pop()
                if j >= q:
                    heapq.heappush(h, [j - i + 1, j])
            while h and h[0][1] < q:
                heapq.heappop(h)
            res[q] = h[0][0] if h else -1
        return [res[q] for q in queries]
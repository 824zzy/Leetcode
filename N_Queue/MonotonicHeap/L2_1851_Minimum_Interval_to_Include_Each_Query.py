""" https://leetcode.com/problems/minimum-interval-to-include-each-query/
TODO: https://leetcode.com/problems/minimum-interval-to-include-each-query/discuss/1186817/JavaC%2B%2BPython-Priority-Queue-Solution
"""
class Solution:
    def minInterval(self, A, queries):
        A = sorted(A)
        pq = []
        ans = {}
        for q in sorted(queries):
            # find open intervals and use `size`, `ending` as key
            while A and A[0][0]<=q:
                i, j = A.pop(0)
                if j >= q:
                    heappush(pq, [j-i+1, j])
            # remove invalid intervals
            while pq and pq[0][1]<q:
                heappop(pq)
            ans[q] = pq[0][0] if pq else -1
        return [ans[q] for q in queries]
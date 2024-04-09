""" https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/
https://leetcode.com/problems/maximum-number-of-tasks-you-can-assign/discuss/1576033/Python-greedy-%2B-binary-search-explained
"""


class Solution:
    def maxTaskAssign(self, T: List[int], W: List[int], p: int, s: int) -> int:
        T, W = sorted(T), sorted(W)
        l, r = 0, min(len(T), len(W)) + 1

        def fn(m, p, s, W):
            W = W[-m:]
            _p = p
            for t in T[:m][::-1]:
                idx = bisect_left(W, t)
                if idx < len(W):
                    W.pop(idx)
                elif _p:
                    idx = bisect_left(W, t - s)
                    if idx < len(W):
                        W.pop(idx)
                        _p -= 1
                else:
                    return False
            return len(W) == 0

        while l < r:
            m = (l + r) // 2
            if not fn(m, p, s, W):
                r = m
            else:
                l = m + 1
        return l - 1 if l - 1 >= 0 else 0

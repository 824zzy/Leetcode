""" https://leetcode.com/problems/minimum-cost-to-merge-stones/
too hard: https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/1465680/Python3-dp
"""


class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        if (len(stones) - 1) % (k - 1):
            return -1  # impossible

        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)

        @cache
        def fn(lo, hi):
            """Return min cost of merging stones[lo:hi]."""
            if hi - lo < k:
                return 0  # not enough stones
            ans = inf
            for mid in range(lo + 1, hi, k - 1):
                ans = min(ans, fn(lo, mid) + fn(mid, hi))
            if (hi - lo - 1) % (k - 1) == 0:
                ans += prefix[hi] - prefix[lo]
            return ans

        return fn(0, len(stones))

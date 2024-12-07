""" https://leetcode.com/problems/sell-diminishing-valued-colred-balls/
steal from: https://leetcode.com/problems/sell-diminishing-valued-colored-balls/discuss/927674/Python3-Greedy
"""


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        # count how many balls can be sold with this threshold
        def fn(x):
            return sum(max(0, xx - x) for xx in inventory)

        l, r = 0, 10 ** 9
        while l < r:
            mid = l + r + 1 >> 1
            if fn(mid) >= orders:
                l = mid
            else:
                r = mid - 1

        upper = sum(x * (x + 1) // 2 - l * (l + 1) // 2 for x in inventory if x > l)
        lower = (fn(l) - orders) * (l + 1)
        return (upper - lower) % (10 ** 9 + 7)

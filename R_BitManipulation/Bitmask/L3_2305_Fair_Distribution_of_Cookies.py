""" https://leetcode.com/problems/fair-distribution-of-cookies/
solution from ye: https://leetcode.com/problems/fair-distribution-of-cookies/discuss/2141196/Python3-masked-dp
"""


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        @cache
        def fn(mask, k):
            """Return min unfairness of distributing cookies marked by mask to k children."""
            if mask == 0:
                return 0
            if k == 0:
                return inf
            ans = inf
            orig = mask
            while mask:
                mask = orig & (mask - 1)
                amt = sum(cookies[i]
                          for i in range(n) if (orig ^ mask) & 1 << i)
                ans = min(ans, max(amt, fn(mask, k - 1)))
            return ans

        return fn((1 << n) - 1, k)

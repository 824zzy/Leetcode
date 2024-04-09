""" https://leetcode.com/problems/stone-game-v/
the hardest part is how to optimize n^3 to n^2. The solution below gets TLE.
"""


class Solution:
    def stoneGameV(self, A: List[int]) -> int:
        # pref sum
        pref = [0] + list(itertools.accumulate(A))

        @lru_cache(None)
        def fn(l, r):
            """Return the score of arranging values from l (inclusive) to r (exclusive). """
            if l + 1 == r:
                return 0
            ans = 0
            for m in range(l + 1, r):
                ll = pref[m] - pref[l]
                rr = pref[r] - pref[m]
                if ll < rr:
                    ans = max(ans, ll + fn(l, m))
                elif ll > rr:
                    ans = max(ans, rr + fn(m, r))
                else:
                    ans = max(ans, ll + max(fn(l, m), fn(m, r)))
            return ans

        return fn(0, len(A))

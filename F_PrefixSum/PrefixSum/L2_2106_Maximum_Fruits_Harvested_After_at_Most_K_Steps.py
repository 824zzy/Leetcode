""" https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/
it is stolen from genius Bakerston
https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/discuss/1624232/Python-Explanation-with-pictures-2-solutions.
"""


class Solution:
    def maxTotalFruits(self, A: List[List[int]], pos: int, k: int) -> int:
        r_b = max(pos, A[-1][0])
        amt = [0] * (1 + r_b)
        for a, b in A:
            amt[a] = b
        # prefix sum
        presum = [0] + list(itertools.accumulate(amt))
        ans = 0
        # The right distance to start position.
        for rd in range(min(k, r_b - pos) + 1):
            # If we turn around, how far we can go left beyond start position.
            ld = max(0, k - 2 * rd)
            # The leftmost and rightmost position we can reach.
            lp, rp = max(0, pos - ld), pos + rd
            # Get overall fruits within this range from presum.
            ans = max(ans, presum[rp + 1] - presum[lp])

        for ld in range(min(k, pos) + 1):
            rd = max(0, k - 2 * ld)
            lp, rp = pos - ld, min(r_b, pos + rd)
            ans = max(ans, presum[rp + 1] - presum[lp])

        return ans

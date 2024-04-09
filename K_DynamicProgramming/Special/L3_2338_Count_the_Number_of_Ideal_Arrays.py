""" https://leetcode.com/problems/count-the-number-of-ideal-arrays/
TODO: steal from ye: https://leetcode.com/problems/count-the-number-of-ideal-arrays/discuss/2261351/Python3-freq-table
"""


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        ans = maxValue
        freq = {x: 1 for x in range(1, maxValue + 1)}
        for k in range(1, n):
            temp = Counter()
            for x in freq:
                for m in range(2, maxValue // x + 1):
                    ans += comb(n - 1, k) * freq[x]
                    temp[m * x] += freq[x]
            freq = temp
            ans %= 1_000_000_007
        return ans

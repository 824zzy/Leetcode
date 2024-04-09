""" https://leetcode.com/problems/number-of-ways-to-select-buildings/
TODO: learn from: https://leetcode.com/problems/number-of-ways-to-select-buildings/discuss/1907871/Python-3-or-Prefix-and-Suffix-sum-Easy-to-understand-or-Explanation
"""


class Solution:
    def numberOfWays(self, s: str) -> int:
        prefix = []
        one = zero = 0
        for c in s:                                # find number of 0 or 1 before index `i`
            prefix.append([zero, one])
            if c == '1':
                one += 1
            else:
                zero += 1

        suffix = []
        one = zero = 0
        for c in s[::-1]:                          # find number of 0 or 1 after index `i`
            suffix.append([zero, one])
            if c == '1':
                one += 1
            else:
                zero += 1
        # reverse since we trace from right to left
        suffix = suffix[::-1]
        ans = 0
        # for c=='1' number of combination is prefix[i][0] * suffix[i][0] ([0
        # before index `i`] * [0 after index `i`])
        for i, c in enumerate(s):
            if c == '1':
                ans += prefix[i][0] * suffix[i][0]
            else:
                ans += prefix[i][1] * suffix[i][1]
        return ans

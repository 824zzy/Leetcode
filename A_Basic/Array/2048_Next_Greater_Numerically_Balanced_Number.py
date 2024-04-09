""" L1: https://leetcode.com/contest/weekly-contest-264/problems/next-greater-numerically-balanced-number/
brute force search, have to use divmod otherwise time limit exceeded.
"""


class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        while True:
            n += 1
            nn = n
            freq = defaultdict(int)
            while nn:
                nn, d = divmod(nn, 10)
                freq[d] += 1
            if all(k == v for k, v in freq.items()):
                return n

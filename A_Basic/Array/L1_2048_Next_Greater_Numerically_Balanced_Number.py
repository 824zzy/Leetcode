""" https://leetcode.com/contest/weekly-contest-264/problems/next-greater-numerically-balanced-number/
brute force search, have to use divmod otherwise time limit exceeded.
"""

from header import *


# divmod based solution
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


# string based solution
class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        for _ in count():
            n += 1
            s = str(n)
            cnt = Counter(s)
            for k, v in cnt.items():
                if int(k) != v:
                    break
            else:
                return n

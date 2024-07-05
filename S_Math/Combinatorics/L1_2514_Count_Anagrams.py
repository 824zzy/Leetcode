""" https://leetcode.com/problems/count-anagrams/
It is obvious that the answer is the product of the number of unique permutations for each word in a sentence.
The last one is just the number of permutations of all letters (treating same letters as distinct, i.e. n!) corrected (divided) by the number of permutations within each group of same letters.
"""
from header import *


class Solution:
    def countAnagrams(self, s: str) -> int:
        ans = 1
        for w in s.split():
            cnt = Counter(w)
            n = factorial(cnt.total())
            for c in cnt.values():
                n //= factorial(c)
            ans *= n
        return ans % (10 ** 9 + 7)

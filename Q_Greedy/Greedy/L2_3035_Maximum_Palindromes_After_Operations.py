""" https://leetcode.com/problems/maximum-palindromes-after-operations/
Observation:
    1. For odd-length palindrome, any character can be placed in the middle ==> **Fill the middle at the end**
    2. prioritize the shorter strings to fill the palindrome

"""
from header import *


class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        # count pairs that can fill half of the palindrome
        cnt = Counter(c for w in words for c in w)
        pairs = sum(v // 2 for v in cnt.values())

        # fill the strings from the shortest to the longest
        A = sorted(map(len, words))
        for i, a in enumerate(A):
            pairs -= a // 2
            if pairs < 0:
                return i
        return len(A)

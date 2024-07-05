""" https://leetcode.com/problems/count-vowel-strings-in-ranges/
prefix sum to count the number of words that start and end with vowels
"""
from header import *


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        A = [1 if w[0] in "aeiou" and w[-1] in "aeiou" else 0 for w in words]
        A = list(accumulate(A, initial=0))
        ans = []
        for i, j in queries:
            ans.append(A[j + 1] - A[i])
        return ans

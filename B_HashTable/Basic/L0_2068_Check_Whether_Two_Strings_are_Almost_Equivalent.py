""" https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/
use frequency table to check if all the elements appear less than 4
"""


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freq = [0] * 26
        for x in word1:
            freq[ord(x) - 97] += 1
        for x in word2:
            freq[ord(x) - 97] -= 1
        return all(abs(x) <= 3 for x in freq)

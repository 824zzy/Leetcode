""" https://leetcode.com/problems/unique-number-of-occurrences/
"""


class Solution:
    def uniqueOccurrences(self, A: List[int]) -> bool:
        return len(Counter(A).values()) == len(set(Counter(A).values()))

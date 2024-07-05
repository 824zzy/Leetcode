""" https://leetcode.com/problems/number-of-distinct-binary-strings-after-applying-operations/
For each 'i', we can choose to flip or not flip it, totally 2^(len(s)-k+1) ways.
"""


class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        n = len(s) - k + 1
        return 2 ** n % (10 ** 9 + 7)


"""
"1001"
3
"10110"
5
"00000011001011"
2
"""

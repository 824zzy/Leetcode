""" https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/
greedily find maximum digit in the number
"""
class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(x))
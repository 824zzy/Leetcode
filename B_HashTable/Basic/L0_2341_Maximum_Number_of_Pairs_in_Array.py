""" https://leetcode.com/problems/maximum-number-of-pairs-in-array/
simulation by counter
"""


class Solution:
    def numberOfPairs(self, A: List[int]) -> List[int]:
        cnt = Counter(A)
        a, b = 0, 0
        for k, v in cnt.items():
            a += v // 2
            b += v % 2
        return [a, b]

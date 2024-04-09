""" https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/
check if n divisible by 3
"""


class Solution:
    def sumOfThree(self, n: int) -> List[int]:
        if n % 3 == 0:
            return [n // 3 - 1, n // 3, n // 3 + 1]
        else:
            return []

""" https://leetcode.com/problems/number-of-employees-who-met-the-target/
reading comprehension
"""


class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], t: int) -> int:
        return sum(h >= t for h in hours)

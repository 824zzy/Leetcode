""" https://leetcode.com/problems/calculate-delayed-arrival-time/
it should be level -1
"""
class Solution:
    def findDelayedArrivalTime(self, a: int, d: int) -> int:
        return (a+d)%24
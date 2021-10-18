""" L0: https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/
Sort two array
"""
class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        return sum([abs(i-j) for i, j in zip(sorted(seats), sorted(students))])
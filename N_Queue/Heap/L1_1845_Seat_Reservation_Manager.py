""" https://leetcode.com/problems/seat-reservation-manager/
initialize a heap with n and simulate the process of seat reservation
"""
class SeatManager:
    def __init__(self, n: int):
        self.pq = list(range(1, n+1))

    def reserve(self) -> int:
        return heappop(self.pq)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.pq, seatNumber)

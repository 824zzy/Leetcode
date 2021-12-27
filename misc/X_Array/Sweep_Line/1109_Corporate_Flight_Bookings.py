""" L1: https://leetcode.com/problems/corporate-flight-bookings/
Set the change of seats for each day.
If booking = [i, j, k],
it needs k more seat on ith day,
and we don't need these seats on j+1th day.
We accumulate these changes then we have the result that we want.
"""
class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cnt = [0] * (n+1)
        for i, j, k in bookings:
            cnt[i-1] += k
            cnt[j] -= k
        for i in range(1, n):
            cnt[i] += cnt[i-1]
        return cnt[:-1]
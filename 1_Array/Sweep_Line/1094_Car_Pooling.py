""" L1: https://leetcode.com/problems/car-pooling/
Find the maximum passengers at each point by sweep line.
"""
class Solution:
    def carPooling(self, trips: List[List[int]], c: int) -> bool:
        n = max([k for i, j, k in trips])
        cnt = [0] * (n+1)
        for k, i, j in trips:
            cnt[i] += k
            cnt[j] -= k
        for i in range(1, n):
            cnt[i] += cnt[i-1]
        return all([n<=c for n in cnt[:-1]])
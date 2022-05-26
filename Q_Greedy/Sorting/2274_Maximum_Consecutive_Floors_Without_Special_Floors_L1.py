""" https://leetcode.com/problems/maximum-consecutive-floors-without-special-floors/
Greedily find consecutive floors by sorting, be careful to the edge floors.
"""
class Solution:
    def maxConsecutive(self, b: int, t: int, A: List[int]) -> int:
        A = [b-1]+A+[t+1]
        A.sort()
        
        ans = 0
        for i in range(1, len(A)):
            ans = max(ans, (A[i]-1)-A[i-1])
        return ans
""" https://leetcode.com/problems/maximum-units-on-a-truck/
greedily assign the most valuable item to the truck
"""
class Solution:
    def maximumUnits(self, A: List[List[int]], n: int) -> int:
        A.sort(key=lambda x: -x[1])
        ans = 0
        for i in range(len(A)):
            x = min(n, A[i][0])
            ans += A[i][1]*x
            n -= x
            if not n: break
        return ans
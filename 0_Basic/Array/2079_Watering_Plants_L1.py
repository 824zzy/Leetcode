""" https://leetcode.com/problems/watering-plants/
simulation
"""
class Solution:
    def wateringPlants(self, P: List[int], C: int) -> int:
        ans = 0
        c = C
        for i, p in enumerate(P):
            if c<p:
                ans += 2*i
                c = C
            ans += 1
            c -= p
        return ans
            
        
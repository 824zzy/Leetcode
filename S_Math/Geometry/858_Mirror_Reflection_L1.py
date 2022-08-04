""" https://leetcode.com/problems/mirror-reflection/
draw the image that flips the room following the light
1. the x-axis and y-axis flipping counts can be found by least common multiple
2. the pattern can be easily found.
"""
class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        n = lcm(p, q)
        x = n//q
        y = n//p
        if y%2==0: return 0
        if x%2==0: return 2
        else: return 1
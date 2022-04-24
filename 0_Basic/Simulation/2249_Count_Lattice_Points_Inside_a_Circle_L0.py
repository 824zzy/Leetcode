""" https://leetcode.com/problems/count-lattice-points-inside-a-circle/
Since circle length is less than 200, so just brute force to find all distinct points
Time: O(n^3)
"""
class Solution:
    def countLatticePoints(self, A: List[List[int]]) -> int:
        ans = set()
        for c in A:
            x, y, r = c[0], c[1], c[2]
            for xx in range(x-r, x+r+1):
                for yy in range(y-r, y+r+1):
                    if (x-xx)**2+(y-yy)**2<=r**2:
                        ans.add((xx, yy))
        return len(ans)
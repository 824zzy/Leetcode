""" https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/
since n<=500, we can easily brute force on all the query-point pairs

Time: O(n^2)
"""
class Solution:
    def countPoints(self, P: List[List[int]], Q: List[List[int]]) -> List[int]:
        ans = []
        for x, y, r in Q:
            cnt = 0
            for xx, yy in P:
                if (xx-x)**2+(yy-y)**2<=r**2: cnt += 1
            ans.append(cnt)
        return ans
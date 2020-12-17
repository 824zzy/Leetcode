class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort(key=lambda x: x[1])
        r = float('-inf')
        for p in points:
            if p[0]>r:
                r = p[1]
                ans += 1
        return ans
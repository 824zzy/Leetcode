""" direct idea based on defaultdict
"""
from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        abs_dis = defaultdict()
        for point in points:
            t = 0
            for val in point:
                t += val**2
            if t not in abs_dis:
                abs_dis[t] = [point]
            else:
                abs_dis[t].append(point)

        sorted_dis = sorted(abs_dis.items())
        ans = []
        for i, (k, v) in enumerate(sorted_dis):
            for p in v:
                ans.append(p)
                K -= 1
            if K == 0:
                break     
        return ans

""" More tricky way with lambda expression
"""
class Solution:
    def kClosest(self, points: List[List[int]], K:int) -> List[List[int]]:
        distance = sorted(points, key=lambda x: x[0]^2+x[1]^2)
        return distance[:K]
        


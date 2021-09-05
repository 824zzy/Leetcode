""" L3: Monotone chain convex hull
TODO: https://leetcode.com/problems/erect-the-fence/discuss/103306/C%2B%2B-and-Python-easy-wiki-solution
"""
class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:
        points = sorted(map(tuple, points), key=lambda x:(x[0], x[1]))
        
        def sign(o, a, b):
            return (a[0]-o[0]) * (b[1]-o[1]) - (b[0]-o[0]) * (a[1]-o[1])
        
        def build(points):
            hull = []
            for p in points:
                while len(hull) >= 2 and sign(hull[-2], hull[-1], p) < 0:
                    hull.pop()
                hull += p,
            return hull
        
        return list(set(build(points) + build(points[::-1])))
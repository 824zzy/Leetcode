"""
Compute the distances between every two points.
If two points overlap or the frequency of length more than three,
then the four points can not form a square.
"""
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(pt1, pt2):
            return (pt1[0]-pt2[0])**2+(pt1[1]-pt2[1])**2
        points = [p1, p2, p3, p4]
        dists = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                d = distance(points[i], points[j])
                # If two points overlapped
                if d==0: 
                    return False
                else:
                    dists.append(d)
        # only side of length and diagnal have the same length
        return len(set(dists))==2
""" https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/
notice that width(10^9) is way greater than height(100), so
1. store all the points in hash table
2. binary search on the width to find the number of rectangles that conver the point
"""


class Solution:
    def countRectangles(self, A: List[List[int]], P: List[List[int]]) -> List[int]:
        sd = defaultdict(list)
        for i, j in sorted(A):
            sd[j].append(i)

        ans = []
        for x, y in P:
            cnt = 0
            for yy, xxs in sd.items():
                if yy >= y:
                    cnt += len(xxs) - bisect_right(xxs, x - 1)
            ans.append(cnt)
        return ans

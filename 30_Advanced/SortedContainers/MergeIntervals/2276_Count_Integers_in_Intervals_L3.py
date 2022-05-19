""" https://leetcode.com/problems/count-integers-in-intervals/
learn a lot from the nice solution from ye: 
https://leetcode.com/problems/count-integers-in-intervals/discuss/2040175/Python3-SortedList
"""
from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.cnt = 0 
        self.A = SortedList()

    def add(self, left: int, right: int) -> None:
        k = self.A.bisect_left((left, right))

        while k<len(self.A) and self.A[k][0]<=right: 
            l, r = self.A.pop(k)
            self.cnt -= r - l + 1
            right = max(right, r)

        if k and left<=self.A[k-1][1]: 
            l, r = self.A.pop(k-1)
            self.cnt -= r - l + 1
            left = l
            right = max(right, r)

        self.cnt += right - left + 1
        self.A.add((left, right))

    def count(self) -> int:
        return self.cnt
        
"""
["CountIntervals","add","add","count","add","count"]
[[],[2,3],[7,10],[],[5,8],[]]
["CountIntervals","count","add","add","count","count","add"]
[[],[],[39,44],[13,49],[],[],[47,50]]
["CountIntervals","count","add","add","add","add","add","count","add","add"]
[[],[],[8,43],[13,16],[26,33],[28,36],[29,37],[],[34,46],[10,23]]
["CountIntervals","add","add","add","add","add","add","count"]
[[],[10,27],[46,50],[15,35],[12,32],[7,15],[49,49],[]]
["CountIntervals","count","add","add","count","count","add","add","add","count"]
[[],[],[33,49],[43,47],[],[],[37,37],[26,38],[11,11],[]]
"""

"""
[null, null, null, 6, null, 8]
[null,0,null,null,37,37,null]
[null,0,null,null,null,null,null,36,null,null]
[null,null,null,null,null,null,null,34]
[null,0,null,null,17,17,null,null,null,25]
"""
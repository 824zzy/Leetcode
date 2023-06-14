""" https://leetcode.com/problems/snapshot-array/
hashmap + binary search
"""
from header import *

class SnapshotArray:
    def __init__(self, l: int):
        self.A = defaultdict(list)
        self.idx = 0
        
    def set(self, index: int, val: int) -> None:
        self.A[index].append((self.idx, val))

    def snap(self) -> int:
        x = self.idx
        self.idx += 1
        return x

    def get(self, index: int, snap_id: int) -> int:
        k = bisect_right(self.A[index], (snap_id, inf))
        if k==0: return 0
        return self.A[index][k-1][1]
        

"""
["SnapshotArray","set","snap","set","get"]
[[3],[0,5],[],[0,6],[0,0]]
["SnapshotArray","snap","snap","get","set","snap","set"]
[[4],[],[],[3,1],[2,4],[],[1,4]]
["SnapshotArray","snap","get","get","set","get","set","get","set"]
[[2],[],[1,0],[0,0],[1,8],[1,0],[0,20],[0,0],[0,7]]
"""
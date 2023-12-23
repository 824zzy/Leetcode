""" https://leetcode.com/problems/matrix-similarity-after-cyclic-shifts/
don't think too much, just simulate
"""
from header import *

class Solution:
    def areSimilar(self, A: List[List[int]], k: int) -> bool:
        n = len(A[0])
        for i, row in enumerate(A):
            for i, x in enumerate(row):
                if i&1:
                    if x!=row[(i+k)%n]:
                        return False
                else:
                    if x!=row[(i-k)%n]:
                        return False
        return True
                
    
"""
[[1,2,1,2],[5,5,5,5],[6,3,6,3]]
2
[[2,2],[2,2]]
3
[[1,2]]
1
[[4,9,10,10],[9,3,8,4],[2,5,3,8],[6,1,10,4]]
5
[[10,6,10,6,10,6,10,6]]
4
[[7,7],[10,10],[4,4]]
2
[[9,10,10,6,6,8,10,7,10,9],[10,6,1,10,10,5,7,9,9,2],[8,5,8,3,5,2,2,9,7,10]]
20
[[8,1,10,5,2,8]]
1
"""
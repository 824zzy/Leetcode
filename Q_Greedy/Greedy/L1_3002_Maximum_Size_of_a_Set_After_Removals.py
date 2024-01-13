""" https://leetcode.com/problems/maximum-size-of-a-set-after-removals/
greedy + categorization?
"""
from header import *

class Solution:
    def maximumSetSize(self, A: List[int], B: List[int]) -> int:
        a, b = len(A)//2, len(B)//2
        cntA, cntB = Counter(A), Counter(B)
        # try to delete redundant element from A
        for k, v in cntA.items():
            if v>1:
                x = min(a, v-1)
                cntA[k] -= x
                a -= x
        # try to delete redundant element from B
        for k, v in cntB.items():
            if v>1:
                x = min(b, v-1)
                cntB[k] -= x
                b -= x
        # when don't need to delete extra element, return union set
        if a==0 and b==0:
            return len(set(cntA.keys()) | set(cntB.keys()))
        else:
            all = set(cntA.keys()) | set(cntB.keys())
            # delete intersection then see how many remained need to be deleted
            inter = set(cntA.keys()) & set(cntB.keys())
            rem = (a+b)-len(inter)
            return len(all)-max(rem, 0)
                                           
        
        
"""
[1,2,1,2]
[1,1,1,1]
[1,2,3,4,5,6]
[2,3,2,3,2,3]
[1,1,2,2,3,3]
[4,4,5,5,6,6]
[8,9]
[4,3]
[1,2,3,4,5,6]
[1,2,3,4,5,6]
[1,3,3,2]
[2,2,1,3]
"""
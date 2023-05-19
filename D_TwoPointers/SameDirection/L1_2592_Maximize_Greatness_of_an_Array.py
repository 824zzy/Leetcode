""" https://leetcode.com/problems/maximize-greatness-of-an-array/
1. sort the array
2. greedily permute the elements from small to large
"""
from header import *

class Solution:
    def maximizeGreatness(self, A: List[int]) -> int:
        A.sort()
        i = 0
        for j in range(len(A)):
            if A[j]>A[i]:
                i += 1
        return i
    

# or use groupby to find the max length of same elements
class Solution:
    def maximizeGreatness(self, A: List[int]) -> int:
        ans = len(A)
        return ans-max(Counter(A).values())
    
"""
[1,3,5,2,1,3,1]
[1,1,1,2,3,3,5]
[1,2,3,4]
[1,2,3,4,5,6,7,8,9,10]
[42,8,75,28,35,21,13,21]
[1,1,0,1,5,0]
"""
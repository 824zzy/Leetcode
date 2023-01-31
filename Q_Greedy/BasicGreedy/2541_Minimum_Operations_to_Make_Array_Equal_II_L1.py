""" https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/
"""
from header import *

class Solution:
    def minOperations(self, A: List[int], B: List[int], k: int) -> int:
        if k==0: return 0 if A==B else -1
        cnt = 0
        ans = 0
        for a, b in zip(A, B):
            if (a-b)%k!=0: return -1
            if (a-b)//k>0: ans += (a-b)//k
            cnt += (a-b)//k
        return ans if cnt==0 else -1
        
"""
[4,3,1,4]
[1,3,7,1]
3
[3,8,5,2]
[2,4,1,6]
1
[13,6,10,16]
[1,16,12,16]
2
[10,5,15,20]
[20,10,15,5]
0
""" 
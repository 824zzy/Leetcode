""" https://leetcode.com/problems/minimum-cost-to-make-array-equalindromic/
1. greedy median
2. binary search on candidate median
"""

from header import *

cand = list(range(1, 10))
for i in range(1, 10000):
    cand.append(int(str(i)+str(i)[::-1]))
    for j in range(10):
        cand.append(int(str(i)+str(j)+str(i)[::-1]))
cand.append(10**9+7)
cand.sort()
        

class Solution:
    def minimumCost(self, A: List[int]) -> int:
        A.sort()
        x = A[len(A)//2]
        i = bisect_left(cand, x)
        a = cand[i-1]
        b = cand[i]
        return min(sum(abs(x-a) for x in A), sum(abs(x-b) for x in A))
    
    
"""
[1,2,3,4,5]
[10,12,13,14,15]
[22,33,22,33,22]
[25,26,27,28,30]
[1,1]
[1,2345]
[1,100000]
[1,2,100000]
[1,1,2,2,2,10000]
[1,1,1,40004]
[101,104,107,126,130]
[1286,8013,9939,8605,5340,4902,9245,4481,6776,7669,4908,8528,9718,5484,3350,8001,7604,4547,5435,9864,2438]
"""
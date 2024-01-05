""" https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/
greedy median + prefix sum + sliding window

1. prerequisite: median is the best option for the elements in an array become equal
2. convert the problem into find a subarray that sum less than the median of subarray ==> sliding window
"""
from header import *

class Solution:
    def maxFrequencyScore(self, A: List[int], k: int) -> int:
        def valid(l, r):
            m = (l+r)//2
            t = A[m]
            
            left = t*(m+1-l) - (pre[m+1]-pre[l])
            right = (pre[r+1]-pre[m]) - t*(r+1-m)
            return left+right<=k
            
        A.sort()
        pre = list(accumulate(A, initial=0))
        
        i = 0
        ans = 0
        for j, x in enumerate(A):
            while not valid(i, j):
                i += 1
            ans = max(ans, j-i+1)
        return ans
    
    
"""
[1,2,6,4]
3
[1,4,4,2,4]
0
[27,8,30,3,13,28,7,14,21,19,24,28,29,1,14,22,6]
23
"""
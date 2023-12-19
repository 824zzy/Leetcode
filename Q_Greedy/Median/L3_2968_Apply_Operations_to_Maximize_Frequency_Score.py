""" https://leetcode.com/problems/apply-operations-to-maximize-frequency-score/
"""
from header import *

class Solution:
    def maxFrequencyScore(self, A: List[int], k: int) -> int:
        def fn(x):
            # return False if exist a subarray that length is x and elements are the sames within k ops.
            print('--')
            print(x)
            for i in range(x, len(pre)):
                if x&1:
                    med = A[i-x//2]
                else:
                    med = (A[i-x//2-1] + A[i-x//2]) // 2
                print(pre[i]-pre[i-x], med, (pre[i]-pre[i-x]) - x*med <= k)
                if x*med - (pre[i]-pre[i-x]) <= k:
                    return False
            return True
            
            
        A.sort()
        print(A)
        pre = list(accumulate(A, initial=0))
        print(pre)
        l, r = 0, len(pre)
        while l<r:
            m = (l+r)//2
            if fn(m):
                r = m
            else:
                l = m+1
        return l-1
    
    
"""
[1,2,6,4]
3
[1,4,4,2,4]
0
"""
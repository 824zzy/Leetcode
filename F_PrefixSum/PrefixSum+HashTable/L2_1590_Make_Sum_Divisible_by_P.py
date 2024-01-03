""" https://leetcode.com/problems/make-sum-divisible-by-p/
1. (sum - subarray) % p = 0 
    ==> subarray % p = sum % p ; 
    ==> (prefixsum[r] - prefixsum[l]) % p = sum % p 
    ==> prefixsum[r]%p - sum % p = prefixsum[l]%p
2. convert the problem into: find prefix sum that 
"""
from header import *

class Solution:
    def minSubarray(self, A: List[int], p: int) -> int:
        cnt = {}
        cnt[0] = -1
        
        ans = inf
        pre = 0
        t = sum(A)%p
        if t==0: # [1,2,3] p=3
            return 0
        for i, x in enumerate(A):
            pre = (pre+x)%p
            if (pre-t)%p in cnt:
                ans = min(ans, i-cnt[(pre-t)%p])
            cnt[pre%p] = i
        return ans if ans<len(A) else -1
    
"""
[3,1,4,2]
6
[6,3,5,2]
9
[1,2,3]
3
[1,2,3]
7
"""
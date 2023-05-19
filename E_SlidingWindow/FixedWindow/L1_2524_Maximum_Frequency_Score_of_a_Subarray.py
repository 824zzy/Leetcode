""" https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/
The idea is not complex, but the implementation is tricky.

Maintain a fixed sliding window of size k, and update the score of the window by hash table.
To avoid TLE, we need to use pow(x, y, mod).
"""
from header import *

class Solution:
    def maxFrequencyScore(self, A: List[int], k: int) -> int:
        ans = 0
        sm = 0
        mod = 10**9+7
        cnt = Counter()
        for i, x in enumerate(A):
            sm -= pow(x, cnt[x], mod) if cnt[x] else 0
            cnt[x] += 1
            sm += pow(x, cnt[x], mod)
            if i>=k-1:
                ans = max(ans, sm%mod)
                sm -= pow(A[i-k+1], cnt[A[i-k+1]], mod)
                cnt[A[i-k+1]] -= 1
                sm += pow(A[i-k+1], cnt[A[i-k+1]], mod) if cnt[A[i-k+1]] else 0
        return ans%mod
                
    
"""
[1,1,1,2,1,2]
3
[1,1,1,1,1,1]
4
[29,29,5,5,27,27,27,27,23,14,14,15,15,15,15,15,15,15]
2
[29,30,30,31]
2
[122,122,122,122,165,122,162,122,122,122,122,165,122,122,122,122,122,182,182,132,122,122,122,122,140,54,180,168,122,122,122,18,33,122,122,54,122,122,120,131,85,122,67,122,54,180,168,188,122,57,18,57,122,131,122]
25
"""
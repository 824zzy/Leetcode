""" https://leetcode.com/problems/count-subarrays-with-median-k/description/
A subarray has a median k if:
1. It includes k
2. Count n[i] < k is equal to count n[i] > k (odd-size subarrays).
3. Count n[i] < k is one less than count n[i] > k (even-size subarrays).
"""
from header import *

class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        def find(i, k):
            L = Counter()
            cnt = 0
            for ii in reversed(range(i+1)):
                if A[ii]<k: cnt += 1
                else: cnt -= 1
                L[cnt] += 1
            
            R = Counter()
            cnt = 0
            for ii in range(i, len(A)):
                if A[ii]>k: cnt += 1
                else: cnt -= 1
                R[cnt] += 1

            ans = 0
            for k, v in L.items():
                if k in R:
                    ans += v*R[k]
                if k+1 in R:
                    ans += v*R[k+1]
            return ans
                    
        ans = 0
        for i in range(len(A)):
            if A[i]==k:
                ans += find(i, k)
        return ans
    
""" 3 1 4
[3,2,1,4,5]
4
[2,3,1]
3
[1,2,3,4]
2
"""
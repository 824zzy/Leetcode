""" L1
Change up to k = 1 values from 0 to 1.
Return the length - 1 of the longest (contiguous) subarray that contains only 1s.
"""
class Solution:
    def longestSubarray(self, A):
        k, i, ans = 1, 0, 0
        for j in range(len(A)):
            if A[j] == 0:
                k -= 1
                if k<0:
                    if A[i]==0: k += 1
                    while A[i]==1: i += 1
                    i += 1
            ans = max(ans, j-i)
        return ans
    
# Lee's brillant solution
class Solution:
    def longestSubarray(self, A):
        k = 1
        i = 0
        for j in range(len(A)):
            if A[j] == 0: k -= 1
            if k < 0:
                if A[i] == 0: k += 1
                i += 1
        return j - i
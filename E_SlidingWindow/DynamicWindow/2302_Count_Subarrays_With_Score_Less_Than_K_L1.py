""" https://leetcode.com/problems/count-subarrays-with-score-less-than-k/
maintain sliding window by sum * length must less than k
"""
class Solution:
    def countSubarrays(self, A: List[int], k: int) -> int:
        i = 0
        ans = 0
        sm = 0
        
        for j in range(len(A)):
            sm += A[j]
            while sm*(j-i+1)>=k:
                sm -= A[i]
                i += 1
            ans += j-i+1
        return ans
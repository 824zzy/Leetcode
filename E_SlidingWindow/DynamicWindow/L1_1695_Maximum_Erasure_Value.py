""" https://leetcode.com/problems/maximum-erasure-value/
"""
class Solution:
    def maximumUniqueSubarray(self, A: List[int]) -> int:
        i = 0
        ans = 0
        seen = set()
        sm = 0
        
        for j in range(len(A)):
            while A[j] in seen:
                seen.remove(A[i])
                sm -= A[i]
                i += 1
            seen.add(A[j])
            sm += A[j]
            ans = max(sm, ans)
        return ans
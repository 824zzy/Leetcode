""" https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/
sort the capacity and rocks by difference, then greedily assign additional rocks
"""
class Solution:
    def maximumBags(self, C: List[int], R: List[int], r: int) -> int:
        A = list(zip(C, R))
        A.sort(key=lambda x: x[0]-x[1])
        
        ans = 0
        for i in range(len(A)):
            if A[i][0]-A[i][1]<=r:
                r -= A[i][0]-A[i][1]
                ans += 1
            else: return ans
        return ans
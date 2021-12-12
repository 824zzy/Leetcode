""" https://leetcode.com/problems/sum-of-subarray-ranges/
TODO: understand the monotonic stack method
"""
class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0 
        stack = []
        for i, x in enumerate([-inf] + nums + [-inf]): 
            while stack and stack[-1][1] > x: 
                ii, xx = stack.pop()
                lo = stack[-1][0]
                ans -= xx * (i-ii) * (ii-lo)
            stack.append((i, x))
        
        stack = []
        for i, x in enumerate([inf] + nums + [inf]): 
            while stack and stack[-1][1] < x: 
                ii, xx = stack.pop()
                lo = stack[-1][0]
                ans += xx * (i-ii) * (ii-lo)
            stack.append((i, x))
        return ans 
    
# O(N^2)
class Solution:
    def subArrayRanges(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            ma, mi = -inf, inf
            for j in range(i, len(A)):
                ma, mi = max(ma, A[j]), min(mi, A[j])
                ans += ma-mi
        return ans
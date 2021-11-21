""" https://leetcode.com/problems/two-furthest-houses-with-different-colors/
at least one of the end points will be used for furthest pairs.
"""
# O(n)
class Solution:
    def maxDistance(self, A: List[int]) -> int:
        ans = 0
        for i, x in enumerate(A):
            if x!=A[0]: ans = max(ans, i)
            if x!=A[-1]: ans = max(ans, len(A)-1-i)
        return ans

# brute force
class Solution:
    def maxDistance(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                if A[i]!=A[j]: ans = max(ans, j-i)
        return ans
""" https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/
linear scan, find k-distant left and right end points for each i-th element
"""
class Solution:
    def findKDistantIndices(self, A: List[int], key: int, k: int) -> List[int]:
        ans = []
        for i in range(len(A)):
            for j in range(max(0, i-k), min(len(A), i+k+1)):
                if A[j]==key:
                    ans.append(i)
                    break
        return ans
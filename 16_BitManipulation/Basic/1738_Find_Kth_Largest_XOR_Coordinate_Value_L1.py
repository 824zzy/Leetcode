""" https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
1. build prefix-XOR 2D matrix
2. find kth largest in prefix-XOR matrix
"""
class Solution:
    def kthLargestValue(self, A: List[List[int]], k: int) -> int:
        ans = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i: A[i][j] ^= A[i-1][j]
                if j: A[i][j] ^= A[i][j-1]
                if i and j: A[i][j] ^= A[i-1][j-1]
                ans.append(A[i][j])
        return sorted(ans, reverse=True)[k-1]
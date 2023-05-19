""" https://leetcode.com/problems/find-kth-largest-xor-coordinate-value/
1. build prefix-XOR 2D matrix
2. find kth largest in prefix-XOR matrix by quick select
"""
class Solution:
    def kthLargestValue(self, A: List[List[int]], k: int) -> int:
        prefix = []
        for i in range(len(A)):
            for j in range(len(A[0])):
                if i: A[i][j] ^= A[i-1][j]
                if j: A[i][j] ^= A[i][j-1]
                if i and j: A[i][j] ^= A[i-1][j-1]
                prefix.append(A[i][j])
        
        A = prefix
        def partition(l, r): 
            """Return partition of A[l:r]."""
            i, j = l+1, r-1
            while i <= j: 
                if A[i] < A[l]: i += 1
                elif A[j] > A[l]: j -= 1
                else: 
                    A[i], A[j] = A[j], A[i]
                    i, j = i+1, j-1
            A[l], A[j] = A[j], A[l]
            return j
        
        shuffle(A)
        l, r = 0, len(A)
        while True: 
            m = partition(l, r)
            if m+k < len(A): l = m + 1
            elif m+k == len(A): return A[m]
            else: r = m
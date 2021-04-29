class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        A.sort()
        i = 0
        for j in range(len(A)):
            k += A[j]
            # valid condition: max*size <= k+sum
            if k < A[j]*(j-i+1):
                k -= A[i]
                i += 1
        return j-i+1
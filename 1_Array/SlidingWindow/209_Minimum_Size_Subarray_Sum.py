""" L0
the k is given, just follow the template to solve this problem.
"""
class Solution:
    def minSubArrayLen(self, k: int, A: List[int]) -> int:
        ans, i = float('inf'), 0
        for j in range(len(A)):
            k -= A[j]
            while k<=0:
                ans = min(ans, j-i+1)
                k += A[i]
                i += 1
        return ans if ans!=float('inf') else 0
""" https://leetcode.com/problems/number-of-arithmetic-triplets/
"""
class Solution:
    def arithmeticTriplets(self, A: List[int], diff: int) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(i+1, len(A)):
                for k in range(j+1, len(A)):
                    if A[j]-A[i]==A[k]-A[j]==diff:
                        ans += 1
        return ans
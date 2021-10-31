""" L1: https://leetcode.com/problems/3sum/
repeated two sum by hash table, remove duplicate by `if i and A[i-1]==A[i]: continue`
"""
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()      
        ans = []
        for i in range(len(A)):
            if A[i]>0: break
            if i and A[i-1]==A[i]: continue
            t = -A[i]
            M = {}
            for j in range(i+1, len(A)):
                if A[j] in M:
                    if not M[A[j]]:
                        ans.append([A[i], t-A[j], A[j]])
                        M[A[j]] += 1
                else: M[t-A[j]] = 0
        return ans
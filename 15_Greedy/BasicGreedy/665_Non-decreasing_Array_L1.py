""" https://leetcode.com/problems/non-decreasing-array/
1. count modify times and check if it less or equal than 1
2. once find any incorrect order, instantly return False
"""
class Solution:
    def checkPossibility(self, A: List[int]) -> bool:
        cnt = 0
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                if (i==0 or A[i-1]<=A[i+1]) or (i+2==len(A) or A[i]<=A[i+2]):
                    cnt += 1
                else: # (3 2(A[i]) 1) and (3(A[i]) 2 1) are incorrect orders
                    return False
        return cnt<=1
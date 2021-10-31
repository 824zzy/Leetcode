""" L1: https://leetcode.com/problems/3sum/
repeated two sum by two pointers, remove duplicate by `if i and A[i-1]==A[i]: continue`
"""
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()      
        ans = []
        for i in range(len(A)):
            if A[i]>0: break
            if i and A[i-1]==A[i]: continue
            l, r = i+1, len(A)-1
            while l<r:
                cur_s = A[i]+A[l]+A[r]
                if cur_s>0: r -= 1
                elif cur_s<0: l += 1
                else:
                    ans.append([A[i], A[l], A[r]])
                    l += 1
                    while l<r and A[l-1]==A[l]: l += 1
        return ans
""" https://leetcode.com/problems/3sum/
classic 3-sum, two pointers or hash table
"""
from header import *

class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        A.sort()
        ans = set()
        n = len(A)
        for i in range(n):
            l, r = i+1, n-1
            while l<r:
                if A[i]+A[l]+A[r]>0:
                    r -= 1
                elif A[i]+A[l]+A[r]<0:
                    l += 1
                else:
                    ans.add(tuple([A[i], A[l], A[r]]))
                    l += 1
                    r -= 1
        return ans
    
"""
non-sort solution using hash table
nums[i] + nums[j] + nums[k] == 0
==> nums[i] + nums[j] == -nums[k]
"""
class Solution:
    def threeSum(self, A: List[int]) -> List[List[int]]:
        ans = set()
        for i in range(len(A)):
            # remove duplicate
            if i and A[i]==A[i-1]:
                continue
            seen = defaultdict(set)
            for j in range(i+1, len(A)):
                if seen[-A[j]]:
                    ans.add(tuple(sorted([A[i], A[j], -A[i]-A[j]])))
                seen[A[i]+A[j]].add(A[j])
        return ans
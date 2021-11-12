""" L1: https://leetcode.com/problems/next-greater-element-i/
build a next greater hash table by monotonic decreasing stask.
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        S, M = [], {}
        for n in nums2:
            while S and n>S[-1]: 
                M[S.pop()] = n
            S.append(n)
        return [M[n] if n in M else -1 for n in nums1]
    
    
# brute force solution
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N = {}
        for i in range(len(nums2)):
            for j in range(i+1, len(nums2)):
                if nums2[i]<nums2[j]:
                    N[nums2[i]] = nums2[j]
                    break
        return [N[n] if n in N else -1 for n in nums1]
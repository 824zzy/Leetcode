""" https://leetcode.com/problems/wiggle-sort-ii/
1. sort the array for preparing greedy
2. to make sure the wiggle attribute we put reversed first half in even indexes and reversed second half in odd indexes
For example, [1,2,3,4,5,6] ==> [3,6,2,5,1,4]
"""
class Solution:
    def wiggleSort(self, A: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        A.sort()
        n = len(A)
        A[::2], A[1::2] = A[:(n+1)//2][::-1], A[(n+1)//2:][::-1]
                
                
"""
[1,5,1,1,6,4]
[1,3,2,2,3,1]
[1,1,2,1,2,2,1]
[4,5,5,6]
"""
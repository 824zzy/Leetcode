""" https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/
there are multiple ways to solve this problem
"""
# [1,2,3,4,5,6] ==> [1,6,2,5,3,4]
class Solution:
    def rearrangeArray(self, A: List[int]) -> List[int]:
        A.sort()
        n = len(A)
        ans = [0]*len(A)
        for i in range(len(A)):
            if i&1: ans[i] = A[(-i-1)//2]
            else: ans[i] = A[i//2]
        return ans

# solve it as /Q_Greedy/Sorting/324_Wiggle_Sort_II_L1.py
# [1,2,3,4,5,6] ==> [3,6,2,5,1,4]
class Solution:
    def rearrangeArray(self, A: List[int]) -> List[int]:
        A.sort()
        n = len(A)
        A[::2], A[1::2] = A[:(n+1)//2][::-1], A[(n+1)//2:][::-1]
        return A
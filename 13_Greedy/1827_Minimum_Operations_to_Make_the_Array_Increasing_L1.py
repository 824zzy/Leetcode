"""Description
Author: your name
Date: 2021-12-19 03:59:31
LastEditTime: 2021-12-19 04:04:15
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: /Leetcode/0_Basic/Array/1827_Minimum_Operations_to_Make_the_Array_Increasing_L1.py
"""
class Solution:
    def minOperations(self, A: List[int]) -> int:
        ans = 0
        for i in range(1, len(A)):
            if A[i-1]>=A[i]:
                ans += A[i-1]-A[i]+1
                A[i] = A[i-1]+1
        return ans
"""Description
Author: your name
Date: 2021-05-11 19:36:05
LastEditTime: 2021-05-11 19:38:03
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /Leetcode/1_Array/SlidingWindow/Fixed_Window/1423_Maximum_Points_You_Can_Obtain_From_Cards_L1.py
"""
class Solution:
    def maxScore(self, A: List[int], k: int) -> int:
        win = sum(A[:k])
        ans = win
        for i in range(k):
            win -= A[k-(i+1)] 
            win += A[-(i+1)]
            ans = max(win, ans)
        return ans
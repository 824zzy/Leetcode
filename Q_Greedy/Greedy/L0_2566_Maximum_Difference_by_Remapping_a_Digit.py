""" https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/submissions/
greedy simulation
"""
class Solution:
    def minMaxDifference(self, A: int) -> int:
        A = str(A)
        mx = A
        for i in range(len(A)):
            if A[i]!='9':
                mx = A.replace(A[i], '9')
                break
        mn = A.replace(A[0], '0')
        return int(mx)-int(mn)
        
        
        
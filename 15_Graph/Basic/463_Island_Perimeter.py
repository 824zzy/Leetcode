""" L1
"""
class Solution:
    def islandPerimeter(self, A: List[List[int]]) -> int:
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j]:
                    ans += 4
                    if i>0 and A[i-1][j]: ans -= 2
                    if j>0 and A[i][j-1]: ans -= 2
        return ans
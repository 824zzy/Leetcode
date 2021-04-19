""" 2D prefix sum
"""
class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(1, n): 
                A[i][j] += A[i][j-1]
        
        ans = 0
        for left in range(n):
            for right in range(left, n):
                prefix = Counter()
                prefix[0] = 1
                area = 0
                for y in range(m):
                    if left>0: area += A[y][right] - A[y][left-1]
                    else: area += A[y][right]
                    ans += prefix.get(area-target, 0)
                    prefix[area] = prefix.get(area, 0) + 1
        return ans

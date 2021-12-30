""" https://leetcode.com/problems/burst-balloons/submissions/
Every element in the given list has two roles:
   1. as the element to disappear lastly
   2. as the boundary for the subarray if it will disappear lastly
"""
class Solution:
    def maxCoins(self, A: List[int]) -> int:
        if not A: return 0
        A = [1] + A + [1]
        
        @lru_cache(None)
        def dfs(i, j):
            if i+1>=j: return 0
            return max(dfs(i, k)+dfs(k, j)+A[i]*A[k]*A[j] for k in range(i+1, j))
        
        return dfs(0, len(A)-1)

        
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + [i for i in nums] + [1]
        c = [[0]*len(nums) for _ in range(len(nums))]
        for l in range(1, n+1):
            for i in range(1, n-l+2):
                j = i+l-1
                for k in range(i, j+1):
                    c[i][j] = max(c[i][j], \
                                  c[i][k-1]+nums[i-1]*nums[k]*nums[j+1]+c[k+1][j])
        return c[1][n]
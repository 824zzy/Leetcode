""" L1
From range m*n, indexes are only determined by column number.
"""


class Solution:
    def matrixReshape(self,
                      nums: List[List[int]],
                      r: int,
                      c: int) -> List[List[int]]:
        if r * c > len(nums) * len(nums[0]):
            return nums
        m, n = len(nums), len(nums[0])
        ans = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(m * n):
            ans[int(i / c)][int(i % c)] = nums[int(i / n)][int(i % n)]
        return ans

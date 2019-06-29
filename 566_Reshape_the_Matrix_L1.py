"""
`i/c` to find Raw.
`i%c` to find Column.
"""
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c > len(nums)*len(nums[0]):
            return nums

        ans = [[None for _ in range(c)] for _ in range(r)]
        ori_c = len(nums[0])

        for i in range(m*n):
            ans[int(i/c)][int(i%c)] = nums[int(i/ori_c)][int(i%ori_c)]
    
        return ans
class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c > len(nums)*len(nums[0]):
            return nums
        nr, nc = len(nums), len(nums[0])
        ans = [[None for _ in range(c)] for _ in range(r)]
        for i in range(nr*nc):
            ans[int(i/c)][int(i%c)] = nums[int(i/nc)][int(i%nc)]
        return ans
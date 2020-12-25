class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack, res = [], [-1] * len(nums)
        for i, num in enumerate(nums):              # 2
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
            stack.append(i)
        for i, num in enumerate(nums):              # 3
            while stack and nums[stack[-1]] < num:
                res[stack.pop()] = num
        return res
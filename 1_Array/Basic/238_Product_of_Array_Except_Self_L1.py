class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t, p = [1], 1
        for i in range(1, len(nums)):
            t.append(p*nums[i-1])
            p *= nums[i-1]
            # print(t, p)
        p = nums[-1]
        for j in range(len(nums)-2, -1, -1):
            t[j] *= p
            p *= nums[j]
            # print(t, p)
        return t
            
        
"""
[1, 1, 2, 6]
[24, 12, 8, 6]
"""
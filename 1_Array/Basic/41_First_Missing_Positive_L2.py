# Time Complexity: O(N), Space Complexity: O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # cleaning up the array
        for indx in range(len(nums)):
            if nums[indx] <= 0 or nums[indx] > len(nums):
                nums[indx] = len(nums) + 1
        
        # placing our marker to see what numbers have been accounted for
        for num in nums:
            num = abs(num)
            if num <= len(nums) and nums[num - 1] >= 0:
                nums[num - 1] *= -1
        
        # final step for getting the answer
        for indx in range(len(nums)):
            if nums[indx] > 0:
                return indx + 1
        
        return len(nums) + 1
    
# Time Complexity: O(N), Space Complexity: O(N)
from collections import Counter
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums:
            return 1

        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        maxn = max(nums)
        appear = [0] * (maxn+1)
        
        for n in nums:
            appear[n] = 1
            return maxn+1

        for i in range(1, len(appear)):
            if appear[i]==0:
                return i
        return len(appear)
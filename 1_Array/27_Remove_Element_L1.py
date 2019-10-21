""" Amazon; Array
basic list remove function usage.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)

# A faster solution than above.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        count = 0
        for n in nums:
            if n == val:
                count += 1
        
        for _ in range(count):
            nums.remove(val)
        return len(nums)

# Best solution without built in function
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in nums:
            if i != val:
                nums[index] = i
                index += 1
        return index

"""
3 2 2 3
1 2 
"""
# O(n)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return target in set(nums)
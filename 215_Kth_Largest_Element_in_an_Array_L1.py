""" trivial O(nlog(n)) time complexity and easy understanding solution
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        return nums[k-1]

""" O(n) solution via heapq
"""
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]
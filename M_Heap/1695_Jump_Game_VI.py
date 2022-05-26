""" L2: Heap+DP
Similar to 239 using Heap to reduce time complexity.
"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        if len(nums)==1: return nums[0]
        heap = []
        heapq.heappush(heap, (-nums[0], 0))
        for i in range(1, len(nums) - 1):
            while heap[0][1] < i - k:
                heapq.heappop(heap)
            heapq.heappush(heap, (-(nums[i]-heap[0][0]), i))

        if heap[0][1] < len(nums) - 1 - k:
            heapq.heappop(heap)
        return - heap[0][0] + nums[-1]
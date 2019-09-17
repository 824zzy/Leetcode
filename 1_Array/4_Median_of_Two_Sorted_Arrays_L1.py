# Brute force solution
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums)%2 != 0:
            return nums[len(nums)//2]
        else:
            return (nums[len(nums)//2-1]+nums[len(nums)//2])/2

# Heap solution
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, heap = (len(nums1)+len(nums2))//2, []
        for i in nums1+nums2:
            heapq.heappush(heap, i)
        
        for _ in range(n):
            t = heapq.heappop(heap)
        
        if n==0:
            return heapq.heappop(heap)
        
        if (len(nums1)+len(nums2))%2 != 0:
            return heapq.heappop(heap)
        else:
            return (t+heapq.heappop(heap))/2
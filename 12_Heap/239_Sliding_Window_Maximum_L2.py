import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k==1: return nums
        ans = []
        h = [(-nums[i], i) for i in range(k)]
        heapq.heapify(h)
        for i in range(k-1, len(nums)):
            while h[0][1]<=i-k: heapq.heappop(h)
            heapq.heappush(h, (-nums[i], i))
            ans.append(-h[0][0])
        return ans
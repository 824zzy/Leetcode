# Kadane's Algorithm

A simple idea of Kadane’s algorithm is to **look for all positive contiguous segments of the array** and **keep track of the maximum sum contiguous subarray** among all positive segments. 

## template

``` py
class Solution:
    def maxSubArray(self, A: List[int]) -> int:
        ans, cur = -inf, 0
        for x in A:
            cur = max(0, cur) + x
            ans = max(ans, cur)
        return ans
```
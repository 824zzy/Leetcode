""" https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/
1. maintain max and min priority queues and left most legit index
2. pop elements when absolute difference larger than limit, while update left most index
"""


class Solution:
    def longestSubarray(self, A: List[int], limit: int) -> int:
        mx, mn = [], []
        i = 0
        ans = 0
        for j in range(len(A)):
            heappush(mx, (-A[j], j))
            heappush(mn, (A[j], j))
            while mx and mn and -mx[0][0]-mn[0][0]>limit:
                while mx and mx[0][1]<=i:
                    heappop(mx)
                while mn and mn[0][1]<=i:
                    heappop(mn)
                i += 1
            ans = max(ans, j-i+1)
        return ans

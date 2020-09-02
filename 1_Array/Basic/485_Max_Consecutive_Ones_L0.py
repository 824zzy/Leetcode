class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cnt = 0
        for n in nums:
            if n==1:
                cnt += 1
            else:
                ans = max(ans, cnt)
                cnt = 0
        return max(ans, cnt)
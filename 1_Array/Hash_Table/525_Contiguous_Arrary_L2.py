class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {} # sum: prevIndex
        currSum, ans = 0, 0
        for idx, n in enumerate(nums):
            currSum += 1 if n==1 else -1
            if currSum in prefix:
                ans = max(ans, idx-prefix[currSum])
            else:
                prefix[currSum] = idx
        return ans
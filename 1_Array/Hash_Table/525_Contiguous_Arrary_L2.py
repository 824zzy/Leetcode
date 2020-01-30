class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mp = {0: -1}
        prefix, ans = 0, 0
        for i, n in enumerate(nums):
            if n==1:
                prefix += 1
            else:
                prefix = -1
            if prefix in mp:
                ans = max(ans, i-mp[prefix])
            else:
                mp[prefix] = i
        return ans
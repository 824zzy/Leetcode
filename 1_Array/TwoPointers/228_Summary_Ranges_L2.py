class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
                return []
        if len(nums) == 1:
            return [str(nums[0])]
        l, r = 0, 1
        start = 0
        ans = []
        while r<len(nums):
            if nums[r]-nums[l]>1:
                if start==l:
                    ans.append(str(nums[start]))
                else:
                    ans.append("->".join([str(nums[start]), str(nums[l])]))
                start = r
                l = r
                r = l + 1
            else:
                l += 1
                r += 1        
        if start==l:
            ans.append(str(nums[start]))
        else:
            ans.append("->".join([str(nums[start]), str(nums[l])]))
        return ans
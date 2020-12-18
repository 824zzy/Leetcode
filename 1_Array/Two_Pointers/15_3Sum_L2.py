class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for k in range(len(nums)-2):
            if nums[k]>0: break
            if k>0 and nums[k]==nums[k-1]: continue
            i, j = k+1, len(nums)-1
            t = 0 - nums[k]
            while i<j:
                if nums[i]+nums[j]==t:
                    ans.append([nums[k], nums[i], nums[j]])
                    while i<j and nums[i]==nums[i+1]: i += 1
                    while i<j and nums[j]==nums[j-1]: j -= 1
                    i += 1
                    j -= 1
                elif nums[i]+nums[j]<t: i += 1
                else: j -= 1
        return ans
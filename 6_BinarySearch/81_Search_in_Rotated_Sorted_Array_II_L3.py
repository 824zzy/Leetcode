"""
If the number in the middle is less than the rightmost number, the right half is ordered;
If the middle number is greater than the rightmost number, the left half is ordered.
Else if the middle number is equal to rightmost number, the right pointer should minus one.
"""
class Solution:
    def search(self, nums: List[int], t: int) -> bool:
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m]==t:
                return True
            elif nums[m]<nums[r]:
                if nums[m]<t<=nums[r]: l = m + 1
                else: r = m - 1 
            elif nums[m]>nums[r]:
                if nums[l]<=t<nums[m]: r = m - 1
                else: l = m + 1
            else: r -= 1
        return False
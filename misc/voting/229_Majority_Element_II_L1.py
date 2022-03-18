""" https://leetcode.com/problems/majority-element-ii/
"""
# Boyer-Moore Vote Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1, cnt2, cand1, cand2 = 0, 0, None, None
        for n in nums:
            if n==cand1:
                cnt1 += 1
            elif n==cand2:
                cnt2 += 1
            elif cnt1==0:
                cand1 = n
                cnt1 += 1
            elif cnt2==0:
                cand2 = n
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [c for c in (cand1, cand2) if nums.count(c)>len(nums)//3]
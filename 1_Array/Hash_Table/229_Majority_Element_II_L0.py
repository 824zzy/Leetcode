from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v>len(nums//3]
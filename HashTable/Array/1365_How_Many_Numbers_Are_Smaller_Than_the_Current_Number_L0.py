class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        freq = {}
        for i, n in enumerate(sorted(nums)):
            if n not in freq: freq[n] = i
        return [freq[n] for n in nums]
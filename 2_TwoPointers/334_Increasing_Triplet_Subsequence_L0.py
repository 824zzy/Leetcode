class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        i, j = float('inf'), float('inf')
        for k in nums:
            if i>=k:  i = k
            elif j>=k: j = k
            else: return True
        return False
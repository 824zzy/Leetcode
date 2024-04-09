class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0, len(nums), 2):
            ans.extend([nums[i + 1]] * nums[i])
        return ans


"""
1 2 3
4 5 6
7 8 9

12

3
"""

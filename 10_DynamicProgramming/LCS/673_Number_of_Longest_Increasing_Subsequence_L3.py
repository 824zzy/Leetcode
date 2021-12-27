""" https://leetcode.com/problems/number-of-longest-increasing-subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/discuss/896111/Python3-bottom-up-dp-O(N2)
"""
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        lis = [[1, 1] for _ in nums] # longest increasing subsequence (length & count)
        for i, x in enumerate(nums): 
            for ii in range(i): 
                if nums[ii] < x: 
                    if lis[ii][0] + 1 > lis[i][0]: lis[i] = [1 + lis[ii][0], lis[ii][1]]
                    elif lis[ii][0] + 1 == lis[i][0]: lis[i][1] += lis[ii][1]
        mx, _ = max(lis, default=(0, 0))
        return sum(y for x, y in lis if x == mx)
""" https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
prefix sum + two pointers

Since prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j], 
lower bound of j is: prefix[j] >= 2 * prefix[i]
upper bound of j is: prefix[j] <= 0.5 * (prefix[-1] + prefix[i])
"""
class Solution:
    def waysToSplit(self, A: List[int]) -> int:
        MOD = 10**9+7
        ans = 0
        prefix = list(accumulate(A))
        for i in range(len(prefix)):
            lower_j = max(lower_j, i+1)
            while lower_j < len(nums) and 2*prefix[i] > prefix[lower_j]: lower_j += 1
            upper_j = max(upper_j, lower_j)
            while upper_j < len(nums) and 2*prefix[upper_j] <= prefix[i] + prefix[-1]: upper_j += 1
            ans += upper_j - j 
        return ans%MOD
    
""" 1 1 3 0
[0,3,3]
[1,1,1]
[1,2,2,2,5,0]
[3,2,1]
"""
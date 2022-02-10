""" https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/discuss/935986/Python3-O(N)-hash-table-of-prefix
"""
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        x = sum(nums) - x
        if not x: return len(nums) # edge case 
        
        seen = {0: -1}
        ans = prefix = 0
        for i, num in enumerate(nums): 
            prefix += num
            if prefix - x in seen: ans = max(ans, i - seen[prefix - x])
            seen.setdefault(prefix, i)
        return len(nums) - ans if ans else -1
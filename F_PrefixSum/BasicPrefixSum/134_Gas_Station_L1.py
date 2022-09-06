""" https://leetcode.com/problems/gas-station/
heuristic: 
all valid prefix sum should be not negative.
If we get negative prefix sum, it means we can not succeed using current starting index,
and we need to take next starting index.
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas)<sum(cost): return -1
        
        prefix = 0
        ans = 0
        for i in range(n):
            prefix += gas[i]-cost[i]
            if prefix<0:
                ans = i + 1
                prefix = 0
        return ans
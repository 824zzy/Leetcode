class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        if sum(gas)<sum(cost):
            return -1
        cur_t = 0
        idx = 0
        for i in range(n):
            cur_t += gas[i]-cost[i]
            if cur_t<0:
                idx = i + 1
                cur_t = 0
        return idx
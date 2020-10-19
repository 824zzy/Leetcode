from collections import defaultdict
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        reachable = defaultdict(set)
        S = set(stones)
        if stones[0]+1 not in S:
            return False
        reachable[stones[0]+1] = {stones[0]}
        for curr in stones[1:]:
            for pre in reachable[curr]:
                dis = curr - pre
                if dis+curr in S:
                    reachable[dis+curr].add(curr)
                if dis+curr+1 in S:
                    reachable[dis+curr+1].add(curr)
                if dis>1 and dis+curr-1 in S:
                    reachable[dis+curr-1].add(curr)
        return len(reachable[stones[-1]])>0
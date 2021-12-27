""" L3: https://leetcode.com/problems/smallest-sufficient-team/
TODO: https://leetcode.com/problems/smallest-sufficient-team/discuss/1201778/Python3-top-down-dp
"""

class Solution:
    def smallestSufficientTeam(self, R: List[str], P: List[List[str]]) -> List[int]:
        M = {s:i for i, s in enumerate(R)}
        print(M)
        masks = [sum(1<<M[s] for s in p) for p in P]
        print(masks)
        
        @cache
        def fn(i, mask): 
            """Return smallest sufficient team of people[i:] for skills in mask."""
            if mask == 0: return []
            if i == len(P): return [0]*100 # impossible
            if not (mask & masks[i]): return fn(i+1, mask)
            return min(fn(i+1, mask), [i] + fn(i+1, mask & ~masks[i]), key=len)
        
        return fn(0, (1 << len(R)) - 1)
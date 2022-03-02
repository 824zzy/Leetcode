""" https://leetcode.com/problems/smallest-sufficient-team/
1. First we need to create masks: set of skills for each person
2. If i == len(P), it means that it's impossible to have required skill
3. If mask = 0, it it means that we reach a possible solution.
4. We have two choices at each state: either take person i or do not take it. Here mask & ~masks[i] is used for subtraction of sets.
"""

class Solution:
    def smallestSufficientTeam(self, R: List[str], P: List[List[str]]) -> List[int]:
        M = {s:i for i, s in enumerate(R)}
        masks = [sum(1<<M[s] for s in p) for p in P]
        
        @cache
        def fn(i, mask): 
            """Return smallest sufficient team of people[i:] for skills in mask."""
            if mask == 0: return []
            if i == len(P): return [0]*100 # impossible
            if not (mask & masks[i]): return fn(i+1, mask)
            return min(fn(i+1, mask), [i] + fn(i+1, mask & ~masks[i]), key=len)
        
        return fn(0, (1 << len(R)) - 1)
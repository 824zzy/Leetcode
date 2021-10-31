""" L2: https://leetcode.com/problems/parallel-courses-iii/
topological sort to find earlist to finish course u and earlist to start course v
"""
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        e = defaultdict(list)
        inD = [0] * n
        for i, j in relations:
            e[j-1].append(i-1)
            inD[i-1] += 1
            
        Q = [(i, time[i]) for i, d in enumerate(inD) if d==0]
        
        start = [0] * n
        while Q:
            for _ in range(len(Q)):
                i, t = Q.pop(0)
                for j in e[i]: 
                    start[j] = max(start[j], t)
                    inD[j] -= 1
                    if not inD[j]: 
                        Q.append((j, start[j]+time[j]))
        return max(s+t for s, t in zip(start, time))
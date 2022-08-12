""" https://leetcode.com/problems/longest-cycle-in-a-graph/
1. use topological sort to remove non-cycle nodes
2. go over unseen nodes to count length of the cycles
"""
class Solution:
    def longestCycle(self, E: List[int]) -> int:
        n = len(E)
        inD = [0] * n
        for i, j in enumerate(E):
            if j!=-1:
                inD[j] += 1
        
        Q = [i for i, d in enumerate(inD) if d==0]
        seen = set()
        while Q:
            i = Q.pop(0)
            seen.add(i)
            j = E[i]
            if j!=-1:
                inD[j] -= 1
                if not inD[j]: Q.append(j)
                    
        ans = 0
        for i in E:
            if i==-1: continue
            cnt = 0
            while i not in seen:
                seen.add(i)
                i = E[i]
                cnt += 1
            ans = max(ans, cnt)
        
        return ans if ans!=0 else -1
                
"""
[3,3,4,2,3]
[2,-1,3,1]
[-1,2,1]
"""
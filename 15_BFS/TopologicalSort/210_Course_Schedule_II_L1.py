""" https://leetcode.com/problems/course-schedule-ii/
use topological sort template
"""
class Solution:
    def findOrder(self, n: int, A: List[List[int]]) -> List[int]:
        e = defaultdict(list)
        inD = [0] * n # in-degree
        for i, j in A:
            e[j].append(i)
            inD[i] += 1

        Q = [i for i, d in enumerate(inD) if d==0]
    
        ans = []
        while Q:
            i = Q.pop(0)
            ans.append(i)
            for j in e[i]:
                inD[j] -= 1
                if not inD[j]: Q.append(j)
        return ans if len(ans)==n else []
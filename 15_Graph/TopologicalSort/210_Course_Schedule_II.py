""" L1: template
TODO: use this problem to summary a template
"""
class Solution:
    def findOrder(self, n: int, A: List[List[int]]) -> List[int]:
        e = defaultdict(list)
        D = [0] * n # in-degree
        for i, j in A:
            e[j].append(i)
            D[i] += 1

        Q = []
        for i, d in enumerate(D):
            if d==0: Q.append(i)
    
        ans = []
        while Q:
            i = Q.pop(0)
            ans.append(i)
            for j in e[i]:
                D[j] -= 1
                if not D[j]: Q.append(j)
        return ans if len(ans)==n else []
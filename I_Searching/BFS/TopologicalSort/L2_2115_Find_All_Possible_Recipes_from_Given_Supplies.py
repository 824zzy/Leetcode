""" https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/
convert problem to topological sort
"""


class Solution:
    def findAllRecipes(self,
                       R: List[str],
                       I: List[List[str]],
                       S: List[str]) -> List[str]:
        G = defaultdict(list)
        inD = defaultdict(int)
        for r, i in zip(R, I):
            inD[r] = len(i)
            for ii in i:
                G[ii].append(r)

        ans = []
        Q = S
        R = set(R)
        while Q:
            i = Q.pop(0)
            if i in R:
                ans.append(i)
            for j in G[i]:
                inD[j] -= 1
                if not inD[j]:
                    Q.append(j)
        return ans

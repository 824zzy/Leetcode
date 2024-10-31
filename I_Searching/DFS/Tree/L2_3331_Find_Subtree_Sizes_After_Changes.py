""" https://leetcode.com/problems/find-subtree-sizes-after-changes/
two pass dfs:
1. first pass to find the cloest ancestor of each node
2. second pass to find the subtree size of each node
"""

from header import *


class Solution:
    def findSubtreeSizes(self, A: List[int], s: str) -> List[int]:

        T = defaultdict(list)
        for i in range(len(A)):
            if i == 0:
                continue
            T[A[i]].append(i)

        ancestor = {chr(97 + i): -1 for i in range(26)}

        def dfs(i):
            # backtracking to find cloest ancestor
            old = ancestor[s[i]]
            if ancestor[s[i]] != -1:
                A[i] = ancestor[s[i]]
            ancestor[s[i]] = i
            for j in T[i]:
                dfs(j)
            ancestor[s[i]] = old

        dfs(0)

        T = defaultdict(list)
        for i in range(len(A)):
            if i == 0:
                continue
            T[A[i]].append(i)

        ans = [1] * len(A)

        def dfs(i):
            # find subtree size
            sm = len(T[i])
            for j in T[i]:
                sm += dfs(j)
            ans[i] += sm
            return sm

        dfs(0)
        return ans


"""
[-1,0,0,1,1,1]
"abaabc"
[-1,0,4,0,1]
"abbba"
[-1,10,0,12,10,18,11,12,2,3,2,2,2,0,4,11,4,2,0]
"babadabbdabcbaceeda"
[-1,19,12,1,17,3,8,1,19,1,3,0,5,5,12,5,15,7,5,11]
"acecbebeeeeccabddcad"
"""

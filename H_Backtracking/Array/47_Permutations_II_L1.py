""" https://leetcode.com/problems/permutations-ii/submissions/
quite hard to handle duplicates if we cannot used `in` statement
E.g.: avoid [1a, 1b, 2a] and [1b, 1a, 2a]
To do that, we need to
1. sort the array
2. avoid duplicates by seen, `if i and A[i-1]==A[i] and i-1 not in seen`
"""
class Solution:
    def permuteUnique(self, A: List[int]) -> List[List[int]]:
        ans = []
        stk = []
        A.sort()
        
        def dfs(seen):
            if len(stk)==len(A): return ans.append(stk.copy())
            for i, x in enumerate(A):
                if i not in seen:
                    if i and A[i-1]==A[i] and i-1 not in seen: continue
                    stk.append(x)
                    dfs(seen+[i])
                    stk.pop()
        
        seen = []
        dfs(seen)
        return ans


# remove duplication using set
class Solution:
    def permuteUnique(self, A: List[int]) -> List[List[int]]:
        ans = set()
        stk = []
        
        def dfs(rem):
            if not rem: return ans.add(tuple(stk.copy()))
            for i, x in enumerate(rem):
                stk.append(x)
                dfs(rem[:i]+rem[i+1:])
                stk.pop()
        
        dfs(A)
        return ans
    

# cheating
from itertools import permutations
class Solution:
    def permuteUnique(self, A: List[int]) -> List[List[int]]:
        return list(set(permutations(A)))
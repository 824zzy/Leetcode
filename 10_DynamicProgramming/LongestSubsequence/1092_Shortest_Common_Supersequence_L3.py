""" https://leetcode.com/problems/shortest-common-supersequence/
TODO: solve this problem
"""
class Solution:
    def shortestCommonSupersequence(self, A: str, B: str) -> str:
        pass
#         @lru_cache(None)
#         def dfs(i, j):
#             if i==len(A) or j==len(B): return ''
#             elif A[i]==B[j]: return A[i]+dfs(i+1, j+1)
#             else: return max(dfs(i, j+1), dfs(i+1, j), key=len)
        
#         lcs = dfs(0, 0)
#         print(lcs, A.index(lcs), B.index(lcs))
#         ans = []
#         i = j = k = 0
#         while i<len(A) and j<len(B):
#             if A[i]==B[j]:
#                 ans.append(A[i])
#                 i += 1
#                 j += 1
#             elif A[i]!=lcs[k]:
#                 ans.append(A[i])
#                 i += 1
#             elif B[j]!=lcs[k]:
#                 ans.append(B[j])
#                 j += 1
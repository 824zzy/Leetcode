""" https://leetcode.com/problems/assign-cookies/
1. sort two lists
2. greedily assign legit cookies to children by two pointers
"""
class Solution:
    def findContentChildren(self, G: List[int], S: List[int]) -> int:
        G, S = G.sort(), S.sort()
        ans = 0
        i = 0
        for j in range(len(S)):
            if i<len(G) and G[i]<=S[j]: 
                i += 1
                ans += 1
        return ans
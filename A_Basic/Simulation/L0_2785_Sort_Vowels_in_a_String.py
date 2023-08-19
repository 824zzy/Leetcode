""" https://leetcode.com/problems/sort-vowels-in-a-string/
string simulation
"""
class Solution:
    def sortVowels(self, s: str) -> str:
        ans = [0]*len(s)
        v = []
        for i, c in enumerate(s):
            if c not in 'aeiouAEIOU':
                ans[i] = c
            else:
                v.append(c)
        v.sort()
        j = 0
        for i, c in enumerate(s):
            if ans[i]==0:
                ans[i] = v[j]
                j += 1
        return ''.join(ans)
""" https://leetcode.com/problems/reorganize-string/
Translate the problem to: rearrange characters to ensure no two adjacent projects are the same.
So based on characters frequency, we can fill the string by odd position first, then even positions.
"""
class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        A = sorted([[v, k] for k, v in cnt.items()], reverse=True)
        ans = ['']*len(s)
        i = 0
        
        if A[0][0]>(len(s)+1)/2: return ''
        for v, k in A:
            for _ in range(v):
                ans[i] = k
                i += 2
                if i>=len(s): i = 1
        return ''.join(ans)
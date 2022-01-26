""" https://leetcode.com/problems/maximum-product-of-word-lengths/
utilize bit mask for quicker check of overlapping.
"""
class Solution:
    def maxProduct(self, A: List[str]) -> int:
        S = defaultdict(int)
        for w in A:
            mask = 0
            for c in w:
                mask |= 1<<(ord(c)-ord('a'))
            S[mask] = w
        
        ans = 0
        for x in S:
            for y in S:
                if not x&y: ans = max(ans, len(S[x])*len(S[y]))
        return ans
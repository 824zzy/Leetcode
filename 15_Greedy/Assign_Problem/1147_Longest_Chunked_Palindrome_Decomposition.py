""" L1
recursively assign shortest matched substring frome two sides to middle
"""
class Solution:
    def longestDecomposition(self, T: str, ans=0) -> int:
        if not T: return ans
        for i in range(len(T)//2):
            if T[:i+1]==T[len(T)-i-1:]:
                return self.longestDecomposition(T[i+1:len(T)-i-1], ans+2)
        return ans+1
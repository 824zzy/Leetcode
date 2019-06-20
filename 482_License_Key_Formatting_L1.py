"""
S[i, i+k] will not out of range at the last element.
"""
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = ''.join(S.split('-'))[::-1]
        ans = ''
        
        for i in range(len(S), K):
            ans += '-' + S[i, i+k].upper()
        return ans[::-1][:-1]
""" https://leetcode.com/problems/scramble-string/
A special double sequence dp problem using string rather than index.

For every index that we can split the string into two parts, we can either swap the two parts, or keep the two parts the same.
"""
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2): return False
        
        @cache
        def dp(s1, s2):
            if s1==s2: return True
            if sorted(s1)!=sorted(s2): return False
            
            for i in range(1, len(s1)):
                # don't swap or swap
                if (dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:])) or \
                   (dp(s1[:i], s2[-i:]) and dp(s1[i:], s2[:-i])):
                    return True
            return False
            
        return dp(s1, s2)
""" https://leetcode.com/problems/one-edit-distance/
only need to check the first different char
"""
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if s==t: return False
        i, j = 0, 0
        while i<len(s) and j<len(t) and s[i]==t[j]:
            i += 1
            j += 1
        # insert/delete
        if s==t[:j]+t[j+1:] or s[:i]+s[i+1:]==t: return True
        # replace
        if s[:i]+s[i+1:]==t[:j]+t[j+1:]: return True
        return False
    
    
"""
"ab"
"acb"
""
""
"""
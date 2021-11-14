"""
haystack.index(needle) available as well.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and not needle:
            return 0
        
        for i in range(len(haystack)):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1
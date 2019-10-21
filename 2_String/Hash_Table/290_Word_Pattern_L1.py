class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if len(pattern)!=len(str.split()):
            return False
        
        d = {}
        for i, s in enumerate(str.split()):
            try:
                if d[pattern[i]]!=s:
                    return False
            except:
                if s in d.values():
                    return False
                d[pattern[i]] = s
        return True
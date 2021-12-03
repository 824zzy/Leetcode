from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        if not pattern:
            return False
        
        pd, sd = defaultdict(list), defaultdict(list)
        for i, s in enumerate(str.split()):
            sd[s].append(i)
        for i, s in enumerate(pattern):
            pd[s].append(i)
            
        for k, v in pd.items():
            if v not in sd.values():
                return False
        return True
    
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
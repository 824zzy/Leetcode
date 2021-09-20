# Pattern matching
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2+1):
            sub = s[:i]
            if sub*(len(s)//i) == s:
                return True
        return False
    
# Search template
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        seen = []
        for i in range(1, len(s)//2+1):
            seen.append(s[:i])
        
        def dfs(s, pat):
            if s==pat:
                return True
            
            if s[:len(pat)]==pat:
                ans = dfs(s[len(pat):][:], pat)
            else:
                return False
            return ans
                
        for pat in seen:
            ans = dfs(s, pat)
            if ans:
                return True
        return False
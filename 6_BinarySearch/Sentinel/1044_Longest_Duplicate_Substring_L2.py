""" https://leetcode.com/problems/longest-duplicate-substring/
Use binary search to save searching time.
"""
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        def find_sub(m):
            seen = Counter()
            for i in range(len(s)-m+1):
                seen[s[i:i+m]] += 1
            
            subs = [k for k, v in seen.items() if v>1]
            if subs:
                self.ans = max(subs, key=lambda x: len(x))
                return True
            else: return False
            
            
        l, r = 0, len(s)-1
        self.ans = ""
        while l<=r:
            m = (l+r)//2
            
            if find_sub(m): l = m + 1
            else: r = m - 1 
        return self.ans
""" L2: https://leetcode.com/problems/longest-duplicate-substring/
Use binary search to save searching time. TODO: optimize sliding window by rolling hash: 
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

# TODO: https://leetcode.com/problems/longest-duplicate-substring/discuss/1548046/Python3-rolling-hash
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        mod = 1_000_000_007
        
        def fn(k): 
            """Return duplicated substring of length k."""
            p = pow(26, k, mod)
            hs = 0
            seen = {}
            for i, ch in enumerate(s): 
                hs = (26*hs + ord(ch) - 97) % mod
                if i >= k: hs = (hs - (ord(s[i-k])-97)*p) % mod # rolling hash 
                if i+1 >= k:
                    if hs in seen and s[i+1-k:i+1] in seen[hs]: return s[i+1-k:i+1] # resolve hash collision
                    seen.setdefault(hs, set()).add(s[i+1-k:i+1])
            return ""
        
        lo, hi = 0, len(s)-1
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid): lo = mid
            else: hi = mid - 1
        return fn(lo)
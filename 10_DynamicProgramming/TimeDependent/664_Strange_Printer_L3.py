""" https://leetcode.com/problems/strange-printer/
"""
class Solution:
    def strangePrinter(self, s: str) -> int:
        s = "".join(ch for i, ch in enumerate(s) if i == 0 or s[i-1] != ch)
        
        @cache
        def fn(lo, hi): 
            """Return min ops to print s[lo:hi]."""
            if lo == hi: return 0
            ans = 1 + fn(lo+1, hi)
            for mid in range(lo+1, hi): 
                if s[lo] == s[mid]: 
                    ans = min(ans, fn(lo, mid) + fn(mid+1, hi))
            return ans 
        
        return fn(0, len(s))
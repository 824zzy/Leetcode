""" https://leetcode.com/problems/shortest-string-that-contains-three-strings/
enumerate all possible combinations + string matching
"""
from header import *

class Solution:
    def minimumString(self, A: str, B: str, C: str) -> str:
        def merge(s, t):
            if s in t: return t
            if t in s: return s
            l = min(len(s), len(t))
            for i in reversed(range(1, l+1)):
                if s[-i:]==t[:i]:
                    return s+t[i:]
            return s+t
            
        ans = 'z'*300
        for a, b, c in permutations((A, B, C)):
            abc = merge(merge(a, b), c)
            ans = min(ans, abc, key=lambda x: (len(x), x))
        return ans
    

class Solution:
    def minimumString(self, A: str, B: str, C: str) -> str:
        ans = 'z'*(len(A)+len(B)+len(C))
        for a, b, c in ((A, B, C), (A, C, B), (B, A, C), (B, C, A), (C, A, B), (C, B, A)):
            if b in a:
                ab = a
            else:
                ab = a+b
                l = min(len(a), len(b))
                for i in reversed(range(1, l+1)):
                    if a[-i:]==b[:i]:
                        ab = a+b[i:]
                        break
            if c in ab:
                abc = ab
            else:
                abc = ab+c
                l = min(len(c), len(ab))
                for i in reversed(range(1, l+1)):
                    if ab[-i:]==c[:i]:
                        abc = ab+c[i:]
                        break
            ans = min(ans, abc, key=lambda x: (len(x), x))
        return ans
    
"""
"abc"
"bca"
"aaa"
"ab"
"ba"
"aba"
"ca"
"a"
"a"
"ab"
"a"
"c"
"cab"
"a"
"b"
"""
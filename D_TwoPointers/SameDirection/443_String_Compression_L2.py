""" https://leetcode.com/problems/string-compression/
"""
from header import *

class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('~')
        cnt = 1
        i = 0
        x = chars[0]
        for j in range(1, len(chars)):
            if chars[j]==chars[j-1]:
                cnt += 1
            elif cnt>1:
                chars[i], x = x, chars[j]
                chars[i+1:i+len(str(cnt))+1] = list(str(cnt))
                i += 1+len(str(cnt))
                cnt = 1
            else:
                chars[i] = x
                i += 1
                x = chars[j]
        chars = chars[:i]
        return len(chars)
    
"""
["a","a","b","b","c","c","c"]
["a"]
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
["a","a","a","a","a","b"]
["#","$","#","#","$","$","$","$","#","#"]
"""
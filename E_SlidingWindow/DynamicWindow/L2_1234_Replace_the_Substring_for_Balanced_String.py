""" https://leetcode.com/problems/replace-the-substring-for-balanced-string/
Given s, we can find the number of Q, W, E, R that exceed their quota len(s)//4. Sweep through s and find the shortest subarray which is enough to provide the exceeding part.
"""
from header import *

class Solution:
    def balancedString(self, s: str) -> int:
        t = len(s)//4
        cnt = Counter()
        for c in s:
            cnt[c] += 1
        for c in cnt:
            cnt[c] = max(0, cnt[c]-t)
            
        sw = Counter()
        i = 0
        ans = len(s)
        for j, c in enumerate(s):
            sw[c] += 1
            # the sliding window must ensure the count of Q W E R is smaller than the upper bound
            while i<len(s) and all(sw[k]>=v for k, v in cnt.items()):
                ans = min(ans, j-i+1)
                sw[s[i]] -= 1
                i += 1
        return ans
        
        
"""
"QWER"
"QQWE"
"QQQW"
"QQQWQWWR"
"WWEQERQWQWWRWWERQWEQ"
"QEQRWRRWWWRQQQWQQEQEQREWRQEQRQQRRQEW"
"""     
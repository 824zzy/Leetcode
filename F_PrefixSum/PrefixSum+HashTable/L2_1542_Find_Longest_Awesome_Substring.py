""" https://leetcode.com/problems/find-longest-awesome-substring/
the same as 1915

categorization + bit mask + prefix sum + hash table

palindrome ==> at most one odd number, the other should be the same
"""
from header import *

class Solution:
    def longestAwesome(self, s: str) -> int:
        cnt = Counter()
        cnt[0] = -1
        ans = pre = 0
        for i, c in enumerate(s):
            pre ^= 1 << int(c)
            # case 1
            if pre in cnt:
                ans = max(ans, i-cnt[pre])
            # case 2
            for j in range(10):
                if pre^(1<<j) in cnt:
                    ans = max(ans, i-cnt[pre^(1<<j)])
            cnt.setdefault(pre, i)
        return ans
    
"""
"3242415"
"12345678"
"213123"
"""
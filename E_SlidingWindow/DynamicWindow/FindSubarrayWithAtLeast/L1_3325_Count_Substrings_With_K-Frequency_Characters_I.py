""" https://leetcode.com/problems/count-substrings-with-k-frequency-characters-i/
sliding window template
"""

from header import *


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        cnt = Counter()
        i = 0
        ans = 0
        for j in range(len(s)):
            cnt[s[j]] += 1
            while cnt[s[j]] >= k:
                cnt[s[i]] -= 1
                i += 1
            ans += i
        return ans


"""
"abacb"
2
"abcde"
1
"""

""" https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/submissions/

"""

from header import *


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        cnt = Counter()
        i = 0
        ans = 0
        for j in range(len(s)):
            cnt[s[j]] += 1
            while len(cnt) == 3:
                cnt[s[i]] -= 1
                if cnt[s[i]] == 0:
                    cnt.pop(s[i])
                i += 1
            ans += i
        return ans

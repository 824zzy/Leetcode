""" L1:
tricky line to count all the legit substrings: ans += i
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        i = 0
        seen = {'a': 0, 'b': 0, 'c': 0}
        for j in range(len(s)):
            seen[s[j]] += 1
            while all(seen.values()):
                seen[s[i]] -= 1
                i += 1
            ans += i
        return ans

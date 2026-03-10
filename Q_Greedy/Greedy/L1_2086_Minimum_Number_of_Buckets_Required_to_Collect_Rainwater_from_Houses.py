""" https://leetcode.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses/
Find all the patterns
"""


class Solution:
    def minimumBuckets(self, S: str) -> int:
        S, ans = list(S), 0
        for i, c in enumerate(S):
            if c == "H" and (i == 0 or S[i - 1] != "#"):
                if i + 1 < len(S) and S[i + 1] == ".":
                    S[i + 1] = "#"
                elif i and S[i - 1] == ".":
                    S[i - 1] = "#"
                else:
                    return -1
                ans += 1
        return ans


class Solution:
    def minimumBuckets(self, S: str) -> int:
        if S == "H" or S[:2] == "HH" or S[-2:] == "HH" or "HHH" in S:
            return -1
        return S.count("H") - S.count("H.H")

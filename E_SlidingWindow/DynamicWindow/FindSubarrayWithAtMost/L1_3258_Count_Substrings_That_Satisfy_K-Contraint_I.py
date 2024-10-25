""" https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-i/
Translate the problem from:
A binary string satisfies the k-constraint if either of the following conditions holds:
The number of 0's in the string is at most k.
The number of 1's in the string is at most k.

to:
Find sliding window that both the number of 0's and 1's in the string are more than k.
"""

from header import *


class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        cnt = Counter()
        ans = 0
        i = 0
        for j in range(len(s)):
            cnt[s[j]] += 1
            while cnt["0"] > k and cnt["1"] > k:
                cnt[s[i]] -= 1
                i += 1
            ans += j - i + 1
        return ans


"""
"10101"
1
"1010101"
2
"11111"
1
"""

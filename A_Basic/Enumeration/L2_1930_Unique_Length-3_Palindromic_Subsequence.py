""" https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
smart solution:
1. we enumerate each character on two side.
2. We find its first occurrence and its last occurrence,
3. all the characters in the middle are the candidate for the middle char.
naive solution:
    for each element in the string, we check if any character is located on the two side.
"""
from header import *

# smart solution from lee: 
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left_most = defaultdict(lambda: inf)
        right_most = defaultdict(lambda: -inf)
        for i, c in enumerate(s):
            left_most[c] = min(left_most[c], i)
            right_most[c] = max(right_most[c], i)

        ans = 0
        for x in range(26):
            i, j = left_most[chr(x+97)], right_most[chr(x+97)]
            if i!=inf and j!=-inf:
                ans += len(set(s[i+1:j]))
        return ans


# naive solution: will TLE sometimes
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = set()
        seen = Counter()
        remain = Counter(s)
        
        for c in s:
            remain[c] -= 1
            for x in ascii_lowercase:
                if seen[x] and remain[x]:
                    ans.add(x+c+x)
            seen[c] += 1
        return len(ans)
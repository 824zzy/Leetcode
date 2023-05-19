""" https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/
smart solution:
    we enumerate each character on two side.
    We find its first occurrence and its last occurrence,
    all the characters in the middle are the candidate for the middle char.
naive solution:
    for each element in the string, we check if any character is located on the two side.
"""
from header import *

# smart solution from lee: 
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for c in ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i!=-1:
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
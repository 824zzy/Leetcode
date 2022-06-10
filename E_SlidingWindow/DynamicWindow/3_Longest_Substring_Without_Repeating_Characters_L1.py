""" https://leetcode.com/problems/longest-substring-without-repeating-characters/
Use a dictionary seen as a sliding window
"""
class Solution:
    def lengthOfLongestSubstring(self, A: str) -> int:
        ans = 0
        seen = set()
        i = 0
        for j in range(len(A)):
            while A[j] in seen:
                seen.remove(A[i])
                i += 1
            ans = max(ans, j-i+1)
            seen.add(A[j])
        return ans
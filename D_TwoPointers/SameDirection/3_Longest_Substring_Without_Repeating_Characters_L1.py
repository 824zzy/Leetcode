""" https://leetcode.com/problems/longest-substring-without-repeating-characters/
Use a dictionary seen to keep track of visited characters and their last positions in string. 
While moving a pointer i forward, if s[i] has seen before, 
move anchor k (forward only) to 1 + seen[s[i]] to make sure no duplicates between k and i.

Time complexity: O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, A: str) -> int:
        i = 0
        ans = 0
        seen = {}
        for j in range(len(A)):
            # update i if there is any duplicate
            if A[j] in seen: i = max(i, seen[A[j]]+1)
            ans = max(ans, j-i+1)
            seen[A[j]] = j
        return ans
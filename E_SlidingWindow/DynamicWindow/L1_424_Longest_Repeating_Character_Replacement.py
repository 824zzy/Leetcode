""" https://leetcode.com/problems/longest-repeating-character-replacement/
the same as 2024.
"""
from header import *

# Since in a substring(A[i:j]) we can at most replace k characters, so use a Counter to record the most frequent element.
# Then the window boundary can be updated by: j-i+1>max(cnt.values())+k


class Solution:
    def characterReplacement(self, A: str, k: int) -> int:
        seen = Counter()
        i = 0
        ans = 0

        for j in range(len(A)):
            seen[A[j]] += 1
            while (j - i + 1) - max(seen.values()) > k:
                seen[A[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)

        return ans


# or use sliding window to ensure the minimum of seen is less or equal than k


class Solution:
    def maxConsecutiveAnswers(self, A: str, k: int) -> int:
        A = [0 if c == "T" else 1 for c in A]
        seen = [0, 0]
        i = 0
        ans = 0

        for j in range(len(A)):
            seen[A[j]] += 1
            while min(seen) > k:
                seen[A[i]] -= 1
                i += 1
            ans = max(ans, j - i + 1)
        return ans

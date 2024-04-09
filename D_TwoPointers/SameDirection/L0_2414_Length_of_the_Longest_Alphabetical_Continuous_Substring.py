""" https://leetcode.com/problems/length-of-the-longest-alphabetical-continuous-substring/
update left point once the ord(A[j-1])+1!=ord(A[j])
"""


class Solution:
    def longestContinuousSubstring(self, A: str) -> int:
        ans = 0
        i = 0
        for j in range(len(A)):
            if j and ord(A[j - 1]) + 1 != ord(A[j]):
                i = j
            ans = max(ans, j - i + 1)
        return ans

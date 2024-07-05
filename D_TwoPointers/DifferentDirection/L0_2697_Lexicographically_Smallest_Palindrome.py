""" https://leetcode.com/problems/lexicographically-smallest-palindrome/
greedy, using two pointers
"""


class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        A = list(s)
        l, r = 0, len(A) - 1
        while l < r:
            if A[l] != A[r]:
                A[l] = A[r] = min(A[l], A[r])
            l += 1
            r -= 1
        return "".join(A)

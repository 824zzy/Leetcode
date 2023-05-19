""" https://leetcode.com/problems/valid-palindrome-iv/
count difference characters by two pointers
"""
class Solution:
    def makePalindrome(self, A: str) -> bool:
        cnt = 0
        l, r = 0, len(A)-1
        while l<r:
            if A[l]!=A[r]:
                cnt += 1
            l += 1
            r -= 1
        return cnt<=2

""" https://leetcode.com/problems/valid-palindrome-ii/
1. use two pointers to find the first different character pairs
2. check if any one of the two conditions(A[l:r], A[l+1:r+1]) is valid palindrome
"""
class Solution:
    def validPalindrome(self, A: str) -> bool:
        l, r = 0, len(A)-1
        while l<r:
            if A[l]!=A[r]:
                return A[l:r]==A[l:r][::-1] or A[l+1:r+1]==A[l+1:r+1][::-1] 
            else: l, r = l+1, r-1
        return True
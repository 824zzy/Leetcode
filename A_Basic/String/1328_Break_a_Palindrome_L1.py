""" https://leetcode.com/problems/break-a-palindrome/
greedily find non-'a' character in the first half of the string, and replace it with 'a'.
if no such character exists, replace the last character with 'b'.
"""
class Solution:
    def breakPalindrome(self, P: str) -> str:
        for i in range(len(P)//2):
            if P[i]!='a': return P[:i]+'a'+P[i+1:]
        if len(P)>1: return P[:-1]+'b'
        else: return ''
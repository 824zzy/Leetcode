""" https://leetcode.com/problems/break-a-palindrome/
greedy
"""
class Solution:
    def breakPalindrome(self, P: str) -> str:
        for i in range(len(P)//2):
            if P[i]!='a': return P[:i]+'a'+P[i+1:]
        if len(P)>1: return P[:-1]+'b'
        else: return ''
""" https://leetcode.com/problems/largest-palindromic-number/
greedily use the largest number to build the first half of palindrome.
And for the middle element, we need to choose the largest element whose frequency is odd.
"""
from header import *

class Solution:
    def largestPalindromic(self, A: str) -> str:
        cnt = Counter(A)
        A = sorted(cnt.items(), key=lambda x: -int(x[0]))
        
        ans = []
        mx = []
        for c, freq in A:
            # find middle element
            if freq%2 and not mx: mx = [str(c)]
            # avoid leading zero
            if not ans and c=='0': continue
            # extend first half
            ans.extend([str(c)]*(freq//2))
        return ''.join(ans+mx+ans[::-1]) or '0'
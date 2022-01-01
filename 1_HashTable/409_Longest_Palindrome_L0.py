""" https://leetcode.com/problems/longest-palindrome/
frequency table to count odd and even numbers, note that one needs to add extra 1 if there is odd number
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = Counter(s)
        ans = 0
        odd = False
        for k, v in cnt.items():
            if v&1==0: ans += v
            else: ans, odd = ans+v-1, True
        return ans+(odd==True)
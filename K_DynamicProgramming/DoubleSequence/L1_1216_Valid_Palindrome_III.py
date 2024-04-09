""" https://leetcode.com/problems/valid-palindrome-iii/
dp(i, j, k) will TLE, so we count the cost of deletion and check if it is less than k
"""
from header import *


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        @cache
        def dp(i, j):
            if i > j:
                return 0
            # equal
            if s[i] == s[j]:
                return dp(i + 1, j - 1)
            # not equal
            return min(1 + dp(i + 1, j), 1 + dp(i, j - 1))
        return dp(0, len(s) - 1) <= k


"""
"abcdeca"
2
"abbababa"
1
"fcgihcgeadfehgiabegbiahbeadbiafgcfchbcacedbificicihibaeehbffeidiaiighceegbfdggggcfaiibefbgeegbcgeadcfdfegfghebcfceiabiagehhibiheddbcgdebdcfegaiahibcfhheggbheebfdahgcfcahafecfehgcgdabbghddeadecidicchfgicbdbecibddfcgbiadiffcifiggigdeedbiiihfgehhdegcaffaggiidiifgfigfiaiicadceefbhicfhbcachacaeiefdcchegfbifhaeafdehicfgbecahidgdagigbhiffhcccdhfdbd"
216
"""

""" https://leetcode.com/problems/valid-palindrome-iii/
convert the problem into finding the longest palindromic subsequence and check if it is longer than len(s)-k

the same as 516
"""
from header import *

class Solution:
    def isValidPalindrome(self, A: str, k: int) -> bool:
        if len(A)<=k: return True

        @cache
        def dp(i, j):
            if i==j: return 1
            if i>j: return 0
            if A[i]==A[j]:
                return dp(i+1, j-1)+2
            else:
                return max(dp(i+1, j), dp(i, j-1))

        return len(A)-dp(0, len(A)-1)<=k

"""
"fcgihcgeadfehgiabegbiahbeadbiafgcfchbcacedbificicihibaeehbffeidiaiighceegbfdggggcfaiibefbgeegbcgeadcfdfegfghebcfceiabiagehhibiheddbcgdebdcfegaiahibcfhheggbheebfdahgcfcahafecfehgcgdabbghddeadecidicchfgicbdbecibddfcgbiadiffcifiggigdeedbiiihfgehhdegcaffaggiidiifgfigfiaiicadceefbhicfhbcachacaeiefdcchegfbifhaeafdehicfgbecahidgdagigbhiffhcccdhfdbd"
216
"dgefaiechgiihccaedehcgcfbfaggcahiihceeddbffabfeabgaaihcahbehaehgahfchdaggccehadhbahefbafadhfehgfceffidebaebeagiiiffgdgcihbdfaibeihafghefgcigdcdbigbecagabachefaecfaahcchaidffffeicgicdhciefbhdhiggeaiefceedgdggabhafhdacccchdffacabgccicieiabhdabcchdgdedfiicdegfdbbbicbabiagaahbcfhaffhebciaffaehgbbibdehacehbddcfbhdcaidhaadfegahgefhabiifaiecbcfgddh"
343
"""
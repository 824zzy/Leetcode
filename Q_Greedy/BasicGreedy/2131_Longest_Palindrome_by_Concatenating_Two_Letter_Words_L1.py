""" https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/
1. create a freq table for all the words
2. greedily add words to the palindrome
"""
from header import *

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        ans = 0
        flag = True
        for k, v in cnt.items():
            _k = k[1]+k[0]
            if _k!=k:
                ans += 2*min(v, cnt[_k])
            elif _k==k:
                # even count 'xx'
                if v%2==0: ans += 2*v
                # if odd count 'xx', then place the extra in the middle once
                elif flag:
                    ans += 2*v
                    flag = False
                else:
                    ans += 2*v-2
        return ans
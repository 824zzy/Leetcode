""" https://leetcode.com/problems/remove-letter-to-equalize-frequency/
There are only two conditions, remove the letter has the most frequency or remove the letter has the least frequency.
1. copy two hash tables
2. simulate the process of removing the letter has the most frequency
3. check if the frequency of each letter is the same
"""
from header import *


class Solution:
    def equalFrequency(self, A: str) -> bool:
        cnt = Counter(A)
        mx = max(cnt.items(), key=lambda x: x[1])
        mn = min(cnt.items(), key=lambda x: x[1])
        cnt_mx = cnt.copy()
        cnt_mx[mx[0]] -= 1
        if not cnt_mx[mx[0]]:
            cnt_mx.pop(mx[0])
        if len(set(cnt_mx.values())) == 1:
            return True

        cnt_mn = cnt.copy()
        cnt_mn[mn[0]] -= 1
        if not cnt_mn[mn[0]]:
            cnt_mn.pop(mn[0])
        if len(set(cnt_mn.values())) == 1:
            return True
        return False


"""
"abcc"
"aazz"
"ab"
"abbcc"
"""

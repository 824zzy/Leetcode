""" https://leetcode.com/problems/total-appeal-of-a-string/
from god lee: https://leetcode.com/problems/total-appeal-of-a-string/discuss/1996390/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation
"""
class Solution:
    def appealSum(self, s):
        last = {}
        res = 0
        for i, c in enumerate(s):
            last[c] = i + 1
            res += sum(last.values())
        return res
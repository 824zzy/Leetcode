""" https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/
learn from: https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1390193/Python-Greedy-O(n)-explained
greedily find minimum swaps through counting not-opened parentheses
the swaps is `(cl+1)//2` since one swap can eliminate at most 2 not-opened parentheses
"""
class Solution:
    def minSwaps(self, s: str) -> int:
        cl = op = 0
        for c in s:
            if c=='[': op += 1
            else: op -= 1
            if op<0:
                op = 0
                cl += 1
        return (cl+1)//2
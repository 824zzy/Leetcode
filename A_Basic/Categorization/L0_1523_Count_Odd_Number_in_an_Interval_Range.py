""" https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/
case 1: l is odd, r is odd, l-=1
case 2: l is even, r is even, r+=1
"""


class Solution:
    def countOdds(self, l: int, r: int) -> int:
        if l & 1:
            l -= 1
        if r & 1:
            r += 1
        return (r - l) // 2

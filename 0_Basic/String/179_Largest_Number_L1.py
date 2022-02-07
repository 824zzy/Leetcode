""" https://leetcode.com/problems/largest-number/
use customized compare key to sort the nums
"""
import functools
class Solution:
    def largestNumber(self, nums):
        ans = ''.join(sorted(map(str, nums)), key=functools.cmp_to_key(lambda x, y: int(y+x)-int(x+y)))
        return ans if ans[0]!='0' else '0'
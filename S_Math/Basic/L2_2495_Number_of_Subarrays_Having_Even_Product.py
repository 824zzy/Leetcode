""" https://leetcode.com/problems/number-of-subarrays-having-even-product/description/
1. The product of elements in a subarray is even if it contains at least one even element.
2. Iterate from left to right and save the last index of an even number. Let that saved index be “j”.
3. It can be seen that every subarray starting from earlier than index “j” and ending at the current index has an even product.
"""
from header import *
class Solution:
    def evenProduct(self, A: List[int]) -> int:
        ans = 0
        cnt = 0
        for i, x in enumerate(A):
            if x&1==0:
                cnt = i+1
            ans += cnt
        return ans
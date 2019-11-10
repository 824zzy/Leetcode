""" Google
Sliding window series problem
use OrderedDict as a window
"""
from collections import OrderedDict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        ans = 0
        last_two = OrderedDict()
        cnt = 0
        
        for i, fruit in enumerate(tree):
            fruit = tree[i]
            if fruit in last_two:
                last_two.pop(fruit)
            last_two[fruit] = i
            cnt += 1
            if len(last_two) > 2:
                cnt = i - last_two.eaapopitem(last=False)[1]
            ans = max(ans, cnt)
        return ans
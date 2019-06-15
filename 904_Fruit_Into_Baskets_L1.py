""" Sliding window series problem
use OrderedDict as a window
"""
from collections import OrderedDict
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        last_two = OrderedDict()
        ans = 0
        cnt = 0
        
        for i in range(len(tree)):
            frt = tree[i]
            if frt in last_two:
                last_two.pop(frt)
        
        last_two[frt] = i

        cnt += 1
        if len(last_two)>2:
            cnt = i - last_two.popitem(last=False)[1]
        ans = max(cnt, ans)
    return ans
                


"""
[1, 2, 1]  3


"""

        
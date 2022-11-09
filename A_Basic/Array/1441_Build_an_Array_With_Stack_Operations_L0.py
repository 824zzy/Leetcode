""" https://leetcode.com/problems/build-an-array-with-stack-operations/description/
linear scan and simulate the stack operations
"""
from header import *

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        cnt = 1
        for t in target:
            if cnt!=t:
                ans.extend(["Push","Pop"]*(t-cnt))
            ans.append('Push')
            cnt = t+1
        return ans
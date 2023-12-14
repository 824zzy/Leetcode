""" https://leetcode.com/problems/count-tested-devices-after-test-operations/
think as difference array 

translate the problem into:
    the current device can be tested if batteryPercentages[i] is greater than the number of tested devices.
"""
from header import *

class Solution:
    def countTestedDevices(self, A: List[int]) -> int:
        ans = 0
        for i in range(len(A)):
            if A[i]>ans:
                ans += 1
        return ans
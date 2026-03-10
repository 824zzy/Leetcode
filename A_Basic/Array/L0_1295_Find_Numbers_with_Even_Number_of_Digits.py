""" https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                ans += 1
        return ans

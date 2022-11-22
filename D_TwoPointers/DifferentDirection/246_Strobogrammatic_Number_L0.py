""" https://leetcode.com/problems/strobogrammatic-number/
use a map to store the pairs of strobogrammatic numbers
"""
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mp = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',            
        }

        l, r = 0, len(num)-1
        while l<=r:
            if num[l] not in mp or num[r] not in mp or mp[num[l]]!=num[r]:
                return False
            l += 1
            r -= 1
        
        return True
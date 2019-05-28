""" essentially the binary search
"""
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min = 1
        max = n
        
        while(True):
            mid = (min + max) // 2
            if min == max:
                return min
            elif isBadVersion(mid):
                max = mid
            else:
                min = mid + 1
            
        
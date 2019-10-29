class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l <= r:     
            m = (l + r) // 2
            if l == r:
                return m
            if isBadVersion(m):
                r = m
            else:
                l = m + 1
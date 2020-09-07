# Facebook
class Solution:
    def firstBadVersion(self, n):
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

class Solution:
    def firstBadVersion(self, n):
        l, r = 1, n
        if l==r:
            return l
        while l<r:
            m = (l+r)//2
            if isBadVersion(m):
                r = m
            else:
                l = m+1
        return r
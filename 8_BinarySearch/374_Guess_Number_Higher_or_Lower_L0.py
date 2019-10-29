class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        while l<=h:
            m = (l+h)//2
            if guess(m)==0:
                return m
            elif guess(m)==1:
                l = m + 1
            else:
                h = m - 1
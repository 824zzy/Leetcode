class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        x = str(x)[::-1]
    
        count = 0
        for c in x:
            if c == '0':
                count += 1
            else:
                break
        x = x[count:]
        
        if x[-1] == '-':
            x = '-' + x
            x = x[:-1]

        if -2**31 <= int(x) <= 2**31-1:
            return x
        else:
            return 0
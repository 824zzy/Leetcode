""" Determine whether an integer is palindrome(it reads the same forward and backward)
1. transfer x into a string
2. `list[::-1]` or `list.reverse()` to reverse the list 

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x[::-1] == x:
            return True
        else:
            return False
        
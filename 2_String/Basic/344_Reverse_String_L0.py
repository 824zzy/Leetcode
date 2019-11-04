class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            s[i], s[-i-1] = s[-i-1], s[i]

""" 5/20/2019
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        post_i = len(s) - 1
        for pre_i in range(len(s)//2):
            s[pre_i], s[post_i] = s[post_i], s[pre_i]
            post_i -= 1
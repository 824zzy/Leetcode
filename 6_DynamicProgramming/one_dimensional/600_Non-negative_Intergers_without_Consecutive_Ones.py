""" L3: https://www.geeksforgeeks.org/count-number-binary-strings-without-consecutive-1s/
Let a[i] be the number of binary strings of length i which do not contain any two consecutive 1’s and which end in 0. 
Similarly, let b[i] be the number of such strings which end in 1. 
We can append either 0 or 1 to a string ending in 0, but we can only append 0 to a string ending in 1.
"""
class Solution:
    def findIntegers(self, n: int) -> int:
        a = [0 for i in range(n)]
        b = [0 for i in range(n)]
        a[0] = b[0] = 1
        for i in range(1, n):
            a[i] = a[i-1] + b[i-1]
            b[i] = a[i-1]
        return a[n-1]+b[n-1]

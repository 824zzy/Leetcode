""" From Lee215
Explanation
First, I count the number of 1 or 0 grouped consecutively.
For example "0110001111" will be [1, 2, 3, 4].

Second, for any possible substrings with 1 and 0 grouped consecutively, the number of valid substring will be the minimum number of 0 and 1.
For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        s = s.replace('01', '0 1').replace('10', '1 0')
        s = list(map(len, s.split()))
        return sum([min(s[i], s[i-1]) for i in range(1, len(s))])
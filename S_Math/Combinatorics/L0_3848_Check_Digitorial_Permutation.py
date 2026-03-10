""" https://leetcode.com/problems/check-digitorial-permutation/
The sum of digit factorials is permutation-invariant (order doesn't matter).
So just compute the sum once and check if the result has the same digit multiset
as n. Leading zeros are handled implicitly: if the sum has fewer digits, the
Counters won't match.
"""


class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        A = list(map(int, str(n)))
        m = sum(factorial(x) for x in A)
        return Counter(str(m)) == Counter(str(n))

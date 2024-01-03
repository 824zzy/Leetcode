""" https://leetcode.com/problems/k-items-with-the-maximum-sum/
1. k<o ==> k
2. o<k<o+z ==> o
3. o<o+z<k<o+z+n ==> o-(k-o-z)
"""
# categorization
class Solution:
    def kItemsWithMaximumSum(self, o: int, z: int, n: int, k: int) -> int:
        if k<=o:
            return k
        elif k<=o+z:
            return o
        else:
            return o-(k-o-z)
        
        
# simulation
class Solution:
    def kItemsWithMaximumSum(self, o: int, z: int, n: int, k: int) -> int:
        ans = 0
        # pick o
        x = min(k, o)
        k -= x
        ans += x
        # pick z
        y = min(k, z)
        k -= y
        # pick n
        z = min(n, k)
        ans -= z
        return ans
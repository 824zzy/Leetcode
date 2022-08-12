""" https://leetcode.com/problems/poor-pigs/
Given D=15 and T=60, we can obtain:
1. 1 pig can verify [60//15+1] => 5 buckets
2. 2 pigs can verify [60//15+1] ^ 2 => 25 buckets
3. n pigs can verify [60//15+1] ^ n pigs.

Thus, we just need to make sure: [T//D+1] ** n >= buckets
"""
class Solution:
    def poorPigs(self, b: int, D: int, T: int) -> int:
        pigs = 0
        while (T//D+1)**pigs<b:
            pigs += 1
        return pigs
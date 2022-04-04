""" https://leetcode.com/problems/find-players-with-zero-or-one-losses/
use set and hash table to find players with zero and one losses
"""
class Solution:
    def findWinners(self, A: List[List[int]]) -> List[List[int]]:
        vals = set()
        for x, y in A:
            vals.add(x)
            vals.add(y)
        
        cnt = Counter([y for _, y in A])
        ans0 = vals-set(cnt.keys())
        ans1 = [k for k, v in cnt.items() if v==1]
        return [sorted(ans0), sorted(ans1)]
        
""" https://leetcode.com/problems/finding-3-digit-even-numbers/submissions/
ans.add(int(''.join(list(map(str, p)))))
"""
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        perms = list(permutations(digits, 3))
        ans = set()
        for x, y, z in perms:
            if x!=0 and not z&1: 
                ans.add(p[0]*100+p[1]*10+p[2])
        return sorted(ans)
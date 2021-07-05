""" L1
Gray code formula: i>>1)^i
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = []
        for i in range(2**n):
            ans.append((i>>1)^i)
        return ans
""" L0:
initial state: dp = [[1], [1, 1]]
transition: R[i-1] = dp[-1][i]+dp[-1][i-1]
"""
class Solution:
    def generate(self, n: int) -> List[List[int]]:
        if n==1: return [[1]]
        if n==2: return [[1], [1, 1]]
        dp = [[1], [1, 1]]
        for _ in range(n-2):
            R = [1]
            for i in range(1, len(dp[-1])):
                R.append(dp[-1][i]+dp[-1][i-1])
            dp.append(R+[1])
        return dp
""" https://leetcode.com/problems/random-flip-matrix/
reservoir sampling will TLE use randrange instead
"""
class Solution:
    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.A = set()
        
    def flip(self) -> List[int]:
        while 1:
            i = random.randint(0, self.m-1)
            j = random.randint(0, self.n-1)
            if (i, j) not in self.A:
                self.A.add((i, j))
                return (i, j)

    def reset(self) -> None:
        self.A = set()
""" Brute Force
"""


class Solution:
    def powerfulIntegers(self, x, y, bound):
        xs = {x**i for i in range(20) if x**i < bound}
        ys = {y**i for i in range(20) if y**i < bound}
        return list({i + j for i in xs for j in ys if i + j <= bound})


""" find lower bound by log
tricky part is how to deal with 1
"""


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        a = bound if x == 1 else int(math.log(bound, x)) + 1
        b = bound if y == 1 else int(math.log(bound, y)) + 1
        ans = []
        for i in range(a):
            for j in range(b):
                if x**i + y**j <= bound:
                    ans.append(x**i + y**j)
                if y == 1:
                    break
            if x == 1:
                break
        return list(set(ans))

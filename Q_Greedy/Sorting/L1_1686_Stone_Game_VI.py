""" https://leetcode.com/problems/stone-game-vi/
Nice explanation from lee215: https://leetcode.com/problems/stone-game-vi/discuss/969574/JavaC%2B%2BPython-Sort-by-Value-Sum
Assume a stone valued [a,b] for Alice and Bod.
Alice takes it, worth a for Alice,
Bob takes it, worth b for Bob,
we can also consider that it worth -b for Alice.
The difference will be a+b.
That's the reason why we need to sort based on a+b.
And Alice and Bob will take one most valued stone each turn.
"""


class Solution:
    def stoneGameVI(self, A: List[int], B: List[int]) -> int:
        S = sorted(list(zip(A, B)), key=sum)

        a_val, b_val = 0, 0
        for i, (a, b) in enumerate(S):
            if i & 1 == 0:
                a_val += a
            else:
                b_val += b

        if a_val > b_val:
            return 1
        elif a_val < b_val:
            return -1
        else:
            return 0

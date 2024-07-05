""" https://leetcode.com/problems/design-bitset/
a comprehensive bit operations problem
"""


class Bitset:
    def __init__(self, size: int):
        self.a = 0
        self.ones = 0
        self.size = size

    def fix(self, idx: int) -> None:
        if self.a & (1 << idx) == 0:
            self.a |= 1 << idx
            self.ones += 1

    def unfix(self, idx: int) -> None:
        if self.a & (1 << idx):
            self.a ^= 1 << idx
            self.ones -= 1

    def flip(self) -> None:
        self.a ^= (1 << self.size) - 1
        self.ones = self.size - self.ones

    def all(self) -> bool:
        return self.ones == self.size

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        a = bin(self.a)[2:]
        return a[::-1] + "0" * (self.size - len(a))


"""
https://leetcode.com/problems/design-bitset/discuss/1748431/Python3-Java-C%2B%2B-All-Operations-O(1)-or-Flipped-StringFlip-Flag

1. Flipping can be done using a is_flip flag, is_flip stores whether the current bitset has to be flipped.
2. Keep a count variable ones that counts the number of ones in the bitset. This has to be updated in fix, unfix, and flip functions.
"""


class Bitset:
    def __init__(self, size: int):
        self.l = [0] * size
        self.ones = 0
        self.is_flip = False

    def fix(self, idx: int) -> None:
        if self.is_flip:
            if self.l[idx] == 1:
                self.ones += 1
            self.l[idx] = 0
        else:
            if self.l[idx] == 0:
                self.ones += 1
            self.l[idx] = 1

    def unfix(self, idx: int) -> None:
        if self.is_flip:
            if self.l[idx] == 0:
                self.ones -= 1
            self.l[idx] = 1
        else:
            if self.l[idx] == 1:
                self.ones -= 1
            self.l[idx] = 0

    def flip(self) -> None:
        self.is_flip = not self.is_flip
        self.ones = len(self.l) - self.ones

    def all(self) -> bool:
        return self.ones == len(self.l)

    def one(self) -> bool:
        return self.ones > 0

    def count(self) -> int:
        return self.ones

    def toString(self) -> str:
        return (
            "".join([str(0 if i else 1) for i in self.l])
            if self.is_flip
            else "".join([str(i) for i in self.l])
        )

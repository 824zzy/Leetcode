""" L0: https://leetcode.com/problems/simple-bank-system/
bank as a list
"""
class Bank:
    def __init__(self, balance: List[int]):
        self.B = balance

    def transfer(self, a1: int, a2: int, m: int) -> bool:
        if 0<=a1-1<len(self.B) and 0<=a2-1<len(self.B) and self.B[a1-1]>=m:
            self.B[a1-1] -= m
            self.B[a2-1] += m
            return True
        return False

    def deposit(self, a: int, m: int) -> bool:
        if 0<=a-1<len(self.B):
            self.B[a-1] += m
            return True
        return False

    def withdraw(self, a: int, m: int) -> bool:
        if 0<=a-1<len(self.B) and self.B[a-1]>=m:
            self.B[a-1] -= m
            return True
        return False
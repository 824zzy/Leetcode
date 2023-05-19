""" https://leetcode.com/problems/insert-delete-getrandom-o1/
"""
from header import *

class RandomizedSet:

    def __init__(self):
        self.V = []
        self.M = {}
        
    def insert(self, val: int) -> bool:
        if val in self.M: return False
        self.M[val] = len(self.V) # len(self.V) as index
        self.V.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.M: return False
        idx = self.M[val]
        self.M[self.V[-1]] = idx
        self.V[idx] = self.V[-1]
        self.V.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.V)
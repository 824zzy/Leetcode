""" https://leetcode.com/problems/insert-delete-getrandom-o1/
"""
from header import *

class RandomizedSet:

    def __init__(self):
        self.loc = {} # val-to-index mapping
        self.vals = []

    def insert(self, val: int) -> bool:
        if val in self.loc: return False 
        self.loc[val] = len(self.vals)
        self.vals.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val not in self.loc: return False 
        i = self.loc[val] 
        self.loc[self.vals[-1]] = i 
        self.loc.pop(val)
        self.vals[i] = self.vals[-1]
        self.vals.pop()
        return True 
 
    def getRandom(self) -> int:
        return choice(self.vals)
""" https://leetcode.com/problems/design-hashset/
"""
class MyHashSet:
    def __init__(self):
        self.set = set()
        
    def add(self, x: int) -> None:
        self.set.add(x)

    def remove(self, x: int) -> None:
        if x in self.set:
            self.set.remove(x)
        
    def contains(self, x: int) -> bool:
        return x in self.set
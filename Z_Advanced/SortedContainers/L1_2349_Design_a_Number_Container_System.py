""" https://leetcode.com/problems/design-a-number-container-system/
1. two hash tables to store index to value and value to index.
2. use a sorted list to ensure the indexes are increasing.
"""
from sortedcontainers import SortedList
class NumberContainers:
    def __init__(self):
        self.v2i = defaultdict(SortedList)
        self.i2v = {}
        
    def change(self, i: int, v: int) -> None:
        if i in self.i2v: self.v2i[self.i2v[i]].remove(i)
        self.i2v[i] = v
        self.v2i[v].add(i)    
        

    def find(self, v: int) -> int:
        if len(self.v2i[v])==0: return -1
        else: return self.v2i[v][0]


# if sortedcontainers is not installed, use the following code:
class NumberContainers:
    def __init__(self):
        self.v2i = defaultdict(list)
        self.i2v = {}
        
    def change(self, i: int, v: int) -> None:
        if i not in self.i2v:
            self.i2v[i] = v
            k = bisect_left(self.v2i[v], i)
            if k==len(self.v2i[v]): self.v2i[v].append(i)
            else: self.v2i[v].insert(k, i)
        else:
            pre_v = self.i2v[i]
            self.v2i[pre_v].remove(i)
            k = bisect_left(self.v2i[v], i)
            if k==len(self.v2i[v]): self.v2i[v].append(i) 
            else: self.v2i[v].insert(k, i)
            self.i2v[i] = v
        return
        
    def find(self, v: int) -> int:
        if len(self.v2i[v])==0: return -1
        else: return self.v2i[v][0]
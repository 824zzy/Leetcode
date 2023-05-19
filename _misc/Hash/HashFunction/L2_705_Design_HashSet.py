""" https://leetcode.com/problems/design-hashset/
Multiplicative hashing:  https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing

h(K) = (aK mod 2**w) / 2**(w-m), where K is key, a is big prime number, m is length of output(10000), w is size of machine word
"""
class MyHashMap:
    def __init__(self):
        self.A = [[] for _ in range(2**15)]
        
    def mul_hash(self, key):
        return (1031237*key%(2**20))//2**5

    def put(self, key: int, value: int) -> None:
        hs = self.mul_hash(key)
        for i, (k, v) in enumerate(self.A[hs]):
            if k==key: 
                self.A[hs][i] = (key, value)
                return
        self.A[hs].append((key, value))

    def get(self, key: int) -> int:
        hs = self.mul_hash(key)
        for i, (k, v) in enumerate(self.A[hs]):
            if k==key: return v
        return -1
        

    def remove(self, key: int) -> None:
        hs = self.mul_hash(key)
        for i, (k, v) in enumerate(self.A[hs]):
            if k==key: self.A[hs].remove((k, v))
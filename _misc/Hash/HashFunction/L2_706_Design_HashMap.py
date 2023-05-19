""" https://leetcode.com/problems/design-hashmap/
Multiplicative hashing:  https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing

h(K) = (aK mod 2**w) / 2**(w-m), where K is key, a is big prime number, m is length of output(10000), w is size of machine word
""" 
class MyHashMap:
    def __init__(self):
        self.M = {}
        
    def put(self, key: int, value: int) -> None:
        self.M[key] = value
        
    def get(self, key: int) -> int:
        if key in self.M: return self.M[key]
        else: return -1
        
    def remove(self, key: int) -> None:
        if key in self.M: del self.M[key]
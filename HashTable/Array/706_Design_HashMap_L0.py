# Simply design problem
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
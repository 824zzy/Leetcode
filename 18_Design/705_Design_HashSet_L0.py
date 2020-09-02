class MyHashSet:
    def __init__(self):
        self.val = [False] * (1000000-1)
        

    def add(self, key: int) -> None:
        self.val[key] = True

    def remove(self, key: int) -> None:
        self.val[key] = False

    def contains(self, key: int) -> bool:
        return self.val[key]
    
    
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = set()

    def add(self, key: int) -> None:
        self.s.add(key)

    def remove(self, key: int) -> None:
        if key in self.s:
            self.s.remove(key)
            
    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return True if key in self.s else False

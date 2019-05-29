from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self._ordered_dict = OrderedDict()
        self._capacity = capacity
        
    def get(self, key: int) -> int:
        self.move_to_end_if_exist(key)
        return self._ordered_dict.get(key, -1)
        
    def put(self, key: int, value: int) -> None:
        self.move_to_end_if_exist(key)
        
        self._ordered_dict[key] = value
        if len(self._ordered_dict) > self._capacity:
            self._ordered_dict.popitem(last=False)
            
    def move_to_end_if_exist(self, key:int) -> None:
        if key in self._ordered_dict:
            self._ordered_dict.move_to_end(key)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
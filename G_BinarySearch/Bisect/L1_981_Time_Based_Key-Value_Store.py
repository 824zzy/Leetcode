""" https://leetcode.com/problems/time-based-key-value-store/
1. store key and value and timestamp in a hash table
2. use customized compare function to find the index of the timestamp
"""
from header import *


class TimeMap:
    def __init__(self):
        self.mp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mp[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        idx = bisect_right(self.mp[key], timestamp, key=lambda x: x[0])
        if idx:
            return self.mp[key][idx - 1][1]
        else:
            return ""


"""
["TimeMap","set","get","get","set","get","get"]
[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
["TimeMap","set","set","get","set","get","get"]
[[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
"""

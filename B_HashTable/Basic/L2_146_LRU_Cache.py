""" https://leetcode.com/problems/lru-cache/
Two approaches:

Solution 1 (Pythonic, ordered-dict trick):
Python dicts preserve insertion order, so pop+reinsert moves a key to the
"most recent" end. Evict by popping the first key when over capacity.

Solution 2 (textbook, hashmap + doubly-linked list):
Circular doubly-linked list with a dummy sentinel keeps the most-recent at
the front and the least-recent at the back. Hashmap maps key -> node so
get/put are both O(1). This is the canonical interview answer.
"""


class LRUCache:
    def __init__(self, capacity: int):
        self.A = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.A:
            res = self.A.pop(key)
            self.A[key] = res
            return res
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.A:
            self.A.pop(key)
        elif self.cap == len(self.A):
            # or: self.A.pop(list(self.A.keys())[0]) but slower
            self.A.pop(next(iter(self.A.keys())))
        self.A[key] = value


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class LRUCache2:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dummy = Node()
        self.dummy.prev = self.dummy
        self.dummy.next = self.dummy
        self.key_to_node = {}

    def remove(self, x):
        x.prev.next = x.next
        x.next.prev = x.prev

    def push_front(self, x):
        x.prev = self.dummy
        x.next = self.dummy.next
        x.prev.next = x
        x.next.prev = x

    def get_node(self, key):
        if key not in self.key_to_node:
            return None
        node = self.key_to_node[key]
        self.remove(node)
        self.push_front(node)
        return node

    def get(self, key: int) -> int:
        node = self.get_node(key)
        return node.val if node else -1

    def put(self, key: int, value: int) -> None:
        node = self.get_node(key)
        if node:
            node.val = value
            return
        node = Node(key, value)
        self.key_to_node[key] = node
        self.push_front(node)
        if len(self.key_to_node) > self.capacity:
            back_node = self.dummy.prev
            del self.key_to_node[back_node.key]
            self.remove(back_node)

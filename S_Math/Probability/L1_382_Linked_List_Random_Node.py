""" https://leetcode.com/problems/linked-list-random-node/
"""
from header import *

# Reservoir Sampling


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        ans, cnt = 0, 0
        node = self.head
        while node:
            cnt += 1
            p = random.random()
            if p < 1 / cnt:
                ans = node.val
            node = node.next
        return ans

# straightforward solution


class Solution:
    def __init__(self, head: ListNode):
        self.head = head
        self.val = []
        self.l = 0
        dummy = head
        while dummy:
            self.val.append(dummy.val)
            dummy = dummy.next
            self.l += 1

    def getRandom(self) -> int:
        idx = random.randint(0, self.l - 1)
        return self.val[idx]

""" https://leetcode.com/problems/delete-node-in-a-linked-list/
dont think about previous node, just change the value of current node

1. carry over the value of next node;
2. delete next node.
"""


class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

""" L1: https://leetcode.com/problems/delete-node-in-a-linked-list/
1. carry over the value of next node;
2. delete next node.
"""
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
""" https://leetcode.com/problems/copy-list-with-random-pointer/submissions/
linked list + hash table
1. use a hashmap to map the original node to its copy.
2. two passes traverses to build deep copy
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':        
        ans = node = Node(-1)
        orig = head
        seen = {}
        while orig:
            node.next = Node(orig.val)
            node = node.next
            seen[orig] = node
            orig = orig.next
        
        node = ans.next
        orig = head
        while orig:
            if orig.random: node.random = seen[orig.random]
            else: node.random = None
            node = node.next
            orig = orig.next
        
        return ans.next
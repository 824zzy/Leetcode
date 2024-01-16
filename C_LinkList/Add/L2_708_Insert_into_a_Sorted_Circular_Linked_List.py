""" https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/
"""
from header import *

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head: 
            ans = Node(val=insertVal)
            ans.next = ans
            return ans
        
        pre, node = head, head.next
        while True:
            if pre.val <= insertVal <= node.val: break 
            if pre.val > node.val and (insertVal < node.val or pre.val < insertVal): break
            pre, node = pre.next, node.next
            if pre==head: break
        tmp = Node(insertVal)
        pre.next = tmp
        tmp.next = node
        return head
    
"""
[3,4,1]
2
[]
1
[1]
0
[3,3,3]
0
[1,3,5]
0
[1,3,5]
6
[3,3,5]
0
"""
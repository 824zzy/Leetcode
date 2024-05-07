# Link List

## Template

``` py
def linklist_template(self, head: ListNode) -> ListNode:
    pre = ans = ListNode('inf')
    pre.next = head
    cur = head
    while `condition`: # mostly `cur` or `cur and cur.next`
        'logic to delete, insert, etc.'
    return ans.next
```

## Reverse Linked List

``` py
# l, r, m = m, l, r 
pre = None
while head: 
    pre, head.next, head = head, pre, head.next
return pre
```

### Iteratively

``` py
class Solution(object):
    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            pre, pre.next, cur = cur, pre, cur.next
        return pre
        # Another form
        pre, cur = None, head
        while cur:
            tmp = cur
            cur = cur.next
            tmp.next = pre
            pre = tmp
        return pre
```

### Recursively

``` py
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        N = self.reverseList(head.next)
        head.next.next = head.next
        head.next = None
        return N
```

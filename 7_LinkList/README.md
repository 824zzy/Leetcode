# Notes

## Hints

1. Transform linklist to stack/queue can be shortcut.
2. For some problems, it is helpful to create a dummy node and return the `dummy.next`.
3. Delete node: `if node.next.val==val: node.next = node.next.next`
4. Reverse linked list:

    ``` py
    prev = None
    while head: prev, head.next, head = head, prev, head.next
    return prev
    ```

## Template

``` py
def linklist_template(self, head: ListNode) -> ListNode:
    prev = ans = ListNode('inf')
    prev.next = head
    curr = head
    while `condition`: # mostly `curr` or `curr and curr.next`
        'logic to delete, insert, etc.'
    return ans.next
```

## Reverse

### Iteratively

``` py
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            prev, prev.next, curr = curr, prev, curr.next
        return prev
        # Another form
        prev, curr = None, head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        return prev
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

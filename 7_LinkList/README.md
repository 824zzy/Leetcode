# Notes

## Hints

1. Transform linklist to stack/queue can be shortcut.

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

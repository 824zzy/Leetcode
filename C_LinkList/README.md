# Linked List

## When to Use

| Problem Signal | Technique |
|---|---|
| Find middle node, check cycle | Fast-slow pointers |
| Remove nth node from end | Fast-slow pointers (n-step gap) |
| Detect cycle start | Fast-slow pointers + Floyd's algorithm |
| Partition into two lists (even/odd, < x, etc.) | Two dummy nodes |
| Reverse entire list or sublist | Iterative reversal (prev, curr, next) |
| Reorder list (1→n→2→n-1→...) | Find middle + reverse second half + merge |
| Merge k sorted lists | Min heap or divide & conquer |
| Delete node(s) matching condition | Dummy head + pointer adjustment |
| Copy list with random pointers | Hash table (original → copy mapping) |
| Swap adjacent pairs or groups | Pointer swapping with dummy head |
| Find intersection of two lists | Two pointers (A→B and B→A traversal) |
| Insert into sorted list | Find insertion point + pointer rewiring |
| Check palindrome | Fast-slow to find middle + reverse second half |

## Dummy Head Pattern

Key insight: A dummy head (sentinel node) simplifies edge cases when you might modify the actual head.

Use when:
- Deleting nodes (including potentially the head)
- Inserting nodes at arbitrary positions
- Swapping or reordering nodes

### Template

```py
def linkedlist_template(self, head: ListNode) -> ListNode:
    ans = pre = ListNode(next=head)  # or ListNode(0, head)
    cur = head
    while cur:  # or cur and cur.next, depending on problem
        # logic to delete, insert, swap, etc.
        # adjust pre and cur pointers
        pass
    return ans.next
```

**LC refs:** 21, 83, 86, 203, 237, 708, 2181, 3217

## Fast-Slow Pointers

Key insight: Two pointers moving at different speeds can detect cycles, find midpoints, or locate positions relative to the end.

### Find Middle Node

Move fast by 2 steps and slow by 1. When fast reaches the end, slow is at the middle.

For even-length lists, returns the second middle node.

```py
def middleNode(self, head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow
```

**LC refs:** 876, 143, 234, 2095, 2130

### Remove nth from End

Use a gap of n steps between fast and slow.

```py
def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    ans = fast = slow = ListNode(next=head)
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return ans.next
```

**LC refs:** 19

### Detect Cycle

If fast meets slow, there's a cycle. Otherwise fast reaches None.

```py
def hasCycle(self, head: ListNode) -> bool:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False
```

**LC refs:** 141

### Detect Cycle Start (Floyd's Algorithm)

After detecting a cycle, reset one pointer to head and move both by 1 step. They meet at the cycle entrance.

```py
def detectCycle(self, head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            # reset one pointer to head
            fast = head
            while fast != slow:
                fast = fast.next
                slow = slow.next
            return slow
    return None
```

**LC refs:** 142

### Reorder List (1→n→2→n-1→...)

1. Find middle with fast-slow
2. Reverse second half
3. Merge two halves by alternating

```py
def reorderList(self, head: ListNode) -> None:
    # find middle
    fast = slow = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # reverse second half
    prev = None
    while slow:
        prev, slow.next, slow = slow, prev, slow.next

    # merge
    node = head
    while prev and prev.next:
        node.next, node = prev, node.next
        prev.next, prev = node, prev.next
```

**LC refs:** 143

### Intersection of Two Lists

Traverse A→B and B→A simultaneously. They meet at the intersection (or None if no intersection).

```py
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    nodeA, nodeB = headA, headB
    while nodeA != nodeB:
        nodeA = nodeA.next if nodeA else headB
        nodeB = nodeB.next if nodeB else headA
    return nodeA
```

**LC refs:** 160

### Palindrome Check

Find middle + reverse second half + compare both halves.

```py
def isPalindrome(self, head: ListNode) -> bool:
    # find middle
    fast = slow = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # reverse second half
    prev = None
    while slow:
        prev, slow.next, slow = slow, prev, slow.next

    # compare
    while prev:
        if prev.val != head.val:
            return False
        prev, head = prev.next, head.next
    return True
```

**LC refs:** 234

## Reversal

Key insight: Reverse by rewiring pointers. Track prev, curr, and next.

### Reverse Entire List (Iterative)

The one-liner version using tuple unpacking (left, right, mid = mid, left, right):

```py
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    while head:
        prev, head.next, head = head, prev, head.next
    return prev
```

The more readable version:

```py
def reverseList(self, head: ListNode) -> ListNode:
    prev = None
    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev
```

**LC refs:** 206

### Reverse Entire List (Recursive)

```py
def reverseList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

### Reverse Sublist [left, right]

1. Locate the node before left
2. Reverse nodes from left to right
3. Reconnect the reversed segment

```py
def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    ans = node = ListNode(next=head)

    # locate the left position node
    prev = None
    for _ in range(left):
        prev = node
        node = node.next

    # reverse nodes in the middle
    pp, nn = prev, node
    for _ in range(left, right + 1):
        nxt = node.next
        node.next = prev
        prev = node
        node = nxt

    # reconnect the reversed nodes
    pp.next = prev
    nn.next = node
    return ans.next
```

**LC refs:** 92

### Reverse in k-Group

Reverse every k nodes. If fewer than k nodes remain at the end, leave them as is.

Common approach: use a stack of size k to batch-reverse.

```py
def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    node = head
    stk = []
    while node:
        pre = node
        while pre and len(stk) < k:
            stk.append(pre.val)
            pre = pre.next
        if len(stk) != k:
            break
        while stk:
            node.val = stk.pop()
            node = node.next
    return head
```

**LC refs:** 25

## Delete Node

Key insight: Use a dummy head to handle edge cases where the head itself is deleted.

### Remove All Occurrences of Value

```py
def removeElements(self, head: ListNode, val: int) -> ListNode:
    ans = pre = ListNode(next=head)
    cur = head
    while cur:
        if cur.val == val:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return ans.next
```

**LC refs:** 203, 3217

### Remove Duplicates (Keep One)

For a sorted list, skip nodes with the same value as the previous.

```py
def deleteDuplicates(self, head: ListNode) -> ListNode:
    ans = pre = ListNode(next=head)
    cur = head
    while cur:
        if cur.val == pre.val:
            pre.next = cur.next
        else:
            pre = cur
        cur = cur.next
    return ans.next
```

**LC refs:** 83

### Remove Duplicates (Remove All)

For a sorted list, if a node has duplicates, skip all occurrences.

```py
def deleteDuplicates(self, head: ListNode) -> ListNode:
    ans = pre = ListNode(next=head)
    while head:
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            pre.next = head.next
        else:
            pre = pre.next
        head = head.next
    return ans.next
```

**LC refs:** 82

### Delete Node (Given Node Only)

When you can't access the previous node, copy the next node's value and skip the next node.

```py
def deleteNode(self, node: ListNode) -> None:
    node.val = node.next.val
    node.next = node.next.next
```

**LC refs:** 237

## Merge and Partition

### Merge Two Sorted Lists

Use a dummy head and always append the smaller node.

```py
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    ans = dummy = ListNode()
    while l1 and l2:
        if l1.val < l2.val:
            ans.next = l1
            l1 = l1.next
        else:
            ans.next = l2
            l2 = l2.next
        ans = ans.next
    ans.next = l1 if l1 else l2
    return dummy.next
```

**LC refs:** 21

### Merge k Sorted Lists

Use a min heap to track the smallest head among all lists.

```py
def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    h = [(node.val, i, node) for i, node in enumerate(lists) if node]
    heapify(h)
    ans = cur = ListNode()
    while h:
        val, i, node = heappop(h)
        cur.next = node
        cur = cur.next
        if node.next:
            heappush(h, (node.next.val, i, node.next))
    return ans.next
```

**LC refs:** 23

### Partition List (Separate by Condition)

Use two dummy nodes to build two separate lists, then connect them.

```py
def partition(self, head: ListNode, x: int) -> ListNode:
    left = dummy_left = ListNode()
    right = dummy_right = ListNode()
    while head:
        if head.val < x:
            left.next = head
            left = left.next
        else:
            right.next = head
            right = right.next
        head = head.next
    right.next = None  # important: avoid cycle
    left.next = dummy_right.next
    return dummy_left.next
```

**LC refs:** 86, 328 (odd/even), 2181 (merge between zeros)

### Odd-Even List

Partition into odd-indexed and even-indexed nodes, then connect.

```py
def oddEvenList(self, head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    odd = head
    even = even_head = head.next
    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next
    odd.next = even_head
    return head
```

**LC refs:** 328

## Swap Nodes

Key insight: Swapping in a linked list means rewiring pointers, not swapping values (unless the problem allows it).

### Swap Adjacent Pairs

Swap every two adjacent nodes. Use a dummy head.

```py
def swapPairs(self, head: ListNode) -> ListNode:
    ans = pre = ListNode(next=head)
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        # pre → a → b → ... becomes pre → b → a → ...
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return ans.next
```

**LC refs:** 24

### Swap Nodes by Position (kth from Start and End)

Locate both nodes and swap their values (or rewire pointers if value swap is not allowed).

```py
def swapNodes(self, head: ListNode, k: int) -> ListNode:
    # find kth from start
    node = head
    for _ in range(k - 1):
        node = node.next
    first = node

    # find kth from end (move node to end, use slow pointer)
    slow = head
    while node.next:
        node = node.next
        slow = slow.next
    second = slow

    # swap values
    first.val, second.val = second.val, first.val
    return head
```

**LC refs:** 1721

## Copy with Random Pointer

Key insight: Use a hash table to map original nodes to their copies. Two passes: first copy structure, then copy random pointers.

```py
def copyRandomList(self, head: Node) -> Node:
    if not head:
        return None

    # first pass: copy all nodes
    seen = {}
    node = head
    while node:
        seen[node] = Node(node.val)
        node = node.next

    # second pass: copy next and random pointers
    node = head
    while node:
        if node.next:
            seen[node].next = seen[node.next]
        if node.random:
            seen[node].random = seen[node.random]
        node = node.next

    return seen[head]
```

**LC refs:** 138

## Insert into Sorted List

Find the insertion point and rewire pointers.

### Insert into Sorted Circular List

Handle edge cases: empty list, insert at min/max boundary, insert in the middle.

```py
def insert(self, head: Node, insertVal: int) -> Node:
    if not head:
        node = Node(insertVal)
        node.next = node
        return node

    prev, curr = head, head.next
    while True:
        # case 1: insert in the middle
        if prev.val <= insertVal <= curr.val:
            break
        # case 2: insert at min/max boundary
        if prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val):
            break
        # case 3: all nodes have same value
        if curr == head:
            break
        prev, curr = curr, curr.next

    prev.next = Node(insertVal, curr)
    return head
```

**LC refs:** 708

### Insertion Sort List

For each node, find its correct position in the sorted prefix and insert it there.

```py
def insertionSortList(self, head: ListNode) -> ListNode:
    ans = node = ListNode(-inf, next=head)
    while node.next:
        if node.val <= node.next.val:
            node = node.next
        else:
            tmp = node.next
            pre = ans
            while pre.next and pre.next.val <= tmp.val:
                pre = pre.next
            node.next = tmp.next
            tmp.next = pre.next
            pre.next = tmp
    return ans.next
```

**LC refs:** 147

## Rotate List

Key insight: Find the new tail (length - k % length - 1 from start), break the list there, and reconnect.

```py
def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head or k == 0:
        return head

    # find length and tail
    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    # effective rotation
    k = k % length
    if k == 0:
        return head

    # find new tail
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    return new_head
```

**LC refs:** 61

## Split List into Parts

Divide the list into k parts with at most 1 node difference between parts.

```py
def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
    # find length
    length = 0
    node = head
    while node:
        length += 1
        node = node.next

    # calculate part sizes
    q, r = divmod(length, k)

    ans = []
    node = head
    for i in range(k):
        ans.append(node)
        part_size = q + (1 if i < r else 0)
        for _ in range(part_size - 1):
            if node:
                node = node.next
        if node:
            node.next, node = None, node.next

    return ans
```

**LC refs:** 725

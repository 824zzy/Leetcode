---
tags:
  - leetcode
  - stack
  - moc
---

# Stack

## When to Use

| Problem Signal | Technique |
|---|---|
| Find next greater/smaller element for each index | Monotonic stack |
| Find distance to next greater/smaller element | Monotonic stack (store indices) |
| Sum/max over all subarrays using min/max as pivot | Monotonic stack (find left/right boundaries) |
| Largest rectangle in histogram | Monotonic increasing stack (find boundaries) |
| Remove k digits to make smallest number | Monotonic increasing stack + greedy |
| Remove duplicates keeping lexicographically smallest | Monotonic increasing stack + greedy |
| Maximum width ramp (i < j, A[i] <= A[j]) | Farmost smaller/greater pattern |
| Longest well-performing interval | Farmost smaller/greater + prefix sum |
| Valid parentheses matching/balancing | Stack (track unmatched) or counter optimization |
| Expression evaluation (calculator) | Stack for operands/operators |
| Decode/encode nested structures | Stack for context |
| Iterative tree traversal (pre/in/post-order) | Stack to simulate recursion |

## Monotonic Stack

Key insight: Monotonic stack finds the next greater/smaller element in O(n). Each element is pushed and popped at most once.

Rule of thumb: **Use monotonic increasing stack to find next smaller elements, monotonic decreasing stack to find next greater elements.**

In templates below, `A[stk[-1]] > A[i]` indicates a monotonic increasing stack (values decrease from bottom to top).

### Basic Template

LC 739, 496, 503, 901, 1019

```py
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]] ? A[i]:
        # pop elements that violate monotonic property
        # process popped element (e.g., record distance, accumulate answer)
        stk.pop()
    # process current element using stack top
    stk.append(i)
return ans
```

### Find Next Smaller Elements (Two Pass)

LC 84, 907, 1856, 2104

Use monotonic increasing stack (`A[stk[-1]] > A[i]` pops).

```py
# next smaller on the right
R = [len(A)] * len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]] > A[i]:
        R[stk.pop()] = i
    stk.append(i)

# next smaller on the left
L = [-1] * len(A)
stk = []
for i in reversed(range(len(A))):
    while stk and A[stk[-1]] >= A[i]:
        L[stk.pop()] = i
    stk.append(i)
```

Note: Use `>=` on one side to handle duplicates correctly (avoid double-counting in problems like LC 907).

### Find Next Greater Elements (Two Pass)

LC 42, 2454

Use monotonic decreasing stack (`A[stk[-1]] < A[i]` pops).

```py
# next greater on the right
R = [len(A)] * len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]] < A[i]:
        R[stk.pop()] = i
    stk.append(i)

# next greater on the left
L = [-1] * len(A)
stk = []
for i in reversed(range(len(A))):
    while stk and A[stk[-1]] <= A[i]:
        L[stk.pop()] = i
    stk.append(i)
```

### Application: Largest Rectangle in Histogram

LC 84, 85

Key insight: For each bar as the minimum height, find the maximum width by locating the next smaller bar on both sides.

```py
# find next smaller on both sides (as above)
L = [-1] * len(A)
R = [len(A)] * len(A)
# ... (use monotonic increasing stack)

# for each A[i] as minimum height
ans = 0
for i, (l, r) in enumerate(zip(L, R)):
    width = r - l - 1
    ans = max(ans, A[i] * width)
return ans
```

### Application: Sum of Subarray Minimums

LC 907, 2104

Key insight: For each element as the minimum, count how many subarrays include it as the min, then sum up contribution.

```py
# find next smaller on both sides
L = [-1] * len(A)
R = [len(A)] * len(A)
# ... (use monotonic increasing stack)

ans = 0
for i, (l, r) in enumerate(zip(L, R)):
    left_count = i - l
    right_count = r - i
    ans += A[i] * left_count * right_count
return ans % (10**9 + 7)
```

### Greedy + Monotonic Stack

LC 402, 316, 1081, 1673, 2030

Pattern: Remove k elements to get the lexicographically smallest/largest result.

Key insight: Maintain a monotonic increasing stack (for smallest) or decreasing stack (for largest). Pop greedily when beneficial and quota k allows.

```py
stk = []
for i, x in enumerate(A):
    while stk and stk[-1] > x and k > 0:
        stk.pop()
        k -= 1
    stk.append(x)
# remove remaining k elements from the end
return stk[: -k or None]
```

For "remove duplicate letters" (LC 316, 1081), also track remaining count and visited set.

## Farmost Smaller/Greater Monotonic Stack

LC 962, 1124

Key insight: Find the maximum distance between indices i < j where A[i] <= A[j] (or some comparison).

Two-pass approach:
1. Build monotonic decreasing stack (left to right) to store candidate left boundaries.
2. Scan right to left, pop stack when condition met, update max distance.

```py
stk = []
for i in range(len(A)):
    if not stk or A[stk[-1]] > A[i]:
        stk.append(i)

ans = 0
for i in reversed(range(len(A))):
    while stk and A[stk[-1]] <= A[i]:
        ans = max(ans, i - stk.pop())
return ans
```

Variation (LC 1124 with prefix sum): Transform array with prefix sum, then apply the template to find longest well-performing interval.

## Parentheses Optimization

Key insight: For simple parentheses validation/balancing, a counter often suffices instead of a full stack.

### Stack Approach (General)

LC 20, 1021, 1249

Use when tracking actual positions or performing structural operations.

```py
stk = []
for c in s:
    if c == '(':
        stk.append(c)
    else:
        if not stk:
            # unmatched closing
        else:
            stk.pop()
# remaining in stack are unmatched opening
```

### Counter Optimization

LC 921, 1963, 2116

Use when only counting imbalance, not tracking positions.

```py
open_count = 0
unmatched_close = 0
for c in s:
    if c == '(':
        open_count += 1
    else:
        open_count -= 1
        if open_count < 0:
            open_count = 0
            unmatched_close += 1
return unmatched_close + open_count
```

### Longest Valid Parentheses

LC 32

Key insight: Scan left to right (catches all valid except those ending early), then right to left (catches those missed).

```py
ans = left = right = 0
for c in s:
    if c == '(':
        left += 1
    else:
        right += 1
    if left == right:
        ans = max(ans, 2 * right)
    elif right > left:
        left = right = 0

left = right = 0
for c in reversed(s):
    if c == '(':
        left += 1
    else:
        right += 1
    if left == right:
        ans = max(ans, 2 * left)
    elif left > right:
        left = right = 0
return ans
```

### Score of Parentheses

LC 856

Stack tracks the score at each nesting level.

```py
stk = [0]
for c in s:
    if c == '(':
        stk.append(0)
    else:
        val = stk.pop()
        stk[-1] += max(2 * val, 1)
return stk[0]
```

## Expression Evaluation

LC 224, 227, 394

### Basic Calculator (+ - and parentheses)

LC 224

Key insight: Stack stores the previous result and sign before entering a new parenthesis level.

```py
s = s.replace('+', ' + ').replace('-', ' - ').replace('(', ' ( ').replace(')', ' ) ').split()
stk = []
sign = 1
ans = 0
for token in s:
    if token == '+':
        sign = 1
    elif token == '-':
        sign = -1
    elif token == '(':
        stk.extend([ans, sign])
        ans = 0
        sign = 1
    elif token == ')':
        ans *= stk.pop()
        ans += stk.pop()
    else:
        ans += sign * int(token)
return ans
```

### Decode String

LC 394

Stack stores the previous string and the repeat count before entering a new bracket level.

```py
stk = []
ans = num = ""
for c in s:
    if c.isalpha():
        ans += c
    elif c.isdigit():
        num += c
    elif c == '[':
        stk.append(num)
        stk.append(ans)
        ans = num = ""
    else:  # c == ']'
        ans = stk.pop() + ans * int(stk.pop())
return ans
```

## Iterative Tree Traversal

LC 94, 144, 145, 173

Use stack to simulate recursion. Different traversal orders require different visit/print timing.

### Preorder (Root, Left, Right)

```py
def preOrder(self, root):
    ans = []
    stk = []
    node = root
    while stk or node:
        if node:
            ans.append(node.val)
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            node = node.right
    return ans
```

### Inorder (Left, Root, Right)

```py
def inOrder(self, root):
    stk = []
    ans = []
    node = root
    while stk or node:
        if node:
            stk.append(node)
            node = node.left
        else:
            node = stk.pop()
            ans.append(node.val)
            node = node.right
    return ans
```

### Postorder (Left, Right, Root)

```py
def postOrder(self, root):
    if not root: return []
    stk1 = [root]
    stk2 = []
    ans = []
    while stk1:
        node = stk1.pop()
        if node.left: stk1.append(node.left)
        if node.right: stk1.append(node.right)
        stk2.append(node)
    while stk2: ans.append(stk2.pop().val)
    return ans
```

## Eulerian Path: Hierholzer's Algorithm

For directed connected graph, find a path that visits every edge exactly once.

Use case: Reconstruct itinerary (LC 332), construct original sequence from pairs.

```py
def hierholzer(pairs):
    G = defaultdict(list)
    degree = defaultdict(int)  # out-degree
    for i, j in pairs:
        G[i].append(j)
        degree[i] += 1
        degree[j] -= 1

    # find starting node (out-degree > in-degree)
    for n in degree:
        if degree[n] == 1:
            x = n
            break

    ans = []
    stk = [x]
    while stk:
        while G[stk[-1]]:
            stk.append(G[stk[-1]].pop())
        ans.append(stk.pop())
    ans.reverse()
    return [[ans[i], ans[i+1]] for i in range(len(ans)-1)]
```

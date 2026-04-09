# Tree BFS (Level-Order Traversal)

## When to Use

| Problem Signal | Technique |
|---|---|
| Process tree level by level | Standard level-order BFS |
| Need level information (depth, level sums) | Level-order BFS with step tracking |
| Rightmost/leftmost node at each level | Track first/last node in each level |
| Zigzag level order | Alternate reversing each level |
| Level aggregation (min, max, avg per level) | Collect level values, then aggregate |
| Connect nodes at same level | Level-order traversal with same-level linking |
| Binary tree serialization/deserialization | Level-order BFS for null handling |
| Find minimum depth | BFS stops at first leaf |
| Tree width (max nodes at any level) | Track max level size |
| Positional indexing (complete tree property) | Track column index: left = 2*i, right = 2*i+1 |

## Standard Level-Order BFS

Use for basic level-by-level traversal.

LC 102, 107, 637, 515, 1161

```py
def level_order(root):
    if not root:
        return []

    Q = [root]
    result = []

    while Q:
        level = []
        for _ in range(len(Q)):
            node = Q.pop(0)
            level.append(node.val)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        result.append(level)

    return result
```

## Zigzag Level Order

Use when you need to alternate direction at each level.

LC 103

**Key insight:** Use a flag to track level parity. Reverse every other level.

```py
def zigzag_level_order(root):
    if not root:
        return []

    Q = [root]
    result = []
    reverse = False

    while Q:
        level = []
        for _ in range(len(Q)):
            node = Q.pop(0)
            level.append(node.val)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)

        if reverse:
            result.append(level[::-1])
        else:
            result.append(level)
        reverse = not reverse

    return result
```

## Right Side View

Use when you need the rightmost node at each level.

LC 199

**Key insight:** The last node processed at each level is the rightmost visible node.

```py
def right_side_view(root):
    if not root:
        return []

    Q = [root]
    result = []

    while Q:
        result.append(Q[-1].val)  # last node in current level
        for _ in range(len(Q)):
            node = Q.pop(0)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)

    return result
```

For left side view, use `Q[0].val` (first node in level).

## Level Aggregation (Min, Max, Avg, Sum)

Use when you need statistics per level.

LC 637, 1161, 2583

```py
def average_of_levels(root):
    if not root:
        return []

    Q = [root]
    result = []

    while Q:
        level_sum = 0
        level_count = len(Q)
        for _ in range(level_count):
            node = Q.pop(0)
            level_sum += node.val
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        result.append(level_sum / level_count)

    return result
```

For max/min level sum (LC 1161, 2583):
```py
max_level_sum = max(sum(node.val for node in level) for level in levels)
```

For kth largest level sum (LC 2583), collect all level sums and sort.

## Connect Nodes at Same Level

Use when you need to link nodes horizontally (next pointers).

LC 116, 117

**Key insight:** At each level, link nodes left to right using their position in the queue.

```py
def connect(root):
    if not root:
        return None

    Q = [root]
    while Q:
        for i in range(len(Q)):
            node = Q.pop(0)
            # link to next node in same level
            if i < len(Q):  # note: len(Q) changes as we pop
                node.next = Q[0]
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)

    return root
```

**Alternative:** Process level by level with explicit level tracking:
```py
def connect(root):
    if not root:
        return None

    Q = [root]
    while Q:
        prev = None
        for _ in range(len(Q)):
            node = Q.pop(0)
            if prev:
                prev.next = node
            prev = node
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)

    return root
```

## Find Specific Level Nodes

### Bottom-left node
LC 513

**Key insight:** Last level's first node.

```py
def find_bottom_left_value(root):
    Q = [root]
    while Q:
        node = Q.pop(0)
        # reversed order: right then left
        if node.right:
            Q.append(node.right)
        if node.left:
            Q.append(node.left)
    return node.val  # last node processed
```

Alternative: track first node of each level, return the last one saved.

### Deepest leaves
LC 1302, 2415

```py
def deepest_leaves_sum(root):
    Q = [root]
    while Q:
        level_sum = sum(node.val for node in Q)
        next_Q = []
        for node in Q:
            if node.left:
                next_Q.append(node.left)
            if node.right:
                next_Q.append(node.right)
        if not next_Q:  # current level is deepest
            return level_sum
        Q = next_Q
```

## Minimum Depth

Use when you need the shortest path to a leaf.

LC 111

**Key insight:** BFS finds minimum depth naturally—stop at first leaf encountered.

```py
def min_depth(root):
    if not root:
        return 0

    Q = [root]
    depth = 1

    while Q:
        for _ in range(len(Q)):
            node = Q.pop(0)
            # first leaf we encounter is at minimum depth
            if not node.left and not node.right:
                return depth
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        depth += 1

    return depth
```

## Maximum Width

Use when you need the maximum number of nodes between leftmost and rightmost at any level (including nulls in between).

LC 662

**Key insight:** Assign column indices. Left child = 2*i, right child = 2*i+1. Width = rightmost_col - leftmost_col + 1.

```py
def width_of_binary_tree(root):
    if not root:
        return 0

    Q = [(root, 0)]  # (node, column_index)
    max_width = 0

    while Q:
        level_width = Q[-1][1] - Q[0][1] + 1
        max_width = max(max_width, level_width)

        for _ in range(len(Q)):
            node, col = Q.pop(0)
            if node.left:
                Q.append((node.left, 2 * col))
            if node.right:
                Q.append((node.right, 2 * col + 1))

    return max_width
```

**Optimization:** To prevent integer overflow on deep trees, normalize column indices by subtracting the leftmost column index at each level:
```py
leftmost_col = Q[0][1]
if node.left:
    Q.append((node.left, 2 * (col - leftmost_col)))
if node.right:
    Q.append((node.right, 2 * (col - leftmost_col) + 1))
```

## Tree Serialization/Deserialization

Use when you need to serialize a tree to string and reconstruct it.

LC 297, 449

**Key insight:** Level-order BFS naturally handles null nodes. Use delimiter (e.g., 'null') for missing children.

```py
def serialize(root):
    if not root:
        return ""

    Q = [root]
    result = []

    while Q:
        node = Q.pop(0)
        if node:
            result.append(str(node.val))
            Q.append(node.left)
            Q.append(node.right)
        else:
            result.append('null')

    # trim trailing nulls
    while result and result[-1] == 'null':
        result.pop()

    return ','.join(result)

def deserialize(data):
    if not data:
        return None

    values = data.split(',')
    root = TreeNode(int(values[0]))
    Q = [root]
    i = 1

    while Q and i < len(values):
        node = Q.pop(0)
        if values[i] != 'null':
            node.left = TreeNode(int(values[i]))
            Q.append(node.left)
        i += 1
        if i < len(values) and values[i] != 'null':
            node.right = TreeNode(int(values[i]))
            Q.append(node.right)
        i += 1

    return root
```

## Check Completeness

Use when you need to verify if a tree is complete (all levels full except possibly the last, which fills left to right).

LC 958

**Key insight:** In a complete tree, after encountering the first null, all remaining nodes must be null.

```py
def is_complete_tree(root):
    Q = [root]
    seen_null = False

    while Q:
        node = Q.pop(0)
        if node is None:
            seen_null = True
        else:
            if seen_null:
                return False
            Q.append(node.left)
            Q.append(node.right)

    return True
```

## Level-Order with Depth Tracking

Use when you need to know the depth of each node during traversal.

LC 1302, 1161, 2415

```py
def level_order_with_depth(root):
    if not root:
        return []

    Q = [(root, 0)]  # (node, depth)
    result = []

    while Q:
        node, depth = Q.pop(0)
        result.append((node.val, depth))
        if node.left:
            Q.append((node.left, depth + 1))
        if node.right:
            Q.append((node.right, depth + 1))

    return result
```

**Alternative:** Track depth separately without storing in queue (more memory efficient):
```py
def level_order_with_depth(root):
    if not root:
        return []

    Q = [root]
    depth = 0

    while Q:
        for _ in range(len(Q)):
            node = Q.pop(0)
            process(node, depth)
            if node.left:
                Q.append(node.left)
            if node.right:
                Q.append(node.right)
        depth += 1
```

## N-ary Tree Level Order

Use for trees where nodes can have arbitrary number of children.

LC 429, 589, 590

```py
def level_order(root):
    if not root:
        return []

    Q = [root]
    result = []

    while Q:
        level = []
        for _ in range(len(Q)):
            node = Q.pop(0)
            level.append(node.val)
            # N-ary: iterate through all children
            for child in node.children:
                Q.append(child)
        result.append(level)

    return result
```

## Key Insights

### BFS vs DFS for trees
- **BFS**: Level-order, minimum depth, width, serialization, same-level connections
- **DFS**: Maximum depth, path problems, tree structure validation, most tree recursion

### Queue initialization
Always check if root is None before initializing queue. Return appropriate empty value ([], 0, None).

### Level processing pattern
The `for _ in range(len(Q))` pattern processes exactly one level. Capture `len(Q)` before the loop—don't use `while Q` which would mix levels.

### Null handling
For serialization or completeness check, you may need to explicitly enqueue None values. Standard traversal skips nulls.

### Memory optimization
Level-order traversal uses O(w) space where w is maximum width of tree. For complete binary tree, w ≈ n/2 at bottom level. If memory is tight, consider DFS alternatives.

### Right-to-left vs left-to-right
- Right side view: process left-to-right, take last
- Bottom-left value: process right-to-left (reverse order), take last
- Both avoid needing to track explicit level boundaries

### Column indexing
When tracking positions (LC 662), use `2*col` and `2*col+1` for left/right children. Normalize at each level to prevent overflow on deep trees.

### Common mistakes
- Forgetting to check `if not root` before initializing queue
- Using `while Q` instead of `for _ in range(len(Q))` (mixes levels)
- Forgetting to append children to queue
- Off-by-one in depth counting (depth 0 or depth 1 for root?)
- Not handling the empty tree case in serialization

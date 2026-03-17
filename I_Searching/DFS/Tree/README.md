# Tree Depth First Search

## When to Use

| Problem Signal | Technique |
|---|---|
| Aggregate value from subtrees (height, sum, count) | Bottom-up DFS (postorder) |
| Path from root with specific property | Top-down DFS with state |
| Path sum equals target (any root-to-node path) | Prefix sum + DFS with backtracking |
| Max/min path value (not necessarily root-to-leaf) | Path aggregation (consider all local paths) |
| Diameter, longest path between any two nodes | Return max single-path, update global with left + right |
| Subtree must satisfy property (balanced, BST) | Return validity + metadata from subtrees |
| Node depends on depth from root | Top-down DFS passing depth |
| Node depends on deepest descendant | Bottom-up DFS returning depth |
| Serialize/identify duplicate subtrees | DFS with serialization (preorder or postorder) |
| Tree construction from traversals | Split by root, recurse on left/right |
| BST with cumulative values (greater sum tree) | Reverse inorder (right, root, left) |
| Convert tree to graph for bidirectional queries | DFS to build adjacency list, then BFS/DFS |
| Answer depends on node's position in entire tree | Rerooting (moving root technique) |
| Node as root vs different node as root | Rerooting DP (compute for one root, adjust for all) |
| State machine on tree (e.g., cameras, coloring) | Bottom-up with state encoding |

## DFS General Template

### Recursive (bottom-up / postorder)

Most tree problems. Process children first, then compute current node's answer.

```py
def dfs(node):
    if not node:
        return 0  # or None, or base case value
    l = dfs(node.left)
    r = dfs(node.right)
    # combine l, r to compute current node's result
    return result
```

**LC References:** 104, 110, 543, 124

### Recursive (top-down / preorder)

Use when you need to pass information from parent to children (like current path sum, depth).

```py
def dfs(node, parent_state):
    if not node:
        return
    # process node with parent_state
    dfs(node.left, updated_state)
    dfs(node.right, updated_state)
```

**LC References:** 257, 112, 129, 1448

### Iterative (preorder)

```py
stack = [root]
while stack:
    curr = stack.pop()
    # process curr
    if curr.right:
        stack.append(curr.right)
    if curr.left:
        stack.append(curr.left)
```

**LC References:** 144, 589

## Tree Traversal

### Recursive Traversals

```py
def preOrder(root):
    if not root:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

def inOrder(root):
    if not root:
        return
    inOrder(root.left)
    print(root.val)
    inOrder(root.right)

def postOrder(root):
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print(root.val)
```

**LC References:** 144 (preorder), 94 (inorder), 145 (postorder)

### Level Order (BFS)

```py
def levelOrder(root):
    if not root:
        return []
    Q = [root]
    result = []
    while Q:
        level = []
        nxtQ = []
        for node in Q:
            level.append(node.val)
            if node.left:
                nxtQ.append(node.left)
            if node.right:
                nxtQ.append(node.right)
        result.append(level)
        Q = nxtQ
    return result
```

**LC References:** 102, 107, 103, 199

## Height / Depth Problems

Key insight: height = max(left_height, right_height) + 1

### Basic Height

```py
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

**LC References:** 104, 559

### Balanced Tree

Check if `|left_height - right_height| <= 1` for every node.

```py
def isBalanced(root):
    self.balanced = True

    def dfs(node):
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        if abs(l - r) > 1:
            self.balanced = False
        return 1 + max(l, r)

    dfs(root)
    return self.balanced
```

**LC References:** 110

### Find Deepest Nodes / LCA of Deepest

Return depth from each subtree. If both subtrees have the same max depth, current node is LCA.

```py
def lcaDeepestLeaves(root):
    self.ans = None
    self.deepest = 0

    def dfs(node, d):
        self.deepest = max(self.deepest, d)
        if not node:
            return d
        l = dfs(node.left, d + 1)
        r = dfs(node.right, d + 1)
        if l == r == self.deepest:
            self.ans = node
        return max(l, r)

    dfs(root, 0)
    return self.ans
```

**LC References:** 1123, 865, 1302

## Path Problems

### Root-to-Leaf Path (Top-Down)

Pass accumulated state from parent to child.

```py
def hasPathSum(root, target):
    def dfs(node, curr_sum):
        if not node:
            return False
        curr_sum += node.val
        if not node.left and not node.right:
            return curr_sum == target
        return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, 0)
```

**LC References:** 112, 113, 129, 257, 1022

### Any Root-to-Node Path Sum (Prefix Sum + Backtracking)

Count paths with sum = target, where path can start at any ancestor.

Key insight: use prefix sum hash table, backtrack to restore state.

```py
def pathSum(root, target):
    cnt = Counter([0])  # prefix 0 with count 1
    self.ans = 0

    def dfs(node, prefix):
        if not node:
            return
        prefix += node.val
        self.ans += cnt[prefix - target]
        cnt[prefix] += 1
        dfs(node.left, prefix)
        dfs(node.right, prefix)
        cnt[prefix] -= 1  # backtrack

    dfs(root, 0)
    return self.ans
```

**LC References:** 437

### Node-to-Node Path (Path Aggregation)

Max path sum where path can be between any two nodes (doesn't have to go through root).

Key insight: at each node, consider left + root + right as a candidate. Return max single-sided path to parent.

```py
def maxPathSum(root):
    self.ans = float('-inf')

    def dfs(node):
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        # consider this node as the "peak" of a path
        self.ans = max(self.ans, l + node.val + r)
        # return max single-sided path to parent (or 0 if negative)
        return max(node.val + l, node.val + r, 0)

    dfs(root)
    return self.ans
```

**LC References:** 124

### Diameter (Longest Path Between Any Two Nodes)

Similar to path aggregation, but count edges instead of sum.

```py
def diameterOfBinaryTree(root):
    self.ans = 0

    def dfs(node):
        if not node:
            return 0
        l = dfs(node.left)
        r = dfs(node.right)
        self.ans = max(self.ans, l + r)  # diameter through this node
        return max(l, r) + 1  # height of this subtree

    dfs(root)
    return self.ans
```

**LC References:** 543, 687, 298, 549

## Binary Search Tree (BST)

### BST Property

Inorder traversal of BST gives sorted values.

```py
def inorderTraversal(root):
    result = []
    def dfs(node):
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    dfs(root)
    return result
```

**LC References:** 230, 530, 783, 501

### Reverse Inorder (Right, Root, Left)

Useful for cumulative sum from largest to smallest.

```py
def bstToGst(root):
    self.sum = 0

    def dfs(node):
        if not node:
            return
        dfs(node.right)  # visit larger values first
        self.sum += node.val
        node.val = self.sum
        dfs(node.left)

    dfs(root)
    return root
```

**LC References:** 1038, 538

### BST Operations

**Search:**
```py
def searchBST(root, val):
    if not root or root.val == val:
        return root
    if val < root.val:
        return searchBST(root.left, val)
    return searchBST(root.right, val)
```

**Insert:**
```py
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
```

**LC References:** 700, 701, 669, 450

## Tree Construction

### From Preorder + Inorder

Key insight: first element in preorder is root. Find root in inorder to split left/right subtrees.

```py
def buildTree(preorder, inorder):
    if not inorder:
        return None
    root_val = preorder.pop(0)
    idx = inorder.index(root_val)
    root = TreeNode(root_val)
    root.left = buildTree(preorder, inorder[:idx])
    root.right = buildTree(preorder, inorder[idx + 1:])
    return root
```

**LC References:** 105, 106, 889, 1008

## Serialization

### Preorder Serialization

Use preorder with markers for null nodes.

```py
def serialize(root):
    def dfs(node):
        if not node:
            return ['#']
        return [str(node.val)] + dfs(node.left) + dfs(node.right)
    return ','.join(dfs(root))

def deserialize(data):
    vals = iter(data.split(','))
    def dfs():
        val = next(vals)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node
    return dfs()
```

**LC References:** 297, 449

### Subtree Serialization (Detect Duplicates)

Serialize each subtree to detect duplicates.

```py
def findDuplicateSubtrees(root):
    seen = defaultdict(list)

    def dfs(node):
        if not node:
            return '#'
        serial = f"({dfs(node.left)}){node.val}({dfs(node.right)})"
        seen[serial].append(node)
        return serial

    dfs(root)
    return [nodes[0] for nodes in seen.values() if len(nodes) > 1]
```

**LC References:** 652

## Tree to Graph Conversion

For problems where you need bidirectional traversal (e.g., distance from any node).

```py
def buildGraph(root):
    G = defaultdict(list)

    def dfs(node, parent):
        if not node:
            return
        if parent:
            G[node].append(parent)
            G[parent].append(node)
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)
    return G
```

Then use BFS/DFS on the graph for queries.

**LC References:** 863

## Rerooting (Moving Root)

For problems where answer depends on which node is the root. Compute answer for one root, then adjust for all other nodes.

Key insight: `f(child) = f(parent) + adjustment`, where adjustment depends on subtree sizes.

### Template

```py
def reroot(n, edges):
    G = defaultdict(list)
    for u, v in edges:
        G[u].append(v)
        G[v].append(u)

    # Step 1: Pick node 0 as root, compute subtree sizes
    subtree = [0] * n
    seen = [False] * n
    seen[0] = True

    def count_subtree(i):
        size = 1
        for j in G[i]:
            if not seen[j]:
                seen[j] = True
                size += count_subtree(j)
        subtree[i] = size
        return size

    count_subtree(0)

    # Step 2: Compute answer for root 0
    ans = [0] * n
    seen = [False] * n
    seen[0] = True

    def compute_root_ans(i):
        # compute ans[0] using subtree info
        pass

    ans[0] = compute_root_ans(0)

    # Step 3: Reroot to compute answers for all nodes
    seen = [False] * n
    seen[0] = True

    def reroot_dfs(i, parent_ans):
        ans[i] = parent_ans
        for j in G[i]:
            if not seen[j]:
                seen[j] = True
                # adjust parent_ans to get ans[j]
                # typically: ans[j] = ans[i] + (n - subtree[j]) - subtree[j]
                child_ans = adjust(parent_ans, subtree[j], n)
                reroot_dfs(j, child_ans)

    reroot_dfs(0, ans[0])
    return ans
```

**Key Formula:** If we move root from `parent` to `child`:
- Nodes in child's subtree get closer (subtract `subtree[child]`)
- Nodes outside child's subtree get farther (add `n - subtree[child]`)
- Adjustment: `f(child) = f(parent) + (n - subtree[child]) - subtree[child]`

**LC References:** 834, 1685, 2121, 2458, 2581

## State Machine on Tree

For problems where each node can be in one of several states, and state transitions depend on children's states.

### Example: Binary Tree Cameras

States:
- 0: leaf (not covered)
- 1: covered without camera
- 2: covered with camera

```py
def minCameraCover(root):
    self.ans = 0

    def dfs(node):
        if not node:
            return 1  # null is considered covered
        l = dfs(node.left)
        r = dfs(node.right)

        # if any child is not covered, place camera here
        if l == 0 or r == 0:
            self.ans += 1
            return 2

        # if any child has camera, current is covered
        if l == 2 or r == 2:
            return 1

        # both children covered without camera, current is leaf
        return 0

    # handle root being a leaf
    if dfs(root) == 0:
        self.ans += 1

    return self.ans
```

**LC References:** 968, 979, 2973

## Subtree Properties

### Validate BST

```py
def isValidBST(root):
    def dfs(node, min_val, max_val):
        if not node:
            return True
        if not (min_val < node.val < max_val):
            return False
        return (dfs(node.left, min_val, node.val) and
                dfs(node.right, node.val, max_val))

    return dfs(root, float('-inf'), float('inf'))
```

**LC References:** 98

### Count Good Nodes (All nodes on path are smaller)

```py
def goodNodes(root):
    def dfs(node, max_so_far):
        if not node:
            return 0
        count = 1 if node.val >= max_so_far else 0
        max_so_far = max(max_so_far, node.val)
        count += dfs(node.left, max_so_far)
        count += dfs(node.right, max_so_far)
        return count

    return dfs(root, float('-inf'))
```

**LC References:** 1448, 3249

## Special Patterns

### Parent Tracking

For problems needing access to parent node.

```py
def buildParentMap(root):
    parent = {root: None}

    def dfs(node):
        if not node:
            return
        if node.left:
            parent[node.left] = node
            dfs(node.left)
        if node.right:
            parent[node.right] = node
            dfs(node.right)

    dfs(root)
    return parent
```

**LC References:** 2096

### Multi-Pass DFS

Some problems require multiple DFS passes to collect different information.

**LC References:** 2458, 2641

## Time Complexity

- Most tree DFS: O(n) where n = number of nodes
- BST search: O(h) where h = height (O(log n) balanced, O(n) skewed)
- Rerooting: O(n) with careful implementation
- Serialization: O(n)

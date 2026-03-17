# Lowest Common Ancestor (LCA)

## When to Use

| Problem Signal | Technique |
|---|---|
| Find LCA of 2 nodes in binary tree | Basic DFS template |
| Find LCA of 2 nodes in BST | BST property (value comparison) |
| Find LCA with parent pointers | Two-pointer traversal upward |
| Find LCA of multiple nodes | Generalized DFS template (set-based) |
| Node existence not guaranteed | Modified DFS with existence flags |
| Find k-th ancestor queries (online) | Binary lifting |
| Find LCA in complete binary tree by node number | Implicit parent (divide by 2) |
| Batch ancestor queries with preprocessing | Binary lifting + LCA |

## Basic LCA Template

**Key insight**: If left and right subtrees each contain one target, current node is the LCA. Otherwise, propagate whichever side found a target.

**LC**: 236

```py
def lowestCommonAncestor(root, p, q):
    def dfs(node):
        if not node:
            return None
        if node == p or node == q:
            return node
        l = dfs(node.left)
        r = dfs(node.right)
        if l and r:
            return node
        return l or r
    return dfs(root)
```

**Time**: O(n), **Space**: O(h) for recursion stack

## Variant 1: BST-specific LCA

**Key insight**: In BST, if current node value is between p and q, it's the LCA. Otherwise, recurse toward the range.

**LC**: 235

```py
def lowestCommonAncestor(root, p, q):
    if p.val > q.val:
        p, q = q, p

    def dfs(node):
        if not node:
            return None
        if p.val <= node.val <= q.val:
            return node
        elif node.val < p.val:
            return dfs(node.right)
        else:
            return dfs(node.left)

    return dfs(root)
```

**Time**: O(h), **Space**: O(h)

## Variant 2: With parent pointers

**Key insight**: Traverse from p to root, mark visited. Then traverse from q to root, first marked node is LCA.

**LC**: 1650

```py
def lowestCommonAncestor(p, q):
    visited = set()
    while p:
        visited.add(p)
        p = p.parent
    while q:
        if q in visited:
            return q
        q = q.parent
```

**Time**: O(h), **Space**: O(h)

## Variant 3: Multiple nodes (generalized)

**Key insight**: Same template as basic LCA, but check if current node is in the target set.

**LC**: 1676

```py
def lowestCommonAncestor(root, nodes):
    vals = set(n.val for n in nodes)

    def dfs(node):
        if not node:
            return None
        if node.val in vals:
            return node
        l = dfs(node.left)
        r = dfs(node.right)
        if l and r:
            return node
        return l or r

    return dfs(root)
```

**Time**: O(n), **Space**: O(h + k) where k = number of target nodes

## Variant 4: Node existence not guaranteed

**Key insight**: Track whether both nodes were found. Return None if either is missing.

**LC**: 1644

```py
def lowestCommonAncestor(root, p, q):
    found_p = found_q = False

    def dfs(node):
        nonlocal found_p, found_q
        if not node:
            return None
        l = dfs(node.left)
        r = dfs(node.right)
        if node == p:
            found_p = True
            return node
        elif node == q:
            found_q = True
            return node
        elif l and r:
            return node
        else:
            return l or r

    ans = dfs(root)
    return ans if found_p and found_q else None
```

**Time**: O(n), **Space**: O(h)

## Variant 5: Implicit tree (complete binary tree by index)

**Key insight**: In a complete binary tree numbered from 1, parent of node i is i // 2. Keep dividing the larger index until both meet.

**LC**: 2509

```py
def cycleLengthQueries(n, queries):
    ans = []
    for i, j in queries:
        cnt = 1
        while i != j:
            if i > j:
                i //= 2
            else:
                j //= 2
            cnt += 1
        ans.append(cnt)
    return ans
```

**Time per query**: O(log n), **Space**: O(1)

## Binary Lifting

**Key insight**: Precompute the 2^j-th ancestor for every node. Jump by powers of 2 to find k-th ancestor in O(log k) per query.

**LC**: 1483

Binary lifting is a technique used to find the k-th ancestor of any node in a tree in O(log n). This also leads to a faster algorithm in finding the lowest common ancestor (LCA) between two nodes in a tree. It can also be used to compute functions such as minimum, maximum and sum between two nodes of a tree in logarithmic time. The technique requires preprocessing the tree in O(N log N) using dynamic programming.

### Template

```py
"""
dp[i][j] = 2^j-th parent of node i
Base case: dp[i][0] = parent[i]
Transition: dp[i][j] = dp[dp[i][j-1]][j-1]

Use binary representation of k to jump through dp table.
"""
class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        m = 1 + int(log2(n))  # max depth
        self.dp = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if j == 0:
                    self.dp[i][0] = parent[i]  # 2^0 parent
                elif self.dp[i][j-1] != -1:
                    self.dp[i][j] = self.dp[self.dp[i][j-1]][j-1]

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0 and node != -1:
            i = int(log2(k))
            node = self.dp[node][i]
            k -= (1 << i)
        return node
```

**Preprocessing**: O(n log n), **Query**: O(log k), **Space**: O(n log n)

### Binary Lifting for LCA

To find LCA of two nodes u and v:
1. Bring both nodes to the same depth using binary lifting
2. If they're the same, that's the LCA
3. Otherwise, lift both upward simultaneously by powers of 2, stopping just before they meet

```py
def lca(u, v, depth, ancestor):
    # Bring to same depth
    if depth[u] < depth[v]:
        u, v = v, u
    diff = depth[u] - depth[v]
    for i in range(int(log2(diff)) + 1):
        if diff & (1 << i):
            u = ancestor.getKthAncestor(u, 1 << i)

    if u == v:
        return u

    # Binary search for LCA
    for i in reversed(range(int(log2(depth[u])) + 1)):
        if ancestor.dp[u][i] != ancestor.dp[v][i]:
            u = ancestor.dp[u][i]
            v = ancestor.dp[v][i]

    return ancestor.dp[u][0]  # parent of u (or v)
```

**Time**: O(log n) per query after O(n log n) preprocessing

## Reference

- [Binary Lifting with k-th ancestor and lowest common ancestor](https://iq.opengenus.org/binary-lifting-k-th-ancestor-lowest-common-ancestor)
- [Errichto tutorial](https://www.youtube.com/watch?v=oib-XsjFa-M)

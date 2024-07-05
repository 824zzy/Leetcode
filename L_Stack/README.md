# Stack

## Monotonic Stack

The monotonic increasing stack and monotonic decreasing stack, namely monotonic stack, is a very powerful tool for finding next greater/smaller element.
More specifically, always **use monotonic increasing stack when we are trying to find the next smaller element, vice versa.**
And in the template, `A[stk[-1]]>A[i]` indicates a monotonic increasing stack.

### Template

Basic template:

``` py
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]]?A[i]:
        `logic`
        stk.pop()
    `logic`
    stk.append([i, A[i]])
return ans
```

Two pass to find next smaller elements:

``` py
# next smaller on the right
R = [len(A)]*len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]]>A[i]:
        R[stk.pop()] = i
    stk.append(i)

# next smaller on the left
L = [-1]*len(A)
stk = []
for i in reversed(range(len(A))):
    while stk and A[stk[-1]]>=A[i]:
        L[stk.pop()] = i
    stk.append(i)
```

Two pass to find next greater elements:

``` py
# next greater on the right
R = [len(A)]*len(A)
stk = []
for i in range(len(A)):
    while stk and A[stk[-1]]<A[i]:
        R[stk.pop()] = i
    stk.append(i)

# next greater on the left
L = [-1]*len(A)
stk = []
for i in reversed(range(len(A))):
    while stk and A[stk[-1]]<A[i]:
        L[stk.pop()] = i
    stk.append(i)
```

## Farmost Smaller Greater Monotonic Stack Template

``` py
stk = []
for i in range(len(A)):
    if not stk or A[stk[-1]]>A[i]:
        stk.append(i)

ans = 0
for i in reversed(range(len(A))):
    while stk and A[stk[-1]]<A[i]:
        ans = max(ans, i-stk.pop())
return ans
```


## Eulerian Path: Hierholzer's Algorithm

For directed connected graph:

``` py
def hierholzer(pairs):
    G = defaultdict(list)
        degree = defaultdict(int) # out-degree
        for i, j in pairs:
            G[i].append(j)
            degree[i] += 1
            degree[j] -= 1
        
        # find node x whose out-degree is 1
        for n in degree:
            if degree[n]==1:
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



##  Iterative Tree Traversal by Stack

``` py
Pre order, In order, Post order: stack

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

# Binary Indexed Tree(Fenwich Tree)

## Motivation

Fenwick tree is proposed to solve the prefix sum problem.
The idea is to **store partial sum** in each node and get total sum by traversing the tree from leaf to root.
The tree has a height of log(n).
Query: O(log(n))
Update: O(log(n))

![fenwick tree](img/fenwick_tree.png)

## Template

``` py
l = max(A)
s = [0] * len(l+1)
def update(x):
    while x<=l:
        s[x] += 1
        x += x & -x

def get(x):
    ans = 0
    while x>0:
        ans += c[x]
        x -= x & -x

ans = 0
for i, a in enumerate(A):
    `logic`
    update(a)
return ans
```

## Reference

1. [花花酱 Fenwick Tree / Binary Indexed Tree - 刷题找工作 SP3](https://www.youtube.com/watch?v=WbafSgetDDk)
